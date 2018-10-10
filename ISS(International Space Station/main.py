import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.content)
print('------------------------------------------------------------')

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of chicago .
parameters = {'lat':37.71, 'lon':-124}
# Make a get request with the parameters.
response = requests.get('http://api.open-notify.org/iss-pass.json', params = parameters)

#This gets the same data as the command above
#response = requests.get('http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74')

#get the response data as a python object
data = response.json()
print(type(data))
print(data)
print('---------------------------------------------')

#Print the content of the response (the data the server returned)
print(response.status_code)
print(response.content)
print('------------------------')

# Headers is a dictionary
print(response.headers)

# Get the content-type from the dictionary.
print(response.headers["content-type"])
print('---------------')

#get the response from API endpoint
response = requests.get('http://api.open-notify.org/astros.json')
astros = response.json()

print(astros)
print(astros['number'])
