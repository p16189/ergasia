import urllib2
import json

firstcity =raw_input('Give first city: ')
secondcity =raw_input('Give second city: ')

firstcitydata =urllib2.urlopen('https://api.teleport.org/api/urban_areas/slug:' + firstcity + '/scores/').read()
secondcitydata =urllib2.urlopen('https://api.teleport.org/api/urban_areas/slug:' + secondcity  + '/scores/').read()


firstcitydata =json.loads(firstcitydata)
secondcitydata =json.loads(secondcitydata)

if (firstcitydata['teleport_city_score'] == secondcitydata['teleport_city_score']):
	print " Both cities have the same score "

if (firstcitydata['teleport_city_score'] > secondcitydata['teleport_city_score']):
	print " City " + firstcity + " has higher score "

if (firstcitydata['teleport_city_score'] < secondcitydata['teleport_city_score']):
	print " City " + secondcity  + " has higher score "
