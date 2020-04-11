
class Login_recuperar_senha:
    
    def __init__(self, email):
        self.email = email
        
    def login_recuperar(self):
        json = {"email":"a.pissulin@gmail.com"} # Retorno do banco de dados
        
        if(self.email == json["email"]):
            print("Senha provisoria enviado no email cadastrado!")
        else:
            print("Email inválido!")