from login.login_efetuar import Login_efetuar
from login.login_recuperar_senha import Login_recuperar_senha

email =input("digite seu email: ")
senha = input("digite sua senha : ")

#Login_efetuar(email, senha).login_check()

Login_recuperar_senha(email).login_recuperar()