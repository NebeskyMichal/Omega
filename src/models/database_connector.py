import re

import pyodbc
import configparser


class DatabaseConnectionSingleton:
    """Class for database connection using singleton design pattern"""
    __instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnectionSingleton.__instance is None:
            DatabaseConnectionSingleton()
        return DatabaseConnectionSingleton.__instance

    def __init__(self):
        if DatabaseConnectionSingleton.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            DatabaseConnectionSingleton.__instance = self

        try:
            config = configparser.ConfigParser()
            if not config.read('../cfg/db_config.ini'):
                raise ValueError('Configuration file not found')

            if not config.has_section('Database') or not config.has_option('Database',
                                                                           'Server') or not config.has_option(
                    'Database', 'Database') or not config.has_option('Database', 'UID') or not config.has_option(
                    'Database', 'PWD') or not config.has_option('Database', 'Driver'):
                raise ValueError('Invalid configuration file')

            db_cfg = config['Database']

            server = db_cfg.get('Server')
            database = db_cfg.get('Database')
            uid = db_cfg.get('UID')
            pwd = db_cfg.get('PWD')
            driver = db_cfg.get('Driver')

            if not server or not database or not uid or not pwd or not driver:
                raise ValueError('Invalid values in the configuration file')

            self.server = server
            self.database = database
            self.uid = uid
            self.pwd = pwd
            self.driver = driver

            self.connection = pyodbc.connect('DRIVER=' + self.driver +
                                             ';SERVER=' + self.server +
                                             ';DATABASE=' + self.database +
                                             ';UID=' + self.uid +
                                             ';PWD=' + self.pwd)
        except Exception as e:
            print("Can't connect to database:", e)
            exit()

    def query(self, sql_query, transactional=True):
        """Method for executing sql queries, with transactional support

            :param sql_query: sql query
            :param transactional: True/False - decision of transactional use

            :return: Select result or bool if successful or unsuccessful
        """
        cursor = self.connection.cursor()
        sql_query = sql_query[:6].lower() + sql_query[6:]
        if transactional:
            cursor.execute("begin transaction")
            cursor.commit()
        try:
            cursor.execute(sql_query)
            if sql_query.startswith("update") or sql_query.startswith("insert") or sql_query.startswith("delete"):
                cursor.commit()
            if sql_query.startswith("select"):
                result = cursor.fetchall()
            else:
                result = None
            if transactional:
                cursor.execute("commit transaction")
                cursor.commit()
        except pyodbc.Error as e:
            if transactional:
                cursor.execute("rollback transaction")
                cursor.commit()
            print("There was an error trying to execute the query")
            return False
        finally:
            cursor.close()
        return result

    def close_connecton(self):
        self.connection.close()
