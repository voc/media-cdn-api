from django.db import connection

class Hexhash:
    def all(self):
        cursor = connection.cursor()
        cursor.execute('SELECT f.path, h.btihhex FROM hexhash h JOIN filearr f ON f.id = h.file_id')
        return [str(col[1]) for col in cursor.fetchall()]
