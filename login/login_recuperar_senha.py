
class Login_recuperar_senha:
    """Classe para fazer a recuperacao da senha """
    
    def __init__(self, email):
        self.email = email
        
        
    def login_recuperar(self):
        """Valida o email e envia uma senha provisoria por email"""
        
        json = {"email":"a.pissulin@gmail.com"} # Retorno do banco de dados
        
        if(self.email == json["email"]):
            print("Senha provisoria enviado no email cadastrado!")
        else:
            print("Email invalido!")