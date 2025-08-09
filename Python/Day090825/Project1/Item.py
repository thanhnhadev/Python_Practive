from abc import ABC, abstractmethod
class Item(ABC):
    def __init__(self,title,author):
        self.title= title
        self.author= author
        self.__available = True  # Private attribute - Encapsulation
        self._borrowed_date = None  # Protected attribute
        # ENCAPSULATION - Thuộc tính được bảo vệ
    @property
    def available(self):
        """Getter để truy cập trạng thái available"""
        return self.__available
    
    def borrow(self):
        """
        Phương thức mượn sách - thay đổi trạng thái available một cách an toàn
        
        Returns:
            bool: True nếu mượn thành công, False nếu sách đã được mượn
        """
        if self.__available:
            self.__available = False
            self._borrowed_date = datetime.now()
            print(f"✅ Mượn sách thành công: '{self.title}'")
            print(f"   Ngày mượn: {self._borrowed_date.strftime('%d/%m/%Y %H:%M')}")
            return True
        else:
            print(f"❌ Không thể mượn: '{self.title}' đã được mượn")
            return False
    
    def return_item(self):
        """
        Phương thức trả sách - thay đổi trạng thái available một cách an toàn
        
        Returns:
            bool: True nếu trả thành công, False nếu sách chưa được mượn
        """
        if not self.__available:
            self.__available = True
            returned_date = datetime.now()
            if self._borrowed_date:
                days_borrowed = (returned_date - self._borrowed_date).days
                print(f"✅ Trả sách thành công: '{self.title}'")
                print(f"   Ngày trả: {returned_date.strftime('%d/%m/%Y %H:%M')}")
                print(f"   Số ngày mượn: {days_borrowed} ngày")
            else:
                print(f"✅ Trả sách thành công: '{self.title}'")
            self._borrowed_date = None
            return True
        else:
            print(f"❌ Không thể trả: '{self.title}' chưa được mượn")
            return False
    
    def get_status(self):
        """Trả về trạng thái hiện tại của sách"""
        return "📗 Có sẵn" if self.__available else "📕 Đã được mượn"
    
    # ABSTRACTION - Phương thức trừu tượng
    @abstractmethod
    def display_info(self):
        """
        Phương thức trừu tượng hiển thị thông tin sách
        Phải được triển khai bởi các lớp con
        """
        pass
