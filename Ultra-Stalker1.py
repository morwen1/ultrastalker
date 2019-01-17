import requests
import urllib
import json


#autenticacion 
id_client = "288689141885-667r4c17i1f9ru9ro5jeesbpf74pb828.apps.googleusercontent.com"
clave = "3RvjxMj2Nbx9fQ3qBVT6XRHL"

def datos ():
	nombre = input('nombre >> ')
	apellido = input('apellido >> ')
	cedula = input('cedula >> ')
	return {'nombre':nombre,'apellido':apellido, 'cedula':cedula}


#datos=datos()

query1="site:facebook.com search:    "
query2="site:instagram.com search:   "
query3="site:linkedin.con search:    "
query4="site:twitter.com search:     "
quer ='site:exploit-db.com intitle:"linux" "vulnerabitlity"'




dir_api="https://www.googleapis.com/customsearch/v1?key="
url = dir_api + clave + "&cx=" + id_client + "&q=" + quer
print(url)
resultado = requests.get(url)
print(resultado)
print(resultado.json)
