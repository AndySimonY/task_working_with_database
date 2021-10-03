import psycopg2

def connect(credentials=None):
    if credentials == None:
            pass
    else:
            database = credentials['database']
            user = credentials['user']
            password = credentials['password']
            host = credentials['host']
            port = credentials['port']

    try:
            conn = psycopg2.connect(
                database=database, 
                user=user, 
                password=password, 
                host=host, 
                port=port) 
            print("Database connected!")
            return conn
    except(Exception, ConnectionError) as error:
            return error
