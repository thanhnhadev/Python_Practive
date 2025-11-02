from item import Item

class Textbook(Item):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def display_info(self):
        status = "Có sẵn" if self._available else "Đã mượn"
        print(f"[Sách Giáo Khoa] Tiêu đề: {self.title}, Tác giả: {self.author}, Môn học: {self.subject}, Trạng thái: {status}")
