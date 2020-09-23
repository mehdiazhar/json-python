import json
import requests
import cgitb

cgitb.enable()


response = (requests.get("http://www.bom.gov.au/fwo/IDN60701/IDN60701.94592.json")).text #fetching json data as a string
responseDict = json.loads(response) #converting string to dictionary in order to manipulate the data

pressure = []
temperature = []

for i in responseDict['observations']['data']: #accessing the value "press" where it resides in the json data
    pressure.append(i['press'])              #appending values of pressure to list

for j in responseDict['observations']['data']: #accessing the value of "air_temp" where it resides in the json data
    temperature.append(j['air_temp'])           #appending values of air_temp to list

print("Content-type: text/html\n")
print("<HTML>\n")

print("Minimum pressure is: ", min(pressure))
print("Maximum pressure is: ", max(pressure))
print("Average pressure is: ", sum(pressure)/len(pressure))

print("Minimum temperature is: ", min(temperature))
print("Maximum temperature is: ",  max(temperature))
print("Average temperature is: ", sum(temperature)/len(temperature))

print("</HTML>")

#
# # print(type(r))
#
# for rData in r:
#     print(type(rData))
#
# print(type(rData))
# # for data in responseDict["observations"]:
# #     for pressure in data["weather"]:
# #         print(pressure.get("weather"))
