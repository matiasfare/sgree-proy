from ZODB import FileStorage, DB
3.import transaction
4.
5. class MiZODB(object):
6. def
init
(self, archivo):
7. self.storage = FileStorage.FileStorage(archivo)
8. self.db = DB(self.storage)
9. self.conexion = self.db.open()
10. self.raiz = self.conexion.root()
11. def close(self):
12. self.conexion.close()
13. self.db.close()
14. self.storage.close()