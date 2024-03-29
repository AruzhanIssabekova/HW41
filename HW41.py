class Pizza:
    def __init__(self, name, dough, sauce, toppings):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def prepare(self):
        print(f"Приготовление пиццы {self.name} с {self.dough} тестом, {self.sauce} соусом и начинкой из {', '.join(self.toppings)}.")

    def bake(self):
        print(f"Выпекание пиццы .")

    def cut(self):
        print(f"Нарезка пиццы.")

    def pack(self):
        print(f"Упаковка пиццы.")


class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        total = 0
        for pizza in self.pizzas:
            total += 10
        return total


class Terminal:
    def __init__(self, menu):
        self.menu = menu

    def display_menu(self):
        print("Меню:")
        for i, pizza in enumerate(self.menu, start=1):
            print(f"{i}. {pizza.name}")

    def take_order(self):
        order = Order()
        while True:
            choice = input("Введите номер пиццы (0 для завешения): ")
            if choice == '0':
                break
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.menu):
                    pizza = self.menu[choice - 1]
                    order.add_pizza(pizza)
                    print(f"{pizza.name} добавлена в заказ.")
                else:
                    print("Неверный выбор. Пожалуйста, введите правильный номер пиццы.")
            except ValueError:
                print("Неверный выбор. Пожалуйста, введите правильный номер пиццы.")
        return order


    def confirm_order(self, order):
        print("Ваш заказ:")
        for i, pizza in enumerate(order.pizzas, start=1):
            print(f"{i}. {pizza.name}")
        total = order.calculate_total()
        print(f"Итого: ${total}")
        confirm = input("Подтверждаете заказ? (да/нет): ")
        if confirm.lower() == 'да':
            print("Заказ подтвержден.")
            return True
        else:
            print("Заказ отменен.")
            return False

    def take_payment(self, order):
        total = order.calculate_total()
        print(f"Итого: ${total}.")
        payment = float(input("Внесите деньги: $"))
        if payment >= total:
            change = payment - total
            print(f"Спасибо за заказ. Ваша сдача ${change:.2f}.")
            return True
        else:
            print("Недостаточно средств.")
            return False


if __name__ == "__main__":
    pepperoni = Pizza("Пепперони", "тонкое", "томатный", ["колбаса", "сыр"])
    bbq= Pizza("Барбекью", "толстое", "барбекью", ["курица", "лук", "перец"])
    margarita = Pizza("Маргарита", "тонкое", "томатный", ["сыр", "помидор"])
    menu = [pepperoni, bbq, margarita]
    terminal = Terminal(menu)
    terminal.display_menu()
    order = terminal.take_order()
    if terminal.confirm_order(order):
        terminal.take_payment(order)
        for pizza in order.pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()
        print("Ваш заказ!")
