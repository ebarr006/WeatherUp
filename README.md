# WeatherUp!
WeatherUp! is a weather text alert system that sends scheduled user-specified weather data via text message. It uses the Wunderground API (https://www.wunderground.com/weather/api/), a python script and a bash script. If you'd like to implement, make sure to register with Wunderground to recieve a unique API Key.

### Overview
The python script requests various weather data using an API call. You can specify the types of data you want by using different keywords and locations in the URL. The call returns all data for the keywords you specified into JSON. The python script can then parse the returned JSON for whatever weather information you are looking for.

The bash script redirects the output of the python script to a textfile that can be sent to a mobile phone or email address via the command-line tool Mail.
