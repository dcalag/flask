import psycopg2
import sys

def query_all_users():
    db_con = None
    users = []

    try:
        #Create a database session
        db_con = psycopg2.connect(host="localhost", database='test', \
            user='postgres', password='masterke')

        #Create a client cursor to execute commands

        cursor = db_con.cursor()
        cursor.execute("SELECT * FROM users")

        rows = cursor.fetchall()
        for row in rows:
            users.append(
                {
                    "id": row[0],
                    "username": row[1]
                }
            )
        return (users)
    except psycopg2.DatabaseError as e:
        return ('Error %s' % e)

    finally:
        if db_con:
            db_con.close()
