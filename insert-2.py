from connection import get_connection

def insert_music(genre,	title, album, year, artist):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO music (genre, title,	album, year, artist) VALUES (%s, %s, %s, %s, %s)"
    values = (genre, title,	album, year, artist)
    cursor.execute(sql, values)
    connection.commit()
    print("The song has been added")
    cursor.close()
    connection.close()

genre = input("Insert value: ")
title = input("Insert value: ")
album = input("Insert value: ") 
year = int(input("Insert value: "))
artist = input("Insert value: ")

insert_music(genre, title,	album, year, artist)