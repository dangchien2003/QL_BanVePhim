import mysql.connector
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
import bean.load_env
from mysql.connector import Error

class MysqlConnect :
    def __init__(self) :
        self.host=os.getenv("DB_HOST")
        self.user=os.getenv("DB_USER")
        self.password=os.getenv("DB_PASSWORD")
        self.database=os.getenv("DB_DATABASE")
        self.port=os.getenv("DB_PORT")

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
        except Error as e:
            print(f"Lỗi kết nối")

        return connection