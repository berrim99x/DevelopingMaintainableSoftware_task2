import mysql.connector
from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface
from src.entities.user_dto import UserDTO


class MySQLUserRepository(UserRepositoryInterface):
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def _connect(self):
        """ إنشاء اتصال بقاعدة بيانات MySQL """
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

    def save(self, user_dto: UserDTO) -> None:
        """ حفظ بيانات المستخدم في قاعدة البيانات """
        connection = self._connect()
        cursor = connection.cursor()
        query = "INSERT INTO users (first_name, last_name) VALUES (%s, %s)"
        values = (user_dto.first_name, user_dto.last_name)

        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        print(f"User {user_dto.first_name} {user_dto.last_name} saved to MySQL.")
