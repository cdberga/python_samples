class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def diga_ola(self):
        print("Olá, meu nome é %s e meu email é %s" %(self.nome, self.email))

# usuario1 = Usuario(nome="José de Almeida", email="jose.almeida@gmail.com")

# usuario1.diga_ola()
# print(usuario1.nome)
# setattr(usuario1, "idade", 30)
# print("Idade %s anos." % usuario1.idade)
# delattr(usuario1, "idade")