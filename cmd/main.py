import subprocess


import requests
from requests.auth import HTTPBasicAuth

# listar_ip = 'ipconfig'

# resultado = subprocess.run(listar_ip, shell=True, capture_output=True, text=True)

# if(resultado == "Getaway Padrão"):
#     resultado = 'O ip e'

# print(resultado.stdout)
# Substitua pelo IP do seu roteador
router_ip = 'http://192.168.1.254'

# Credenciais do roteador (substitua pelas suas)
username = 'TP-link_9DD1'
password = '05223506'

# Tenta acessar a página de configuração do roteador
response = requests.get(router_ip, auth=HTTPBasicAuth(username, password))

# Verifica se o login foi bem-sucedido
if response.status_code == 200:
    print("Login bem-sucedido")
    # Adicione aqui o código para navegar pela interface e verificar o status do WPS
    # Isso dependerá da estrutura da interface web do roteador
else:
    print("Falha no login. Verifique suas credenciais.")

