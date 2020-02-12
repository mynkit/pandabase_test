import pandas as pd
from sqlalchemy import create_engine
from const import con


def read_users():
    users = pd.read_sql('SELECT * FROM users;', create_engine(con))
    return users
