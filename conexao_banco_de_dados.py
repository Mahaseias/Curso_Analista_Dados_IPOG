import pandas as pd
import oracledb
import getpass

user = 'ADMIN'
dsn = 'treinamentoinpasa_high'
pw = '14297301tnMS'
wallet_pw = '2410OU2501ja'

config_dir = 'C:/Users/Mahaseias/Documents/Curso Analista de Dados/drive-download-20241023T170727Z-001/Wallet Treinamento Inpasa'
wallet_location = 'C:/Users/Mahaseias/Documents/Curso Analista de Dados/drive-download-20241023T170727Z-001/Wallet Treinamento Inpasa'

connection = oracledb.connect(user=user, password=pw, dsn=dsn,
                            config_dir=config_dir,
                            wallet_location=wallet_location, wallet_password=wallet_pw)

with connection.cursor() as cursor:
    sql = "SELECT * FROM products"
    df = pd.read_sql(sql, con=connection)
    for row in cursor.execute(sql):
        print(row)

connection.close()