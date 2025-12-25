from unittest.mock import Mock


def test_saving_user_calls_repository_save():
    # Arrange
    user = User(first_name="Islam", last_name="Hala")

    spy_user_repository = Mock(spec=UserRepositoryInterface)

    saving_use_case = SavingUseCase(
        user_repository=spy_user_repository
    )

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once_with(user)
