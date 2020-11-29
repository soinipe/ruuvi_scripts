# Sample script

from ruuvitag_sensor.ruuvi import RuuviTagSensor
import time
from datetime import datetime

def handle_data(found_data):
    data = {}
    data["ts"] = str(datetime.now())
    data["mac"] = found_data[0]
    data["data"] = found_data[1]
    #dateTimeObj = datetime.now()
    #print("" + str(dateTimeObj) + " " + found_data[0] + str(found_data[1]))
    print(data)

RuuviTagSensor.get_datas(handle_data)

# End of file
