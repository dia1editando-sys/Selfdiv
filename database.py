# modulo feito por hake atos

from pymongo import MongoClient
from typing import Optional
import time

class Manager(object):

 def __init__(self, Mongo):
 # self.("link", "id do servidor")
 # resposta -> End point da conexão
 # resposta -> False = Falha
  self.mongo = Mongo 
  try:
    CONNECTION_STRING = Mongo
    client = MongoClient(CONNECTION_STRING,tls=True, tlsAllowInvalidCertificates=True)
    self.db = client
  except Exception as e:
    return False

 def reconnect(self): 
     
      pass
 def store_user_data(self, cluster, local, id, json: Optional[bool] = None, log: Optional[bool] = False):
 # self.store_user_data('pontos', '388s363351325016075')
 # resposta -> Valor
 # resposta -> None = Não existe

  try:
   query  = list(self.db[cluster][local].find({"_id": str(id)}))
   if len(query) > 0:

        return True
   else:

        return False
  except:
      return False
 
 def insert_user_data(self, cluster, local, id, updata: Optional[bool] = False):
 # self.insert_user_data('pontos', '388s363351325016075', 0) 
 # resposta -> True = Criado
 # resposta -> False = Não criado

  try:
      collection_name = self.db[cluster][local];
      collection_name.insert_one({"_id" : str(id)});
      return True
  except Exception as e:
      if "duplicate key error collection" in str(e) and updata:
        return False
      return None



 def delete_user_data(self, cluster, local, id):
 # self.delete_user_data('pontos', '388s363351325016075')
 # resposta -> True = Deletado
 # resposta -> False = Não deletado

  try:
      self.db[cluster][local].delete_one({"_id" : str(id)})
      return True
  except:
          return False

# modulo feito por hake atos


