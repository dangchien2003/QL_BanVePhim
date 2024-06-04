import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from mysql.connector import Error
from src.util.connect.mysql_connect import MysqlConnect

class Excute:
    def getAll(self, query):
        mysql = MysqlConnect()
        connection = mysql.create_connection()
        cursor = connection.cursor()
        result = None
        
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e:
            print(f"Lỗi truy vấn: {e}")
        finally:
            cursor.close()
            connection.close()
        return result

    def getOne(self, query):
        mysql = MysqlConnect()
        connection = mysql.create_connection()
        if connection is None:
            return None

        cursor = connection.cursor(buffered=True)
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchone()
        except Error as e:
            print(f"Lỗi truy vấn: {e}")
        finally:
            cursor.close()
            connection.close()
        return result

    def getMany(self, query, limit):
        mysql = MysqlConnect()
        connection = mysql.create_connection()
        if connection is None:
            return None

        cursor = connection.cursor(buffered=True)
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchmany(size=limit)
        except Error as e:
            print(f"Lỗi truy vấn: {e}")
        finally:
            cursor.close()
            connection.close()
        return result

    def editMany(self, query, data):
        mysql = MysqlConnect()
        connection = mysql.create_connection()
        if connection is None:
            return None

        cursor = connection.cursor()
        rowcount = 0
        try:
            cursor.executemany(query, values)
            rowcount = cursor.rowcount
            if(rowcount == len(data)):
                connection.commit()
            else :
                raise ValueError(f"Lỗi thêm dữ liệu {rowcount}/{len(data)}")
        except (Error, ValueError) as e:
            print(f"Lỗi truy vấn: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
        return rowcount

    def edit(self, query):
        mysql = MysqlConnect()
        connection = mysql.create_connection()
        if connection is None:
            return None

        cursor = connection.cursor()
        rowcount = 0
        try:
            cursor.execute(query)
            rowcount = cursor.rowcount
            connection.commit()
        except (Error, ValueError) as e:
            print(f"Lỗi truy vấn: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
        return rowcount