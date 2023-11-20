import os
from machine import Pin, SoftSPI
from sdcard import SDCard

# Montar el módulo micro SD
spisd = SoftSPI(-1, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
sd = SDCard(spisd, Pin(12))
#os.mount(SDCard(slot=2, width=1, sck=Pin(18), miso=Pin(19), mosi=Pin(23), cs=Pin(12)), "/sd")
body = {
  "device_id": "0x001",
  "lab_id": "XXXXXX",
  "aforo": 100
}
print("Root directory: {}".format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, "/sd")
print("Root directory: {}".format(os.listdir()))
os.chdir("sd")
print("SD Card contains: {}".format(os.listdir()))

# Abrir un archivo para escribir
f = open('/sd/test.txt', 'w')

# Escribir algunos datos en el archivo
# data = 'Este es un archivo de ejemplo.'
f.write(';{}'.format(body))

# Cerrar el archivo
f.close()