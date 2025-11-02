from item import Item

class Novel(Item):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def display_info(self):
        status = "Có sẵn" if self._available else "Đã mượn"
        print(f"[Tiểu Thuyết] Tiêu đề: {self.title}, Tác giả: {self.author}, Thể loại: {self.genre}, Trạng thái: {status}")
