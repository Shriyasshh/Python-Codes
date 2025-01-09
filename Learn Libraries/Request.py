import requests


#Get request(reading a post)

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)  # HTTP Status Code
print(response.text)         # Response Body
print(response.json())       # Parse JSON response (if applicable)


'''
Status_Codes:
200: OK (Request was successful)
201: Created (Resource successfully created)
204: No Content (Request succeeded, but no content to return)
400: Bad Request (Client sent an invalid request)
401: Unauthorized (Authentication required or failed)
403: Forbidden (Client doesn't have permission)
404: Not Found (Resource not found)
500: Internal Server Error (Server encountered an error)
'''

#Post request(creating a new post)

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code)
print(response.json())


#Put request(updating a post)

data = {'title': 'updated title'}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data)
print(response.status_code)
print(response.json())



#Delete request(deleting a post)

response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)
print(response.json())



#Common Attributes of a Response Object

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)   # HTTP status code (e.g., 200, 404)
print(response.headers)        # Response headers
print(response.content)       # Response body (bytes)
print(response.text)          # Response body (string)
print(response.json())        # Parsed JSON (if applicable)


#Sending Custom Headers

# headers = {'Authorization': 'Bearer your_token'}
# response = requests.get('https://api.example.com/resource', headers=headers)
# print(response.status_code)

#Handling Timeouts

response = requests.get('https://jsonplaceholder.typicode.com/posts/1', timeout=15)
print(response.status_code)


#timeout=5:
# Sets a timeout for the request.
# If the server does not respond within 5 seconds, a requests.exceptions.Timeout error is raised.
# Useful to prevent your program from hanging indefinitely if the server is unresponsive.

#Downloading Large Files

url = 'https://example.com/sample.jpg'
response = requests.get(url)
with open('sample.jpg', 'wb') as file:
    file.write(response.content)
