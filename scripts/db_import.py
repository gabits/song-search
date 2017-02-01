import csv
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="123", db="song_search")

with open('songdata.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    cursor = db.cursor()
    for row in spamreader:
        cursor.execute("INSERT INTO songs_songs (artist, song_name, lyrics_link, lyrics) VALUES (%s, %s, %s, %s)", (
            row[0], row[1], row[2], row[3]))
    db.commit()