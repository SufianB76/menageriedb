import mysql.connector as mc

# connect to database
conn = mc.connect(
    host='', # add your own host 
    user='root', 
    password='', # add your own password
)

c = conn.cursor()


def show_database():
    c.execute('SHOW databases')
    fetch = c.fetchall()
    print(fetch)


def create_database():
    c.execute('CREATE DATABASE menagerie')


def drop_database():
    c.execute('DROP DATABASE menagerie')


def use_database():
    c.execute('USE menagerie')


def show_table():
    c.execute('SHOW TABLES')
    table = c.fetchall()
    print(table)


def create_pet():
    c.execute('CREATE TABLE pet \
          (                \
        name VARCHAR(20), \
        owner VARCHAR(20), \
        species VARCHAR(20),\
        sex CHAR(1), \
        birth DATE,\
        death DATE \
   )'
              )


def read_data():
    c.execute('DESCRIBE pet')
    tablepet = c.fetchall()
    for pet in tablepet:
        print(pet)


def insert_into_pet():
    c.execute("INSERT INTO pet VALUES \
    ('Fluffy', 'Harold', 'cat', 'f', '1993-02-04', NULL), \
    ('Claws', 'Gwen', 'cat', 'm', '1994-03-17', NULL), \
    ('Buffy', 'Harold', 'dog', 'f', '1989-05-13', NULL), \
    ('Fang', 'Benny', 'dog', 'm', '1990-08-27', NULL), \
    ('Bowser', 'Diane', 'dog', 'm', '1979-08-31', '1995-07-29'), \
    ('Chirpy', 'Gwen', 'bird', 'f', '1998-09-11', NULL), \
    ('Whistler', 'Gwen', 'bird', NULL, '1997-12-09', NULL), \
    ('Slim', 'Benny', 'snake', 'm', '1996-04-29', NULL), \
    ('Puffball', 'Diane', 'hamster', 'f', '1999-03-30', NULL)"
              )


def read_data_pet():
    c.execute('SELECT * FROM pet')
    tablepet1 = c.fetchall()
    for pet1 in tablepet1:
        print(pet1)


def female_dog_only():
    c.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f' ")
    row = c.fetchall()
    print(row)


def birthdate_name():
    c.execute('SELECT name, birth FROM pet ')
    row1 = c.fetchall()
    for rows in row1:
        print(rows)


def pets_each_owner():
    c.execute('SELECT owner, COUNT(*) FROM pet GROUP BY owner')
    row2 = c.fetchall()
    for rows1 in row2:
        print(rows1)


def pet_name_birth_month():
    c.execute('SELECT name, birth, MONTH(birth) FROM pet')
    row3 = c.fetchall()
    for rows2 in row3:
        print(rows2)


def main():
    use_database()
    insert_into_pet()


if __name__ == '__main__':
    main()

