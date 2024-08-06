class Shoe:
    def __init__(self, shoe_type, shoe_style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

class ShoeView:
    def show_shoe(self, shoe):
        print(f"Type: {shoe.shoe_type}")
        print(f"Style: {shoe.shoe_style}")
        print(f"Color: {shoe.color}")
        print(f"Price: {shoe.price}")
        print(f"Manufacturer: {shoe.manufacturer}")
        print(f"Size: {shoe.size}")

class ShoeController:
    def __init__(self, shoe, view):
        self.shoe = shoe
        self.view = view

    def set_shoe_type(self, shoe_type):
        self.shoe.shoe_type = shoe_type

    def set_shoe_style(self, shoe_style):
        self.shoe.shoe_style = shoe_style

    def set_color(self, color):
        self.shoe.color = color

    def set_price(self, price):
        self.shoe.price = price

    def set_manufacturer(self, manufacturer):
        self.shoe.manufacturer = manufacturer

    def set_size(self, size):
        self.shoe.size = size

    def update_view(self):
        self.view.show_shoe(self.shoe)

shoe = Shoe("men's", "sneakers", "white", 100, "Nike", 45)
view = ShoeView()
controller = ShoeController(shoe, view)

controller.update_view()

controller.set_shoe_type("women's")
controller.set_shoe_style("boots")
controller.set_color("black")
controller.set_price(150)
controller.set_manufacturer("Adidas")
controller.set_size(38)

controller.update_view()