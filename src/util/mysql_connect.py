import mysql.connector
import sys
import os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from mysql.connector import Error

import bean.load_env
class MysqlConnect:
    def __init__(self):
        active = os.getenv("ACTIVE").strip().lower()
        if active == "dev":
            self.host = os.getenv("DB_HOST")
            self.user = os.getenv("DB_USER")
            self.password = os.getenv("DB_PASSWORD")
            self.database = os.getenv("DB_DATABASE")
            self.port = os.getenv("DB_PORT")
        elif active == "prod":
            self.host = os.getenv("DB_HOST_PRODUCT")
            self.user = os.getenv("DB_USER_PRODUCT")
            self.password = os.getenv("DB_PASSWORD_PRODUCT")
            self.database = os.getenv("DB_DATABASE_PRODUCT")
            self.port = os.getenv("DB_PORT_PRODUCT")
        else:
            print("Môi trường không xác định")
            exit()

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
            )
        except Error as e:
            print(f"Lỗi kết nối")

        return connection
