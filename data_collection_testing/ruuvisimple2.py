# Sample script for forever loop

from ruuvitag_sensor.ruuvi import RuuviTagSensor
import time
from datetime import datetime
import json

macs = []
timeout_in_sec = 20
dateTimeObj = datetime.now()

datas = RuuviTagSensor.get_data_for_sensors(macs, timeout_in_sec)

#print("" + str(dateTimeObj) + " " + str(datas))

ruuvidata = {}
ruuvidata["ts"] = str(datetime.now())
ruuvidata["data"] = datas

jsonstr = json.dumps(ruuvidata)
print(jsonstr)

time.sleep(5)

# End of file
