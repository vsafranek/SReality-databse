import psycopg2

def load_from_sql():
    #establishing the connection
    conn = psycopg2.connect(
       database="flats", user='admin', password='admin', host='127.0.0.1', port= '5432'
    )

    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Retrieving data
    cursor.execute('''SELECT * from main''')


    #Fetching 1st row from the table
    result = cursor.fetchall();

    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()

    return result
