import mysql.connector
from src.interface_adapters.gateways.user_repository_interface import UserRepositoryInterface
from src.entities.user_dto import UserDTO


class MySQLUserRepository(UserRepositoryInterface):
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306):
        self.host = host
        self.user = user
        self.password = password  # تأكد من أنه فارغ إذا كانت كلمة المرور فارغة
        self.database = database
        self.port = port

    def _connect(self):
        """ إنشاء اتصال بقاعدة بيانات MySQL مع رسائل تشخيصية """
        print(f"Connecting to MySQL at {self.host}:{self.port}...")  # طباعة لفحص الاتصال
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,  # إذا كانت كلمة المرور فارغة، تأكد من أن هذه فارغة
                database=self.database,
                port=self.port
            )
            print("Connected to MySQL successfully!")  # تأكد من نجاح الاتصال
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise  # أعد رمي الاستثناء لمزيد من المعالجة

    def save(self, user_dto: UserDTO) -> None:
        """ حفظ بيانات المستخدم في قاعدة البيانات """
        try:
            connection = self._connect()
            cursor = connection.cursor()
            query = "INSERT INTO users (first_name, last_name) VALUES (%s, %s)"
            values = (user_dto.first_name, user_dto.last_name)

            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            print(f"User {user_dto.first_name} {user_dto.last_name} saved to MySQL.")
        except Exception as e:
            print(f"Error during save operation: {e}")
            raise  # أعد رمي الاستثناء
