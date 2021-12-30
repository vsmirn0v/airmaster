This script provides polling mechanism with json output for Weeksky Instruments Air Master 2 AM7 p indoor air quality detector, if equipped with wifi module.

Single request:

python3 ./scrape.py -h 192.168.88.13

Continous poll:

python3 ./scrape.py -h 192.168.88.13 poll


Example output:
```
❯ python3 ./scrape.py poll
{
    "PM2.5": "10",
    "PM10": "12",
    "HCHO": "0.10",
    "TVOC": "1.13",
    "CO2": "655",
    "TEMP": "23.90",
    "RH": "63.00"
}
{
    "PM2.5": "9",
    "PM10": "11",
    "HCHO": "0.09",
    "TVOC": "1.13",
    "CO2": "656",
    "TEMP": "23.90",
    "RH": "63.00"
}
{
    "PM2.5": "10",
    "PM10": "12",
    "HCHO": "0.10",
    "TVOC": "1.13",
    "CO2": "655",
    "TEMP": "23.80",
    "RH": "62.90"
}
```
