from __future__ import annotations
from abc import ABC, abstractmethod


class Developer(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        # Вызываем фабричный метод, чтобы получить объект-продукт
        product = self.factory_method()

        # Работаем с этим продуктом
        result = f"Creator: Today the company has created a new game: {product.operation()}"

        return result


class ComputerDeveloper(Developer):
    def factory_method(self) -> Game:
        return ComputerGame()


class MobileDeveloper(Developer):
    def factory_method(self) -> Game:
        return MobileGame()


class Game(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ComputerGame(Game):
    def operation(self) -> str:
        return "Computer game created"


class MobileGame(Game):
    def operation(self) -> str:
        return "Mobile game created"


def client_code(creator: Developer):

    # print(f"Client: I'm not aware of the creator's class, but it still works.\n"
    #       f"{creator.some_operation()}", end="")
    result = (f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}")
    return result


if __name__ == "__main__":
    print("App: Launched with the ComputerDeveloper.")
    print(client_code(ComputerDeveloper()))
    print("\n")

    print("App: Launched with the MobileDeveloper.")
    print(client_code(MobileDeveloper()))
    print("\n")
