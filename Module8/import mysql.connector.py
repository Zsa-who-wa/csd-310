import mysql.connector

# MySQL database configuration
config = {
    'user': 'movies_user',
    'password': 'popcorn',
    'host': '127.0.0.1',
    'database': 'movies',
    'raise_on_warnings': True,
    'auth_plugin': 'mysql_native_password'
}

def show_films(cursor, title):
    query = '''
    SELECT film.film_name AS Name, film.film_director AS Director, genre.genre_name AS Genre, studio.studio_name AS Studio
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    '''
    cursor.execute(query)
    films = cursor.fetchall()
    for film in films:
        name = film[0]
        director = film[1]
        genre = film[2]
        studio = film[3]
        print("Film Details:")
        print("------------")
        print("Name:    {}".format(name))
        print("Director:{}".format(director))
        print("Genre:   {}".format(genre))
        print("Studio:  {}".format(studio))
        print()

        # Connect to the MySQL database
        db = mysql.connector.connect(**config)

    try:
        cursor = db.cursor()
        display_films(cursor)

finally:
    # Close the database connection
    db.close()