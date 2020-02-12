import pandas as pd
import pandabase
from const import con
from utils import read_users


def read_data1():
    return pd.read_csv('source/data1.csv')


def data1_to_sql(data1, how):
    '''
    Args:
        data1: usersテーブルに追加したいデータのデータフレーム
        how : {'create_only', 'upsert', 'append'}
            - create_only:
                If table exists, raise an error and stop.
            - append:
                If table exists, append data. Raise if index overlaps
                Create table if does not exist.
            - upsert:
                create table if needed
                if record exists: update (possibly replacing values with NULL)
                else: insert
    '''
    data1 = data1.set_index('id')
    pandabase.to_sql(data1, table_name='users', con=con, how=how)


if __name__ == '__main__':
    print('-- before upsert --')
    users = read_users()
    print(users)
    data1 = read_data1()
    print('- source/data1.csv -')
    print(data1)
    data1_to_sql(data1, how='upsert')
    print('-- after upsert --')
    users = read_users()
    print(users)
