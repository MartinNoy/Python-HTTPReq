import requests 

# Making a PUT request 
r = requests.put('https://httpbin.org/put', data ={'key':'value'}) 

# check status code for response recieved 
# success code - 200 
print(r) 

# print content of request 
print(r.content) 
