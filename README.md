# Weather Scraper


## Approach

### Important Endpoints

- <https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode=18.98%2C72.83&language=en-IN&units=m>
- <https://api.weather.com/v2/turbo/vt1observation?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&>geocode=18.98%2C72.83&language=en-IN&units=m>

- We need geocode for result retrieval
  - Geocode is latitude and longitude of an address.
  - We can use google map api for getting geocodes but it needs registration but we can use free service that provide geocodes and that provide api service too.
    - curl <https://geocode.xyz/{PLACE_NAME}?json=1>

- Get the json response and print it on terminal.

## Run as command line tool

- Uncomment "the argparse if" part and comment the app.run part.

## Run as Web Based Service

- Uncomment the "app.run if" part and comment the argparse part.

## How to install

- Download the file as zip.
- Open command prompt or terminal with  python3 installed in it.
- Traverse to the weather folder containing setup.py
- Type 'pip install -r requirements.txt'
- Type 'pip install .'
- After successful completion, the package can be imported as 'weather'

```shell
shell$ pip install .

Processing /mnt/d/weather
Installing collected packages: weather-scraper
  Running setup.py install for weather-scraper ... /
done
Successfully installed weather-scraper-0.1
```

- In python shell, after declaring main, place info must be passed to run the package

```
Python 3.6.8 (default, Jan 14 2019, 11:02:34)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import weather.main
```

## Web Based Service

- It uses flask as a service
  - Routes like api, api/v1, api/v1/weather

> Command

```C:\Users\Rai>curl -G http://127.0.0.1:5000/api/v1/weather?place=Mumbai```

> Output

```json
{
  "altimeter": 1008.13,
  "barometerChange": 2.03,
  "barometerCode": 1,
  "barometerTrend": "Rising",
  "dewPoint": 25,
  "feelsLike": 32,
  "gust": null,
  "humidity": 87,
  "icon": 21,
  "obsQualifierCode": null,
  "obsQualifierSeverity": null,
  "observationTime": "2019-09-11T20:09:29+0530",
  "phrase": "Haze",
  "precip24Hour": 46.74,
  "snowDepth": 0.0,
  "temperature": 27,
  "temperatureMaxSince7am": 29,
  "uvDescription": "Low",
  "uvIndex": 0,
  "visibility": 3.22,
  "windDirCompass": "S",
  "windDirDegrees": 190,
  "windSpeed": 8
}
```

>Command

```shell
python3 main.py --place Mumbai --forecast --monthly
```

>Output

```json
{
    "altimeter": 1007.11,
    "barometerTrend": "Rising",
    "barometerCode": 1,
    "barometerChange": 0.68,
    "dewPoint": 24,
    "feelsLike": 32,
    "gust": null,
    "humidity": 84,
    "icon": 11,
    "observationTime": "2019-09-11T18:24:15+0530",
    "obsQualifierCode": null,
    "obsQualifierSeverity": null,
    "phrase": "Light Rain",
    "precip24Hour": 45.97,
    "snowDepth": 0.0,
    "temperature": 27,
    "temperatureMaxSince7am": 29,
    "uvIndex": 0,
    "uvDescription": "Low",
    "visibility": 4.83,
    "windSpeed": 10,
    "windDirCompass": "SSW",
    "windDirDegrees": 210
}
```

## TODO

- The monthly and daily json respone are intermixed, need a little parsing
- The api endpoints need a little categorisation as it is not officially documented.

- Need a little parsing in large data
