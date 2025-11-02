from PaymentGateway import PaymentGateway
class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Thanh toán  {amount} bằng Thẻ Tín Dụng...")
        print(f"so tien  {amount} đã thanh toan thanh cong")