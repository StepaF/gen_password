# My first project
## Generate password
**My first repository. In this project i create simple password generator on python**

``Сonnecting the choice function from the random module:``

```python
from random import choice
```
___
``Creating a main class:``

```python
class PasswordGenerator:
    """Main class for generating password"""
    def __init__(self, length: int):
        self.length = length
        self.characters = (
            'abcdefghijklmnopqrstuvwxyz'  # lowercase letters
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # capital letters
            '0123456789'                     # numbers
            '!@#$%^&*()-_=+[]{}|;:,.<>?/'    # special characters
        )

    def get_random_character(self):
        """Returns a random character from a character set"""
        return choice(self.characters)

    def generate_password(self) -> str:
        """Generates a password of the specified length"""
        password: str = ''.join(self.get_random_character() for _ in range(self.length))
        return password

    def display_password(self) -> None:
        """Displays the generated password on the screen."""
        password = self.generate_password()
        print("Generated password:", password)
```
___

``Connection of the structure __main__:``

```python
if __name__ == "__main__":
    length: int = int(input("Enter password length: "))
    generator = PasswordGenerator(length)
    generator.display_password()
```