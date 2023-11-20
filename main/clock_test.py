from machine import Pin, SoftI2C
from ds3231 import DS3231

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
ds = DS3231(i2c)

year = 2023 # Can be yyyy or yy format
month = 02
mday = 1
hour = 13 # 24 hour format only
minute = 55
second = 30 # Optional
weekday = 6 # Optional

datetime = (year, month, mday, hour, minute, second, weekday)
ds.datetime(datetime)
