import pyodbc
import configparser


class DatabaseConnectionSingleton:
    """Třída reprezentující připojení do DB pomocí návrhového vzoru Singleton """
    __instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnectionSingleton.__instance is None:
            DatabaseConnectionSingleton()
        return DatabaseConnectionSingleton.__instance

    def __init__(self):
        if DatabaseConnectionSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseConnectionSingleton.__instance = self
        try:
            config = configparser.ConfigParser()
            config.read('../cfg/db_config.ini')
            config.sections()
            db_cfg = config['Database']

            self.server = db_cfg['Server']
            self.database = db_cfg['Database']
            self.uid = db_cfg['UID']
            self.pwd = db_cfg['PWD']
            self.driver = db_cfg['Driver']
            self.connection = pyodbc.connect('DRIVER=' + self.driver +
                                             ';SERVER=' + self.server +
                                             ';DATABASE=' + self.database +
                                             ';UID=' + self.uid +
                                             ';PWD=' + self.pwd)
        except Exception:
            print("Cant connect to database")

    def query(self, sql_query, transactional=False):
        """Metoda pro spouštění příkazů SQL, rozhoduje se o použití transakcí

            :param sql_query: SQL příkaz
            :param transactional: True/False - rozhoduje o použití transakce

            :return: Výsledek ze Selectu nebo False pokud se nepovede
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
