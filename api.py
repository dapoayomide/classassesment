import requests
url = 'https:// api-customer-038j.onrender.com/customer'

response = requests.get(url)
print(response.json())