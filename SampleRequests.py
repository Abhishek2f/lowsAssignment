#Author     : Abhishek Kumar Dwivedi
#Created On : 19/6/2020
# importing the requests library
import requests

#Post
URL = "http://127.0.0.1:5000/cart"
PARAMS = {
    'name': "itemName2",
    'description': "itemDesc1",
    'price': "itemPrice1",
    'qty': "itemQty1"
}
headers = {'Content-type': 'application/json'}
# sending post request
r = requests.post(url = URL, json=PARAMS, headers=headers)
print(r.content)
#==============================================================================================

#delete
# api-endpoint
URL = "http://127.0.0.1:5000/cart/2004"

# sending delete request 
r = requests.delete(url = URL)
print(r.content)

#=============================================================================================

#PUT
URL = "http://127.0.0.1:5000/cart/5147"
PARAMS = {
    'name': "itemNameNew",
    'description': "itemDescNew",
    'price': "itemPriceNew",
    'qty': "itemQtyNew"
}
headers = {'Content-type': 'application/json'}
# sending put request 
r = requests.put(url = URL, json=PARAMS, headers=headers)
print(r.content)
#=============================================================================================

# Get request
URL = "http://127.0.0.1:5000/cart"

headers = {'Content-type': 'application/json'}
# sending get request and saving the response as response object
r = requests.get(url = URL, headers=headers)
print(r.content)

#===========================================================================================
# Get Specific request
URL = "http://127.0.0.1:5000/cart/5147"

headers = {'Content-type': 'application/json'}
# sending get request and saving the response as response object
r = requests.get(url = URL, headers=headers)
print(r.content)
