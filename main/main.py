import os
import json
from micropython import const
from machine import Pin, SoftI2C, SoftSPI
from utime import sleep_ms, localtime

from sdcard import SDCard
from ds3231 import DS3231
from wifi import Wifi
from vl53l1x import VL53L1X

def main():
    ledR = Pin(25, Pin.OUT)
    ledG = Pin(33, Pin.OUT)
    ledB = Pin(32, Pin.OUT)
    ledR.value(True)

    # SD initialization
    cs = Pin(12)
    spisd = SoftSPI(-1, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
    sd = SDCard(spisd, cs)
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/sd")
    os.chdir("sd")
    print("SD Card contains: {}".format(os.listdir()))

    # External RTC initialization
    i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
    ds = DS3231(i2c)
    dsDateTime = list(ds.datetime()[:3])
    dsDateTime.extend(ds.datetime()[4:-2])

    # conectar al Wifi
    ssid = "univalle"
    password = "Univalle"
    url = "https://us-central1-sigelabx.cloudfunctions.net/itemsGenerateRegSensor-createRegistroSensor"
    body = {
        "device_id": "0x001",
        "lab_id": "XXXXXX",
        "state": "",
        "aforo": 0
    }
    wifi = Wifi(ssid=ssid, password=password)
    wifi.scan()
    wifi.connect(ledF=ledR, ledT=ledG)
    if dsDateTime != list(localtime()[:-3]):
        wifi.timeSync(ds)

    # Initialize the sensors
    # irq_pin_1 = Pin(26, Pin.IN)
    # irq_pin_2 = Pin(14, Pin.IN)
    XSHUT_PIN_1 = const(27)
    XSHUT_PIN_2 = const(13)
    i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
    sensor_1 = VL53L1X(i2c, XSHUT_PIN_1, 0x29, 0x31)
    sensor_2 = VL53L1X(i2c, XSHUT_PIN_2, 0x29, 0x32)
    treshold_1 = sensor_1.calibration(samples=10, ledF=ledB, ledT=ledG)
    treshold_2 = sensor_2.calibration(samples=10, ledF=ledB, ledT=ledG)
    print("{} - {}".format(treshold_1, treshold_2))

    capacity = 0
    oldCapacity = 0
    state = 0
    count = 0
    ledState = True

    # for address in i2c.scan():
    #     print("Available I2C address: ", hex(address))

    actual_hour = ds.datetime()[4]
    # actual_hour = 0

    print("Start reading")
    while True:
        ledR.value(False)
        ledG.value(False)
        if not wifi.isConnected():
            wifi.connect(timeout=2000)
            if dsDateTime != list(localtime()[:-3]):
                wifi.timeSync(ds)

        # newCapacity, state, count, ledState = sensor_1.inOut(sensor_1, sensor_2, treshold_1, treshold_2, ledR, state, capacity, count, ledState)
        if actual_hour != ds.datetime()[4]:
            print("Sending offline data")
            actual_hour = ds.datetime()[4]
            file = open('data.txt', 'r')
            info = file.read()
            info = info.split(';')[1:]
            for doc in info:
                sendBody = json.loads(doc.replace("'", '"'))
                response = wifi.post(url=url, body=sendBody)
                if response != 200:
                    file = open('/sd/newData.txt', 'a')
                    file.write(";{}".format(sendBody))
                    file.close()
            os.rename('newData.txt', 'data.txt')

        distance_1 = sensor_1.read()
        distance_2 = sensor_2.read()
        if state == 0 and distance_1 < treshold_1:
            state = 1
        # else:
        elif state == 0 and distance_2 < treshold_2:
            state = 2
        sleep_ms(10)

        # print("D1: {} mm; D2: {} mm; S: {}".format(distance_1, distance_2, state))
        if state == 1 and distance_2 < treshold_2:
            state = 0
            count = 0
            capacity += 1
            body["state"] = True
            ledState = not(ledState)
            # sleep_ms(10)
        elif state == 2 and distance_1 < treshold_1:
            state = 0
            count = 0
            capacity -= 1
            body["state"] = False
            ledState = not(ledState)
            # sleep_ms(10)
        elif state != 0:
            count += 1
            # print(count)
        if count >= 120:
            count = 0
            state = 0
        # if capacity <= 0:
        #     capacity = 0
        ledB.value(ledState)

        if oldCapacity != capacity:
            ledG.value(True)
            oldCapacity = capacity
            body["aforo"] = capacity
            response = wifi.post(url=url, body=body, ds3231=ds)
            print(response)
            print("Aforo: {}".format(body["aforo"]))
            print("-"*50)
            if response != 200:
                file = open('/sd/data.txt', 'a')
                file.write(";{}".format(body))
                file.close()

if __name__ == "__main__":
    main()
