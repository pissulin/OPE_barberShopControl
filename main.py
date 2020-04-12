from login.login_efetuar import Login_efetuar
from login.login_recuperar_senha import Login_recuperar_senha
from cadastro.cadastro_usuario import Cadastro_usuario
from cadastroDB import clientes

#email =input("digite seu email: ")
#senha = input("digite sua senha : ")

#Login_efetuar(email, senha).login_check()

#Login_recuperar_senha(email).login_recuperar()
print(clientes)

Cadastro_usuario().cadastro_insert("aaaa", "aaaas@gmil.com.br", "luca20")

print(clientes)