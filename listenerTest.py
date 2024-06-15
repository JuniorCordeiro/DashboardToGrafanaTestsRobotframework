import mysql.connector
from datetime import datetime, timedelta
 
ROBOT_LIBRARY_SCOPE = "GLOBAL"
ROBOT_LISTENER_API_VERSION = 3
 
def conectar_banco():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="robot_results",
            port=3306
        )
        cursor = connection.cursor()
        return connection, cursor
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None, None
 
def end_suite(data, result):
    print(f'{data.name} - {data.tests} - {data.metadata} - {data.suites} - {data.doc}')
    print(f'{result.name} - {result.status} - {result.start_time} - {result.end_time} - {result.elapsedtime}')
    insert_data_into_db(result, data)
    return  result, data
 
def insert_data_into_db(result, data):
        connection, cursor = conectar_banco()
        try:
            if connection and cursor:
                create_table_query = '''
                CREATE TABLE IF NOT EXISTS test_results (
                id SERIAL PRIMARY KEY,
                suite_name VARCHAR(255),
                status VARCHAR(255),
                execution_time VARCHAR(255),
                last_execution VARCHAR(255),
                execution_average VARCHAR(255)
                )
            '''
            cursor.execute(create_table_query)
            connection.commit()

            suite_name = data.name
            status = result.status

            start_time = datetime.strptime(result.starttime, '%Y%m%d %H:%M:%S.%f')
            end_time = datetime.strptime(result.endtime, '%Y%m%d %H:%M:%S.%f')
            execution_average = datetime.strptime(result.endtime, '%Y%m%d %H:%M:%S.%f')

            elapsed_time = end_time - start_time
            execution_average = elapsed_time + timedelta(seconds=46)
            execution_time = str(elapsed_time)

            end_time_str = result.endtime
            end_time = datetime.strptime(end_time_str, '%Y%m%d %H:%M:%S.%f')
            last_execution = end_time.strftime('%Y-%m-%d %H:%M:%S')

            insert_query = '''
                INSERT INTO test_results (suite_name, status, execution_time, last_execution, execution_average)
                VALUES (%s, %s, %s, %s, %s)
            '''
            print(f'Inserido no banco')
            
            values = (suite_name, status, execution_time, last_execution, execution_average)
            cursor.execute(insert_query, values)
            connection.commit()
            
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        finally:
            cursor.close()
            connection.close()

