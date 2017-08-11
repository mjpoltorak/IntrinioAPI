import intrinio
import psycopg2
import pandas as pd

intrinio.client.username = ''
intrinio.client.password = ''

Location = "./NAS.csv"
Location2 = "./NYSE.csv"

df = pd.read_csv(Location)
df2 = pd.read_csv(Location2)
dfticker = df["Symbol"]
df2ticker = df2["Symbol"]
lista = dfticker.append(df2ticker)

password = input("Please Enter the Password for the Postgres Database: ")

connectionSTR = "dbname='postgres' user='postgres' host='dev-datafactory-postgresql.csodrrohkuas.us-east-1.rds.amazonaws.com' password=" + password;

conn = psycopg2.connect(connectionSTR)  # GLobal host
cur = conn.cursor()

count = 0

for i in lista:
    prices = intrinio.prices('%s', i)
    insert = f"INSERT INTO historical VALUES ('{i}', '{prices}');"
    cur.execute(insert)
    conn.commit()