# import psycopg2

# # Define connection parameters
# dbname = 'demo'      # Replace with your database name
# user = 'postgres'      # Replace with your username
# password = 'root'  # Replace with your password
# host = 'localhost'          # Change if your database is hosted remotely
# port = '5432'               # Default PostgreSQL port

# # Establish connection to PostgreSQL
# try:
#     conn = psycopg2.connect(
#         dbname=dbname,
#         user=user,
#         password=password,
#         host=host,
#         port=port
#     )
#     print("Connected to the database successfully!")
# except Exception as e:
#     print("Error while connecting to PostgreSQL:", e)

# db.py
import psycopg2
from urllib.parse import urlparse
import os

# def get_db_connection():
#     # Connection parameters
#     dbname = 'demo'      # Replace with your database name
#     user = 'postgres'      # Replace with your username
#     password = 'root'  # Replace with your password
#     host = 'localhost'          # Change if your database is hosted remotely
#     port = '5432'  # Default PostgreSQL port

#     try:
#         # Establish the connection
#         conn = psycopg2.connect(
#             dbname=dbname,
#             user=user,
#             password=password,
#             host=host,
#             port=port
#         )
#         # Return connection object
#         # print('success')
#         return conn
#     except Exception as e:
#         print("Error while connecting to PostgreSQL:", e)
#         return None
    
def get_db_connection():
    # db_url = os.getenv("postgresql://postgres:DdrfpaFFFhzcgEznxfDVZSJiJlVSUtQa@junction.proxy.rlwy.net:15474/railway")
    result = urlparse("postgresql://postgres:sVwIPatXTZRoEGcMeMoFFpBGRIGxdLId@autorack.proxy.rlwy.net:33550/railway")
    conn = psycopg2.connect(
        dbname=result.path[1:],
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port
    )
    return conn
get_db_connection()

# conn=get_db_connection()
# cur=conn.cursor()
# cur.execute("select * from students;")
# rows=cur.fetchall()
# for i in rows:
#     print(i)