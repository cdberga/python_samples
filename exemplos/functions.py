def print_ola(nome="estranho"): # valor default
    print("Olá, " + nome)

def print_tudo_2_vezes(*args):
    print(len(args))
    for parametro in args:
        print(parametro + "! " + parametro + "!")


def print_info(**kwargs):
    for parametro, valor in kwargs.items():
        print(parametro + " - " + str(valor))

#
print_ola("Priscilla")
print_ola()
#
print_tudo_2_vezes("Olá", "Python", "Zezinho")
#
print_info(nome="Zezinho", idade=35, nacionalidade="Brasileiro")
