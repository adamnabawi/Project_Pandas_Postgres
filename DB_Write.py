# Library
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text

# Define the database connection parameters
db_params = {
    'host': 'localhost',
    'database': 'trial',
    'user': 'adam',
    'password': 'password'
}

# Create a connection to the PostgreSQL server
conn = psycopg2.connect(
    host=db_params['host'],
    database=db_params['database'],
    user=db_params['user'],
    password=db_params['password']
)

# Create a cursor object
cur = conn.cursor()

# Set automatic commit to be true, so that each action is committed without having to call conn.committ() after each command
conn.set_session(autocommit=True)

# Commit the changes and close the connection to the default database
conn.commit()
cur.close()
conn.close()

# Connect to the 'soccer' database
db_params['database'] = 'trial'
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')

# Import File CSV   
df = pd.read_csv('Costumer_Master.csv', sep='|')

# Normalize Data
df['Count']=1
df.rename(columns=lambda x: x.strip(), inplace= True)
cols = df.select_dtypes(object).columns
df[cols] = df[cols].apply(lambda x: x.str.strip())

# Loop through the CSV files and import them into PostgreSQL
df.to_sql('tabel', engine, if_exists='replace', index=False)
print(df)