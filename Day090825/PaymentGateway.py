# Xây dựng một hệ thống xử lý thanh toán đơn giản.
# Yêu cầu:
# •	Sử dụng module abc để tạo một lớp trừu tượng tên là PaymentGateway.
# •	Trong lớp PaymentGateway, định nghĩa một phương thức trừu tượng tên là process_payment(amount).
# •	Tạo hai lớp con kế thừa từ PaymentGateway:
# o	CreditCardPayment: triển khai process_payment để in ra thông báo "Thanh toán bằng Thẻ Tín Dụng..."
# o	PayPalPayment: triển khai process_payment để in ra thông báo "Thanh toán qua PayPal..."
# •	Tạo một đối tượng từ CreditCardPayment và một từ PayPalPayment, sau đó gọi process_payment() trên từng đối tượng
from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    def process_payment(seft,amount ):
        pass

