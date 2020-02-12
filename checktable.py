import pandas as pd
from sqlalchemy import create_engine

if __name__ == '__main__':
    con = create_engine(
        'mysql+mysqlconnector://root:password@localhost/sample_db')
    users = pd.read_sql('SELECT * FROM users;', con)
    print(users.head())
