import requests

#response = requests.get('http://api.open-notify.org/iss-now.json')


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {'lat':40.71, 'lon':-74}
# Make a get request with the parameters.
#response = requests.get('http://api.open-notify.org/iss-pass.json', params = parameters)

# This gets the same data as the command above
response = requests.get('http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74')



# Print the content of the response (the data the server returned)
print(response.status_code)
print(response.content)
