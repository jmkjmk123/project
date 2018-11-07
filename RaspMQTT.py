import spidev
import time
import os
import paho.mqtt.client as mqtt

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

delay = 5 #data transfer delay = 5 sec
execute_time = 60 # execution time = 60 sec
temp_channel = 0 # tmp using ch.0 of MCP
light_channel = 1 # cds using ch.1 of MCP
broker="broker's IP"
publisher = mqtt.Client("Rasp")
publisher.connect(broker)
start_time=time.time()
while True:
 
 print "--------------------------------"

 temp_level = ReadAdc(temp_channel)
 temp_volt = ConvertVolt(temp_level,2)
 temp = ConvertTMP36(temp_level,2)
 times = time.localtime(time.time()+32400)
 tstr = time.strftime("%Y-%m-%d %H:%M:%S", times)
 print(tstr)
 publisher.publish("CLK",tstr)
 print("TMP36 : Data {} ({}V) {} C".format(temp_level, temp_volt, temp))
 temp_str=`temp`
 publisher.publish("TMP",temp_str)
 light_level = ReadAdc(light_channel)
 light_volt = ConvertVolt(light_level,2)
 print("Light : Data {} ({}V)".format(light_level, light_volt))
 light_str=`light_level`
 publisher.publish("CDS",light_str)
 time.sleep(delay)
 curr_time=time.time()
 if (curr_time - start_time) > execute_time :
  publisher.publish("Exit","off")
  break
 os.system('clear')
print("time out" + '\n')
