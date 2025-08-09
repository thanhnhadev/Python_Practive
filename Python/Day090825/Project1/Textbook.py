class Textbook(Item):
    def __init__(self, title, author, subject):
        """
        Khởi tạo sách giáo khoa
        
        Args:
            title (str): Tiêu đề sách
            author (str): Tác giả
            subject (str): Môn học
        """
        super().__init__(title, author)
        self.subject = subject
    def display_info(self):
        """Hiển thị thông tin chi tiết của sách giáo khoa"""
        print("📚 SÁCH GIÁO KHOA")
        print(f"   Tiêu đề: {self.title}")
        print(f"   Tác giả: {self.author}")
        print(f"   Môn học: {self.subject}")
        print(f"   Trạng thái: {self.get_status()}")
        if self._borrowed_date and not self.available:
            print(f"   Ngày mượn: {self._borrowed_date.strftime('%d/%m/%Y %H:%M')}")
