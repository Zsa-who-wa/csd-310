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

# Connect to the MySQL database
db = mysql.connector.connect(**config)

print("-- DISPLAYING Studio RECORDS --")
cursor = db.cursor()
cursor.execute("SELECT studio_id, studio_name FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

print("-- DISPLAYING Genre RECORDS --")
cursor = db.cursor()
cursor.execute("SELECT genre_id, genre_name FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

print("-- DISPLAYING Short Film RECORDS --")
cursor = db.cursor()
cursor.execute("SELECT film_name 'Film Name:',film_runtime 'Runtime:' FROM film WHERE film_runtime < 120")
films = cursor.fetchall()
for film in films:
    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

print("-- DISPLAYING Director RECORDS in Order --")
cursor = db.cursor()
cursor.execute("SELECT film_name 'Film Name:',film_director 'Director:' FROM film ORDER BY film_director;")
films = cursor.fetchall()
for film in films:
    print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

# Close the database connection
db.close()



