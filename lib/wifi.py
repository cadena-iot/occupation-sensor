# from index import html
import ujson
import network
import urequests
import ntptime
from machine import RTC
from utime import sleep_ms, localtime

class Wifi:

  def __init__(self, ssid, password):
    count = 0
    self.ssid = ssid
    self.password = password
    self.station = network.WLAN(network.STA_IF)
    if self.station.active():
      self.station.active(False)
    self.station.active(True)
    while len(self.station.scan()) == 0:
      count += 1
      print(count)
      sleep_ms(1000)

  def scan(self):
    enable_networks = self.station.scan()
    print("Available networks: \n{}\n".format([x[0] for x in enable_networks]))

  def connect(self, timeout=60000, ledF=None, ledT=None):
    count = 0
    ledState = True
    try:
      self.station.connect(self.ssid, self.password)
      while not self.station.isconnected() and count < timeout:
        count += 500
        ledState = not ledState
        if ledF:
          ledF.value(ledState)
        sleep_ms(500)
      if self.station.isconnected():
        if ledT:
          ledT.value(True)
          sleep_ms(1000)
          ledT.value(False)
          print("connected to the network: {}".format(self.ssid))
    except OSError as e:
      print("Error al conectar a la red WiFi: {}".format(e))

  def isConnected(self):
    return self.station.isconnected()

  def timeSync(self, ds3231):
    try:
      print("Local time before synchronization：%s" % str(localtime()))
      ntptime.settime()
      (year, month, day, weekday, hour, minute, second, milisecond) = RTC().datetime()
      RTC().init((year, month, day, weekday, hour-5, minute, second, milisecond))
      print("Local time after synchronization：%s" % str(localtime()))
      ds3231.datetime(localtime()[:-2])
    except OSError as e:
      print("Error syncing time: {}".format(e))

  def post(self, url="", headers={'content-type':'application/json'}, body={}, ds3231=None):
    if ds3231:
      body["date"] = "{}".format(ds3231.datetime()[:3])
      body["time"] = "{}".format(ds3231.datetime()[4:-1])
      # body["datetime"] = {
      #   "date": "{}".format(ds3231.datetime()[:3]),
      #   "time": "{}".format(ds3231.datetime()[4:-1])
      # }
    try:
      response = urequests.post(url, headers=headers, data=ujson.dumps(body)).json()
      return response
    except OSError as e:
      print("Error al enviar la data al servidor: {}".format(e))

# datetime = (year, month, mday, hour, minute, second, weekday)
# punto de acceso
# ap= network.WLAN(network.AP_IF)
# ap.active(True)
# ap.config(essid='ESP32')
# ap.config(authmode=network.AUTH_WPA_WPA2_PSK, password='Univalle')

# #ntptime.host = "1.co.pool.ntp.org"
