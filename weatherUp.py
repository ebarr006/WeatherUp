#!/usr/bin/python
import urllib2
import json

# ------------------  Conditions  ---------------------------

f = urllib2.urlopen('http://api.wunderground.com/api/ff68d6a834ef4090/geolookup/conditions/q/CA/Riverside.json')
json_string = f.read()
parsed_json = json.loads(json_string)

location = parsed_json['location']['city']
# temp_f = parsed_json['current_observation']['temp_f']
# location_full  = parsed_json['current_observation']['display_location']['full']
temp_f = parsed_json['current_observation']['temp_f']
f.close()

# ------------------  Forecasts  ---------------------------

f = urllib2.urlopen('http://api.wunderground.com/api/ff68d6a834ef4090/geolookup/forecast/q/CA/Glendora.json')
json_string = f.read()
parsed_json = json.loads(json_string)

# for day in parsed_json['forecast']['simpleforecast']['forecastday']:
#     print day['date']['weekday'] + ":"
#     print "Conditions: ", day['conditions']
#     print "High: ", day['high']['fahrenheit'] + "F", "Low: ", day['low']['fahrenheit'] + "F"

f.close()

# ------------------  Prints  ---------------------------
# print "Location: %s" % (location_full)
print "Current temperature in %s is: %sF" % (location, temp_f)
print "Forecast:", parsed_json['forecast']['txt_forecast']['forecastday'][0]['fcttext']
print "High:", parsed_json['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit'], "F, Low: ", parsed_json['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit'], "F"


