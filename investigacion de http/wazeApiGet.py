# importing the requests library 
import requests 

# api-endpoint 
URL = "https://waze.com/ul"

# Params given here 
# Spaces need to be replaced with %20
stringBusqueda = "?q="
nivelDeAmpliacion = "ul?z=8"
location = "Amancio%20Alcorta%20310"


# defining a params dict for the parameters to be sent to the API 
PARAMS = {stringBusqueda: location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS)
print(r)

# extracting data in json format