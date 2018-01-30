import psycopg2
# from config import Config

CONNECT_FIG = "dbname='MARCDATA' user='postgres' password='12345678'"
book_list = [dict([('ISBN', '0520074777'), ('Title_Prop', "America at century's end"), ('Copy_Date', '1991'), ('Topical_LCSH_Term', 'Social problems')])]

def CreateTable():
    """
    create table in the PostgreSQL database

    """
    commands = (
        """
        CREATE TABLE BOOKS (
            ISBN VARCHAR(255)PRIMARY KEY,
            Creator_Personal_Name VARCHAR(255),
            Creator_Corporate_Name VARCHAR(255),
            Title_Prop VARCHAR(255),
            Edition_Statement VARCHAR(255),
            Publisher VARCHAR(255),
            Copy_Date VARCHAR(255),
            Series_Title VARCHAR(255),
            Summarization_Of_Content VARCHAR(255),
            Topical_LCSH_Term VARCHAR(255)
        )
        """,
     )
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(CONNECT_FIG)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def InsertBookInfo(self, book_list):
    """
    Insert multiple book information into the table

    >>> InsertBookInfo(InsertBookInfo, book_list)
    """

    try:
        # read database configuration
        # connect to the PostgreSQL database
        conn = psycopg2.connect(CONNECT_FIG)
        # create a new cursor
        cur = conn.cursor()

        # create INSERT statment
        for i in range(len(book_list)):
            book = book_list[i]
            col = ','.join(book.keys())
            marks = ','.join('%s' for i in book.keys())
            val = [v for v in book.values()]
            insert = 'INSERT INTO BOOKS(%s) VALUES(%s)'%(col, marks)
            # execute INSERT statment
            cur.execute(insert, val)

        conn.commit()
        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




def CheckTable():
    try:
        conn = psycopg2.connect(CONNECT_FIG)
        cur = conn.cursor()

        # create INSERT statment
        cur.execute('SELECT * FROM Books')
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


#CreateTable()

# InsertBookInfo(InsertBookInfo, book_list)

# CheckTable()