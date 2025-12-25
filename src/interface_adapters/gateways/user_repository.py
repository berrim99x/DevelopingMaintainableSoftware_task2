import mysql.connector
from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface
from src.entities.user import User


class MySQLUserRepository(UserRepositoryInterface):
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def _connect(self):
        """ Establish a connection to MySQL database """
        try:
            # محاولة الاتصال بـ MySQL باستخدام إعدادات جديدة
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port  # استخدام المنفذ الذي يتم تحديده
            )
            print("Successfully connected to MySQL")
            return connection
        except mysql.connector.Error as err:
            # التعامل مع الخطأ في حال فشل الاتصال
            print(f"Error: {err}")
            raise Exception("Could not connect to MySQL server. Please check the connection details and MySQL server.")

    def save(self, user: User) -> None:
        """ Save the user in MySQL database """
        connection = self._connect()  # الاتصال بـ MySQL
        cursor = connection.cursor()
        query = "INSERT INTO users (first_name, last_name) VALUES (%s, %s)"
        values = (user.first_name, user.last_name)

        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        print(f"User {user.first_name} {user.last_name} saved to MySQL.")
