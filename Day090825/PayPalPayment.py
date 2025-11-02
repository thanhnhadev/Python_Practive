from PaymentGateway import PaymentGateway
class PayPalPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Thanh toán  {amount} qua PayPal...")
        print(f"so tien  {amount} đã thanh toan thanh cong")


