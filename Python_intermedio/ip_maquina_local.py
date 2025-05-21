#Debemos instalar: pip install requests
import requests
import public_ip as ip

print(f'----------FORMA_1----------------')
requests = requests.get("https://ident.me")
ip_publica = requests.text
print(ip_publica)


print(f'----------FORMA_1----------------')
#Necesario instalar: pip install public-ip
ip_publica2 = ip.get()
print(ip_publica2)