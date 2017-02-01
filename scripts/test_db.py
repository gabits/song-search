import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="123", db="song_search")
cursor = db.cursor()


col = 'artist'

cursor.execute("SELECT * FROM songs_songs WHERE {} LIKE '%{}%' ".format(col, 'BB'))
lista = []

for row in cursor.fetchall():
    dicionario = {
        'artist': row[1],
        'song_name': row[2],
        'lyrics': row[3],
        'lyrics_link': row[4],
    }
    lista.append(dicionario)

print(lista)
