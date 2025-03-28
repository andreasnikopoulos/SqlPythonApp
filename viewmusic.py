from connection import get_connection

def view_music():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "DELECT * FROM music"
    cursor.execute(sql)
    music = cursor.fetchall()

    if music:
        print("Music playlist")
        for song in music:
            print(f"Id: {song[0]}, genre: {song[1]}, title: {song[2]}, album: {song[3]}, year: {[4]}, artist: {[5]}")
    else:
        print("No song available")  
    cursor.close()
    connection.close()          