from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._available = True

    @abstractmethod
    def display_info(self):
        pass

    def borrow(self):
        if self._available:
            self._available = False
            print(f"'{self.title}' đã được mượn.")
        else:
            print(f"'{self.title}' hiện không có sẵn.")

    def return_item(self):
        if not self._available:
            self._available = True
            print(f"'{self.title}' đã được trả.")
        else:
            print(f"'{self.title}' đã có sẵn trong thư viện.")

    def is_available(self):
        return self._available
