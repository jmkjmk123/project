import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0,0)

def ReadAdc(chNum):
 if chNum > 7 or chNum < 0:
  return -1
 adc = spi.xfer2([1, (8+chNum) << 4, 0])
 data = ((adc[1] & 3) << 8) + adc[2]
 return data

def ConvertVolt(data, places):
 volt = (data * 3.3) / float(1023)
 volt = round(volt, places)
 return volt

def ConvertTMP36(data, places):
 temp =((data * 330) / float(1023)) - 50
 temp = round(temp, places)
 return temp

delay = 5
temp_channel = 0
light_channel = 1

while True:
 
 print "--------------------------------"

 temp_level = ReadAdc(temp_channel)
 temp_volt = ConvertVolt(temp_level,2)
 temp = ConvertTMP36(temp_level,2)
 print("TMP36 : Data {} ({}V) {} C".format(temp_level, temp_volt, temp))
 light_level = ReadAdc(light_channel)
 light_volt = ConvertVolt(light_level,2)
 print("Light : Data {} ({}V)".format(light_level, light_volt))
 time.sleep(delay)
