import pyodbc

def write_database(table_name, data):
    dbConnection = None
    try:
        dbConnection = pyodbc.connect("Driver={SQL Server};"
                                      "Server=DESKTOP-N6R0GB7;"
                                      "123;"
                                      "UID=sa;"
                                      "Trusted_Connection=yes")
    except Exception:
        print("Ошибка подключения к базе данных")
    dbCursor = dbConnection.cursor()
    try:
        if table_name == "shop" or table_name == "Shops" or table_name == "Cities":
            for record in data:
                dbCursor.execute(f"INSERT INTO [{table_name}] VALUES(?)", record)
        else:
            
            count_table_fields = len(data[0])
            print(count_table_fields)
            query = f"INSERT INTO [{table_name}] VALUES(?{', ?' * (count_table_fields - 1)})"
            dbCursor.executemany(query, data)
    except Exception as error:
        raise(error)
    finally:
        dbConnection.commit()
        dbConnection.close()

        