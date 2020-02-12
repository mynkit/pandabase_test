# pandabase_test

## pandabase

* [pypi](https://pypi.org/project/pandabase/)
* [github](https://github.com/notsambeck/pandabase)

## Required

* pyenv
	* Python 3.6系
	* pipenvがinstall済み
* docker, docker-compose

## Usage

* mysqlサーバを立ち上げる

```sh
make run
```

* `sample_db`データベースの`users`テーブルを確認

```sh
pipenv run check

# 初期状態では
#
#   id  name   age
# 0  1  taro   20
# 1  2  jiro   17
# 2  3  saburo 18
#
# が返ってくる
```

* pandabaseのupsertのテスト

```sh
pipenv run start

# -- before upsert --
#    id    name  age
# 0   1    taro   20
# 1   2    jiro   17
# 2   3  saburo   18
# - source/data1.csv -
#    id    name  age
# 0   2    jiro   17
# 1   3  saburo   18
# 2   4   shiro   28
# 3   6     syo   20
# -- after upsert --
#    id    name  age
# 0   1    taro   20
# 1   2    jiro   17
# 2   3  saburo   18
# 3   4   shiro   28
# 4   6     syo   20
```
