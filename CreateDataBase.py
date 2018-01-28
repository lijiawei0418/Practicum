import psycopg2
# from config import Config

CONNECT_FIG = "dbname='MARCSAMPLE' user='postgres' password='12345678'"

def CreateTable():
    """
    create table in the PostgreSQL database

    """
    commands = (
        """
        CREATE TABLE BOOKS (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
     )
    conn = None
    try:
        # read the connection parameters
        # params = Config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname='MARCSAMPLE' user='postgres' password='12345678'")
        cur = conn.cursor()
        # create table one by one
        # for command in commands:
        #     cur.execute(command)

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')



        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


    finally:
        if conn is not None:
            conn.close()

def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None
    try:
        # read database configuration
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname='MARCSAMPLE' user='postgres' password='12345678'")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, vendor_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        conn = psycopg2.connect("dbname='MARCSAMPLE' user='postgres' password='12345678'")
        cur = conn.cursor()
        cur.execute("SELECT vendor_name FROM vendors")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    # CreateTable()
    # insert one vendor
    # insert_vendor("3M Co.")
    # insert multiple vendors
    # insert_vendor_list([
    #     ('AKM Semiconductor Inc.',),
    #     ('Asahi Glass Co Ltd.',),
    #     ('Daikin Industries Ltd.',),
    #     ('Dynacast International Inc.',),
    #     ('Foster Electric Co. Ltd.',),
    #     ('Murata Manufacturing Co. Ltd.',)
    # ])

    get_vendors()