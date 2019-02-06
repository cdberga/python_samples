from pymongo import MongoClient
import json

client = MongoClient('mongodb://dev.egerdau.users.mongodb.gerdau.digital:27017', username='usersLogin', password='2022gerdau', authSource='users')
banco = client.users
usuarios = banco.users

#obj = usuarios.find_one({"email":"pedro.paulo@sciensa.com"})
obj = usuarios.find("{$and: [{\"sendOrdersToEmail\": true, \"status\": { $ne: \"disabled\" },$or: [{\"roles.adminCustomers.0\": {$exists: true}, \"roles.ordersViewCustomers.0\": {$exists: true}}]}],}")

print(obj)
#print(json.JSONEncoder().encode(str(obj)))

