import requests

def main():
    try:
        # User Input section
        city = input('Enter your City Name :')
        # data retrieved from API and URL
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&' \
              'appid=f4db5e7626d74a981b1232316fce4caa&units=metric'.format(city)
        # Retrieves data from URL
        res = requests.get(url)
        # takes json file and displays using user input
        data = res.json()
        # minimal results for user
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        # prints results for user
        print('Temperature :{} degrees celsius'.format(temp))
        print('Wind Speed : {} m/s'.format(wind_speed))
        print('Latitude : {}'.format(latitude))
        print('Longitude : {}'.format(longitude))
        print('Description : {}'.format(description))
        main()
    except:
        print('Sorry this is not a city name')
        main()


main()