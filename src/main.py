import time
import DATA

data = DATA.GetMeasures()

cTemp = data[0]
humidity = data[1]

print ("Temperature in Celsius : %.2f C" %cTemp)
print ("Relative Humidity : %.2f %%" %humidity)

