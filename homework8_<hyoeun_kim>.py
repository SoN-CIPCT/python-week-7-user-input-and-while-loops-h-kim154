pizza_orders = ["Cheese pizza", "Pepperoni pizza", "Mushroom pizza", "Chicken pizza"]
finished_pizzas = []

while pizza_orders:
    current_pizza = pizza_orders.pop()
    print(current_pizza, "Your pizza pie is finished!")
    finished_pizzas.append(current_pizza)

for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")