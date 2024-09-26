from random import choice


class PasswordGenerator:
    """Основной класс для генерирования пароля"""
    def __init__(self, length: int):
        self.length = length
        self.characters = (
            'abcdefghijklmnopqrstuvwxyz'  # строчные буквы
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # заглавные буквы
            '0123456789'                     # цифры
            '!@#$%^&*()-_=+[]{}|;:,.<>?/'    # специальные символы
        )

    def get_random_character(self):
        """Возвращает случайный символ из набора символов."""
        return choice(self.characters)

    def generate_password(self) -> str:
        """Генерирует пароль заданной длины."""
        password: str = ''.join(self.get_random_character() for _ in range(self.length))
        return password

    def display_password(self) -> None:
        """Выводит сгенерированный пароль на экран."""
        password = self.generate_password()
        print("Сгенерированный пароль:", password)


if __name__ == "__main__":
    length: int = int(input("Введите длину пароля: "))
    generator = PasswordGenerator(length)
    generator.display_password()
