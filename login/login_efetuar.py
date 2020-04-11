 

class Login_efetuar:
    """ Classe para efetuar o login no sistema """
   
    def __init__(self, email, senha):
        """ Email e senha vem do formulario do front """
        self.email = email
        self.senha = senha 
         
         

    def login_check(self):
        """ Metodo para checar se o login é valido  """
        json = {"email":"a.pissulin@gmail.com", "senha":"123456", "perfil":"adm"} # Retorno do banco de dados
        
        if(self.email == json["email"] and self.senha == json["senha"]):
            print("Esta logado no minha conta: [ perfil:",json["perfil"],"]") # aqui pode ser retorna um True 
        else:
            print("Email ou senha invalida!") # aqui pode ser retorna um False 
        