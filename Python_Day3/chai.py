from abc import ABC, abstractmethod
class Chai(ABC):
    def __inti__(self, name, base_price, quantity_in_stock):
        self.name=name
        self.base_price=base_price
        self.quantity_in_stock=quantity_in_stock

    @abstractmethod
    def calculate_price(self):
        pass
    def display_info(self):
        pass

class MasalaChai(Chai):
    def __inti__(self, name, base_price, quantity_in_stock):
        self.name=name
        self.base_price=base_price
        self.quantity_in_stock=quantity_in_stock
        super()
    def calculate_price(self):
        self.base_price+=10
    def display_info(self):
        print("name:{self.name} base_price:{self.base_price} quantity_in_stock:{self.quantity_in_stock}")
class GingerChai(Chai):
    def calculate_price(self):
        self.base_price+=8
    def display_info(self):
        print("name:{self.name} base_price:{self.base_price} quantity_in_stock:{self.quantity_in_stock}")
class ElaichiChai(Chai):
    def calculate_price(self):
        self.base_price+=12
    def display_info(self):
        print("name:{self.name} base_price:{self.base_price} quantity_in_stock:{self.quantity_in_stock}")

chai1 = MasalaChai("Masala Chai", 20, 50)
print(chai1)