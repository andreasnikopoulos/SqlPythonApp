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

insert_music("Metal", "The Stage", "The Stage", 2017, "Avenged Sevenfold")
insert_music("Metal", "Bat Country", "City of Evil", 2005, "Avenged Sevenfold")        