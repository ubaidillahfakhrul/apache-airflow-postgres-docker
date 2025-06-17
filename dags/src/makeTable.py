from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2

def make_database():
    """
    Make the Postgres database and create the table.
    """

    dbname = 'airflow'
    username = 'airflow'
    password = 'airflow'
    tablename = 'cuaca_table'

    # Note: I didn't make a password.
    # engine    = create_engine('postgresql+psycopg2://%s@localhost/%s'%(username,dbname))

    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@postgres:5432/{dbname}')
    # Check if the database exists, and create it if it does not.
    if not database_exists(engine.url):
           create_database(engine.url)

    # conn = psycopg2.connect(database = dbname, user = username, password = password)
    conn = psycopg2.connect(database=dbname, user=username, password=password, host="postgres", port="5432")

    curr = conn.cursor()

    create_table = """CREATE TABLE IF NOT EXISTS %s
                (
                    city         TEXT, 
                    country      TEXT,
                    latitude     REAL,
                    longitude    REAL,
                    todays_date  DATE,
                    humidity     REAL,
                    pressure     REAL,
                    min_temp     REAL,
                    max_temp     REAL,
                    temp         REAL,
                    weather      TEXT
                )
                """ % tablename

    curr.execute(create_table)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    make_database()