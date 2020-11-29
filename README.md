# Testing Ruuvi tags with python scripts

Dependencies:

## RuuviTag Sensor Python Package

Install `RuuviTag Sensor Python Package`

- https://github.com/ttu/ruuvitag-sensor
- `git clone https://github.com/ttu/ruuvitag-sensor.git`
- `pip install -e .`

Tested with `b9d1d976`.

## BlueZ

Installation commands:

- `sudo apt-get install bluez bluez-hcidump`

Testing:

- `sudo -n hcidump -i hci0 --raw`

Tested with `hcidump --version` 5.43.

## System versions

Raspberry Pi 3B', Raspbian GNU/Linux 9 (stretch)

```bash
$ python --version
Python 2.7.13

$ uname -a
Linux 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l GNU/Linux

$ cat /proc/cpuinfo | grep Rev
Revision	: a020d3
```
# Data collection

Start with command `./loop.sh > logfile.txt &` in `data_collection_testing` folder.
