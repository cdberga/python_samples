from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nome, email, chave_adm):
        Usuario.__init__(self, nome, email)
        self.chave_adm = chave_adm

    def poder_admin(self):
        print("Eu tenho o poder! Minha chave é %s" %self.chave_adm)

usuario_adm = Administrador(email="admin@sistema.com.br", chave_adm="asiodnas#%$$#%$#%-+=sdfsdf", nome="Admin")
usuario_adm.diga_ola()
usuario_adm.poder_admin()