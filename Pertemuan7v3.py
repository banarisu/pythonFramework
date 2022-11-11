#Buat bikin database sqlite doang
'''import sqlite3

con = sqlite3.connect('sesi.sql')
cursor = con.cursor()
cursor.execute(
    CREATE TABLE IF NOT EXISTS "users"(
    "id" INTEGER NOT NULL,
    "email" VARCHAR(80),
    "username" VARCHAR(100),
    "password_hash" VARCHAR,
    PRIMARY KEY("id"),
    UNIQUE("email")
    );
)
con.commit()
cursor.close()
con.close()'''


