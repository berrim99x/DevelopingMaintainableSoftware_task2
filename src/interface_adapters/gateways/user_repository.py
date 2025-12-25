from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface
from src.entities.user_dto import UserDTO
import mysql.connector


class MySQLUserRepository(UserRepositoryInterface):
    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def _connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def save(self, user_dto: UserDTO) -> None:
        connection = self._connect()
        cursor = connection.cursor()
        query = "INSERT INTO users (first_name, last_name) VALUES (%s, %s)"
        values = (user_dto.first_name, user_dto.last_name)

        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        print(f"User {user_dto.first_name} {user_dto.last_name} saved to MySQL.")
