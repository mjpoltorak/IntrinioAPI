import intrinio
import psycopg2
import pandas as pd

intrinio.client.username = '165e99c4bad271d20298f0661636fbcb'
intrinio.client.password = '1027db3a95605f877d17a2ae87807bbc'

Location = "./NAS.csv"
Location2 = "./NYSE.csv"

df = pd.read_csv(Location)
df2 = pd.read_csv(Location2)
dfticker = df["Symbol"]
df2ticker = df2["Symbol"]
lista = dfticker.append(df2ticker)

conn = psycopg2.connect("dbname='postgres' user='postgres' host='dev-datafactory-postgresql.csodrrohkuas.us-east-1.rds.amazonaws.com' password='sbterminal'") #GLobal host
cur = conn.cursor()

count = 0

for i in lista:
    prices = intrinio.prices('%s', i)
    insert = f"INSERT INTO historical VALUES ('{i}', '{prices}');"
    cur.execute(insert)
    conn.commit()