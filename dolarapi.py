import requests
url = 'https://api.bluelytics.com.ar/v2/latest'
response = requests.get(url)
#class dolar: falta definir la api como objeto
if response.status_code == 200:
    # Obtén los datos JSON de la respuesta
        data = response.json()
        #print("Por favor ingrese el tipo de valor de dolar que desea obtener")
        #print ("1 - valor dolar oficial, 2 - valor del dolar blue")
        #value = (input())
    
#if value == '1':
#        print("Valor del dolar oficial:", data['oficial'])
#elif value == '2':
#        print("Valor del dolar blue:", data['blue'])
#else: print(f"Error: {response.status_code}")