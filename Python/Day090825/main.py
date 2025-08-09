
from PayPalPayment import PayPalPayment
from CreditCardPayment import CreditCardPayment
payment = CreditCardPayment()
payment.process_payment(500)

payment = PayPalPayment()
payment.process_payment(300)