import psycopg2 as bd

conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    # conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Uziel', 'Ocaño', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)
    
    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Bernabe', 'Ocaño','brboca@mail.com', 1)
    conexion.commit()
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo rollback: {e}')
finally:
    conexion.close()