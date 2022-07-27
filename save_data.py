from scraper import load_names
from scraper import load_items
import psycopg2
from psycopg2 import Error

def update_database():
    print("Connecting to PostgreSQL database")
    try:

        connection = psycopg2.connect(host="localhost",database="flats",user="admin",password="admin",port="5432")
        cursor = connection.cursor()


        names, url_images = load_items()

        ids=list(range(0,500))
        print(ids)
        records = merge(names,url_images,ids)
        print((records))
        sql_update_query = """ 
            Update main 
            set name = %s, 
            image = %s 
            where id = %s"""
        sql_insert_query = """
            Insert into main (id,name,image)
            values(%s,%s,%s)
        """

        cursor.executemany(sql_update_query, records)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into table")

        #print("Table After updating record ")
        #sql_select_query = """select * from main where id = %s"""
        #cursor.execute(sql_select_query, (0,500))
        #record = cursor.fetchone()
        #print(record)

    except(Exception,Error) as error:
        print("Failed to insert record into table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def merge(list1, list2,list3):
    merged_list = [(list1[i], list2[i],list3[i]) for i in range(0, len(list1))]
    return merged_list

