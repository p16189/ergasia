import openaq

firstcity = input('Give first city: ')
secondcity = input('Give second city: ')

api = openaq.OpenAQ()
status, firstcity_weather = api.measurements(city = firstcity)
status, secondcity_weather = api.measurements(city = secondcity)

if (firstcity_weather['results'][0]['value'] > secondcity_weather['results'][0]['value']):
    print ('City', city1_weather['results'][0]['city'], 'has better weather')
elif (firstcity_weather['results'][0]['value'] < secondcity_weather['results'][0]['value']):
    print ('City', city2_weather['results'][0]['city'], 'has better weather')
else:
    print ('Both of cities has the same weather!!')
