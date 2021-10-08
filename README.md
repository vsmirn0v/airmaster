!!! KNOWN BUG: TEMPERATURE READING IS NOT CORRECT !!!


Single request:

python3 ./scrape.py -h 192.168.88.13

Continous poll:

python3 ./scrape.py -h 192.168.88.13 poll


Example output:

❯ python3 ./scrape.py poll
{
    "PM2.5": "19",
    "PM10": "20",
    "HCHO": "0.02",
    "TVOC": "0.31",
    "CO2": "556",
    "TEMP": "22.78",
    "RH": "36.90"
}
{
    "PM2.5": "19",
    "PM10": "21",
    "HCHO": "0.01",
    "TVOC": "0.31",
    "CO2": "557",
    "TEMP": "22.78",
    "RH": "37.00"
}
{
    "PM2.5": "19",
    "PM10": "21",
    "HCHO": "0.02",
    "TVOC": "0.31",
    "CO2": "558",
    "TEMP": "22.78",
    "RH": "37.00"
}