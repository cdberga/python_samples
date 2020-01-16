import pprint

class MyDictionaire(dict):
    def __init__(self, dict):
        self.dict = dict

    def has_key(self, key):
        print(str(key in self.dict.keys()) + " for the existence of key " + key)

    def has_value(self, val):
        print(str(val in self.dict.values()) + " for the existence of value " + val)

    def has_key(self, key):
        print(str(self.dict.get(key, 0)) + ' is the value for key ' + key)

    def ins_if_not_in(self, key, value):
        self.dict.setdefault(key, value)
        pprint.pprint(self.dict)

your_dict = MyDictionaire({"email":"admin@sistema.com.br", "chave_adm":"asiodnas#%$$#%$#%-+=sdfsdf", "nome":"Admin"})
your_dict.has_key("email")
your_dict.has_value("Admin")
your_dict.has_key("chave_adm")
your_dict.ins_if_not_in("minha_chave", "meu_valor")
