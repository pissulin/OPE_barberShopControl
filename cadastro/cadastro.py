from cadastro.cadastroDB import salvar
 
class Cadastro:
      
    def __init__(self,*args):
        pass
    
    def cadastro_insert(self, *args):
        salvar(args)
        print(args)
    
    
    def cadastro_update(self):
        pass
    
    
    def cadastro_delete(self):
        pass
    
    
    def cadastro_read(self):
        pass