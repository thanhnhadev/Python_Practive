# class order
class Order:
    def __init__(self, order_id, product_name, quantity, price_per_unit):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = int(quantity)
        self.price_per_unit = float(price_per_unit)

    def __repr__(self):
        return (f"Order(id={self.order_id}, product='{self.product_name}', "
                f"qty={self.quantity}, price={self.price_per_unit})")
