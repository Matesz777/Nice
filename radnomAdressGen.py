import random_address

def multiplyAddres():
   for i in range(10):
       addres = random_address.real_random_address_by_state('CA')
       selectedkeys = ['address1', 'city', 'postalCode']
       formatedAdress = " ,".join(str(addres[key]) for key in selectedkeys if key in addres)
       print(formatedAdress)

result = multiplyAddres()
print(result)


