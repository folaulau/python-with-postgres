#!/usr/bin/python
import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        host = '127.0.0.1'
        database = 'iate_api_db'
        username = 'postgres'
        password = 'postgres'

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(database=database, host=host, user=username, password=password)
        print('Connected to the PostgreSQL database.')
        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')

        cur.execute('SELECT id FROM server_activity LIMIT 1')

        # display the PostgreSQL database server version
        result = cur.fetchone()

        print("id:{}".format(result[0]))

        # close the communication with the PostgreSQL
        cur.close()

        print('PostgreSQL execution done!')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

