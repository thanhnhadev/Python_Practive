class Item:
    def __init__(self,name, price, quantity):
       
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Giá: {self.price:,.0f} VNĐ, SL: {self.quantity})"

    def total_price(self):
        return self.price * self.quantity