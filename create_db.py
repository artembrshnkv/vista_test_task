from pymysql import connect
from config_reader import config


try:
    with connect(
        host=config.db_host,
        user=config.db_user,
        password=config.db_password,
    ) as con:
        with con.cursor() as cur:
            cur.execute(f"CREATE DATABASE {config.db_name}")
except Exception as e:
    print(e)
