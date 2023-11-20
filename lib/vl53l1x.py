from machine import Pin
from utime import sleep_ms

_VL53L1X_I2C_SLAVE_DEVICE_ADDRESS = 0x0001
VL51L1X_DEFAULT_CONFIGURATION = bytes([
    # 0x2d : set bit 2 and 5 to 1 for fast plus mode (1MHz I2C), else don't touch */
    0x00,
    # 0x2e : bit 0 if I2C pulled up at 1.8V, else set bit 0 to 1 (pull up at AVDD) */
    0x00,
    # 0x2f : bit 0 if GPIO pulled up at 1.8V, else set bit 0 to 1 (pull up at AVDD) */
    0x00,
    # 0x30 : set bit 4 to 0 for active high interrupt and 1 for active low (bits 3:0 must be 0x1), use SetInterruptPolarity() */
    0x01,
    0x02,  # 0x31 : bit 1 = interrupt depending on the polarity, use CheckForDataReady() */
    0x00,  # 0x32 : not user-modifiable */
    0x02,  # 0x33 : not user-modifiable */
    0x08,  # 0x34 : not user-modifiable */
    0x00,  # 0x35 : not user-modifiable */
    0x08,  # 0x36 : not user-modifiable */
    0x10,  # 0x37 : not user-modifiable */
    0x01,  # 0x38 : not user-modifiable */
    0x01,  # 0x39 : not user-modifiable */
    0x00,  # 0x3a : not user-modifiable */
    0x00,  # 0x3b : not user-modifiable */
    0x00,  # 0x3c : not user-modifiable */
    0x00,  # 0x3d : not user-modifiable */
    0xff,  # 0x3e : not user-modifiable */
    0x00,  # 0x3f : not user-modifiable */
    0x0F,  # 0x40 : not user-modifiable */
    0x00,  # 0x41 : not user-modifiable */
    0x00,  # 0x42 : not user-modifiable */
    0x00,  # 0x43 : not user-modifiable */
    0x00,  # 0x44 : not user-modifiable */
    0x00,  # 0x45 : not user-modifiable */
    0x20,  # 0x46 : interrupt configuration 0->level low detection, 1-> level high, 2-> Out of window, 3->In window, 0x20-> New sample ready , TBC */
    0x0b,  # 0x47 : not user-modifiable */
    0x00,  # 0x48 : not user-modifiable */
    0x00,  # 0x49 : not user-modifiable */
    0x02,  # 0x4a : not user-modifiable */
    0x0a,  # 0x4b : not user-modifiable */
    0x21,  # 0x4c : not user-modifiable */
    0x00,  # 0x4d : not user-modifiable */
    0x00,  # 0x4e : not user-modifiable */
    0x05,  # 0x4f : not user-modifiable */
    0x00,  # 0x50 : not user-modifiable */
    0x00,  # 0x51 : not user-modifiable */
    0x00,  # 0x52 : not user-modifiable */
    0x00,  # 0x53 : not user-modifiable */
    0xc8,  # 0x54 : not user-modifiable */
    0x00,  # 0x55 : not user-modifiable */
    0x00,  # 0x56 : not user-modifiable */
    0x38,  # 0x57 : not user-modifiable */
    0xff,  # 0x58 : not user-modifiable */
    0x01,  # 0x59 : not user-modifiable */
    0x00,  # 0x5a : not user-modifiable */
    0x08,  # 0x5b : not user-modifiable */
    0x00,  # 0x5c : not user-modifiable */
    0x00,  # 0x5d : not user-modifiable */
    0x01,  # 0x5e : not user-modifiable */
    0xdb,  # 0x5f : not user-modifiable */
    0x0f,  # 0x60 : not user-modifiable */
    0x01,  # 0x61 : not user-modifiable */
    0xf1,  # 0x62 : not user-modifiable */
    0x0d,  # 0x63 : not user-modifiable */
    # 0x64 : Sigma threshold MSB (mm in 14.2 format for MSB+LSB), use SetSigmaThreshold(), default value 90 mm  */
    0x01,
    0x68,  # 0x65 : Sigma threshold LSB */
    # 0x66 : Min count Rate MSB (MCPS in 9.7 format for MSB+LSB), use SetSignalThreshold() */
    0x00,
    0x80,  # 0x67 : Min count Rate LSB */
    0x08,  # 0x68 : not user-modifiable */
    0xb8,  # 0x69 : not user-modifiable */
    0x00,  # 0x6a : not user-modifiable */
    0x00,  # 0x6b : not user-modifiable */
    0x00,  # 0x6c : Intermeasurement period MSB, 32 bits register, use SetIntermeasurementInMs() */
    0x00,  # 0x6d : Intermeasurement period */
    0x0f,  # 0x6e : Intermeasurement period */
    0x89,  # 0x6f : Intermeasurement period LSB */
    0x00,  # 0x70 : not user-modifiable */
    0x00,  # 0x71 : not user-modifiable */
    # 0x72 : distance threshold high MSB (in mm, MSB+LSB), use SetD:tanceThreshold() */
    0x00,
    0x00,  # 0x73 : distance threshold high LSB */
    # 0x74 : distance threshold low MSB ( in mm, MSB+LSB), use SetD:tanceThreshold() */
    0x00,
    0x00,  # 0x75 : distance threshold low LSB */
    0x00,  # 0x76 : not user-modifiable */
    0x01,  # 0x77 : not user-modifiable */
    0x0f,  # 0x78 : not user-modifiable */
    0x0d,  # 0x79 : not user-modifiable */
    0x0e,  # 0x7a : not user-modifiable */
    0x0e,  # 0x7b : not user-modifiable */
    0x00,  # 0x7c : not user-modifiable */
    0x00,  # 0x7d : not user-modifiable */
    0x02,  # 0x7e : not user-modifiable */
    0xc7,  # 0x7f : ROI center, use SetROI() */
    0xff,  # 0x80 : XY ROI (X=Width, Y=Height), use SetROI() */
    0x9B,  # 0x81 : not user-modifiable */
    0x00,  # 0x82 : not user-modifiable */
    0x00,  # 0x83 : not user-modifiable */
    0x00,  # 0x84 : not user-modifiable */
    0x01,  # 0x85 : not user-modifiable */
    0x01,  # 0x86 : clear interrupt, use ClearInterrupt() */
    0x40  # 0x87 : start ranging, use StartRanging() or StopRanging(), If you want an automatic start after VL53L1X_init() call, put 0x40 in location 0x87 */
])


class VL53L1X:
    def __init__(self, i2c, xshut_pin, old_address=0x29, new_address=0x29):
        self.xshut_pin = Pin(xshut_pin, Pin.OUT)
        self.xshut_pin.value(0)
        sleep_ms(10)
        self.xshut_pin.value(1)
        self.i2c = i2c
        self.address = old_address
        self.reset()
        sleep_ms(1)
        if self.read_model_id() != 0xEACC:
            raise RuntimeError(
                'Failed to find expected ID register values. Check wiring!')
        # write default configuration
        # print("Old address: ", hex(self.address))
        self.i2c.writeto_mem(self.address, _VL53L1X_I2C_SLAVE_DEVICE_ADDRESS, bytes([new_address]), addrsize=16)
        sleep_ms(100)
        self.address = new_address
        self.i2c.writeto_mem(self.address, 0x2D,
                             VL51L1X_DEFAULT_CONFIGURATION, addrsize=16)
        sleep_ms(100)
        slave_device_address = self.i2c.readfrom_mem(self.address,
              _VL53L1X_I2C_SLAVE_DEVICE_ADDRESS, 1, addrsize=16)[0]
        # print("New address: ", hex(slave_device_address))
        # the API triggers this change in VL53L1_init_and_start_range() once a
        # measurement is started; assumes MM1 and MM2 are disabled
        self.writeReg16Bit(0x001E, self.readReg16Bit(0x0022) * 4)
        sleep_ms(200)

    def calibration(self, alpha=0.05, samples=10, ledF=None, ledT=None):
        raw_array = []
        ajusted_array = []
        ajusted = self.read()
        ledState = True
        for i in range(samples):
            sleep_ms(1000)
            ledState = not ledState
            if ledF:
                ledF.value(ledState)
            raw = self.read()
            ajusted = (alpha * raw) + ((1-alpha) * ajusted)
            raw_array.append(raw)
            ajusted_array.append(ajusted)
            print("-{} Raw: {}; Ajusted: {}".format(i+1, raw, ajusted))
        raw_acc = 0
        ajusted_acc = 0
        for raw in raw_array:
            raw_acc += raw
        for ajusted in ajusted_array:
            ajusted_acc += ajusted
        mean_raw = raw_acc / len(raw_array)
        mean_ajusted = ajusted_acc / len(ajusted_array)
        if ledT:
            ledT.value(True)
            sleep_ms(1000)
            ledT.value(False)
        print("Mean raw: {} [mm]; Mean ajusted: {} [mm]".format(mean_raw, mean_ajusted))
        return mean_ajusted*0.7 if mean_ajusted <= mean_raw else mean_raw*0.7

    def inOut(self, sensor_1, sensor_2, treshold_1, treshold_2, led, capacity, state, count, ledState):
        distance_1 = sensor_1.read()
        if state == 0 and distance_1 < treshold_1:
            state = 1
        # else:
        distance_2 = sensor_2.read()
        if state == 0 and distance_2 < treshold_2:
            state = 2
        sleep_ms(25)
        # print("range_1: {} mm - range_2: {} mm".format(distance_1, distance_2))
        if state == 1 and distance_2 < treshold_2:
            state = 0
            count = 0
            capacity += 1
            ledState = not(ledState)
            sleep_ms(1000)
        elif state == 2 and distance_1 < treshold_1:
            state = 0
            count = 0
            capacity -= 1
            ledState = not(ledState)
            sleep_ms(1000)
        elif state != 0:
            count += 1
        if count >= 120:
            count = 0
            state = 0
        if capacity <= 0:
            capacity = 0
        led.value(ledState)
        return [capacity, state, count, ledState]


    def writeReg(self, reg, value):
        try:
            return self.i2c.writeto_mem(self.address, reg, bytes([value]), addrsize=16)        
        except OSError:
            self.address = 0x29
            print("Exception rising: ", hex(self.address))
            return self.i2c.writeto_mem(self.address, reg, bytes([value]), addrsize=16)        
            
    def writeReg16Bit(self, reg, value):
        return self.i2c.writeto_mem(self.address, reg, bytes([(value >> 8) & 0xFF, value & 0xFF]), addrsize=16)

    def readReg(self, reg):
        return self.i2c.readfrom_mem(self.address, reg, 1, addrsize=16)[0]

    def readReg16Bit(self, reg):
        data = self.i2c.readfrom_mem(self.address, reg, 2, addrsize=16)
        return (data[0] << 8) + data[1]

    def read_model_id(self):
        return self.readReg16Bit(0x010F)

    def reset(self):
        self.writeReg(0x0000, 0x00)
        sleep_ms(100)
        self.writeReg(0x0000, 0x01)

    def read(self):
        data = self.i2c.readfrom_mem(
            self.address, 0x0089, 17, addrsize=16)  # RESULT__RANGE_STATUS
        range_status = data[0]
        # report_status = data[1]
        stream_count = data[2]
        dss_actual_effective_spads_sd0 = (data[3] << 8) + data[4]
        # peak_signal_count_rate_mcps_sd0 = (data[5]<<8) + data[6]
        ambient_count_rate_mcps_sd0 = (data[7] << 8) + data[8]
        # sigma_sd0 = (data[9]<<8) + data[10]
        # phase_sd0 = (data[11]<<8) + data[12]
        final_crosstalk_corrected_range_mm_sd0 = (data[13] << 8) + data[14]
        peak_signal_count_rate_crosstalk_corrected_mcps_sd0 = (
            data[15] << 8) + data[16]
        #status = None
        # if range_status in (17, 2, 1, 3):
        #status = "HardwareFail"
        # elif range_status == 13:
        #status = "MinRangeFail"
        # elif range_status == 18:
        #status = "SynchronizationInt"
        # elif range_status == 5:
        #status = "OutOfBoundsFail"
        # elif range_status == 4:
        #status = "SignalFail"
        # elif range_status == 6:
        #status = "SignalFail"
        # elif range_status == 7:
        #status = "WrapTargetFail"
        # elif range_status == 12:
        #status = "XtalkSignalFail"
        # elif range_status == 8:
        #status = "RangeValidMinRangeClipped"
        # elif range_status == 9:
        # if stream_count == 0:
        #status = "RangeValidNoWrapCheckFail"
        # else:
        #status = "OK"
        return final_crosstalk_corrected_range_mm_sd0