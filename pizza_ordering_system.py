{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ac6264f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import Tk, Label, StringVar, BooleanVar, Radiobutton, Checkbutton, Button, simpledialog\n",
    "import csv\n",
    "from datetime import datetime\n",
    "\n",
    "class PizzaOrderingSystem:\n",
    "    def __init__(self, master):\n",
    "        self.master = master\n",
    "        master.title(\"Pizza Ordering System\")\n",
    "\n",
    "        # Define the available pizza types and their prices\n",
    "        self.pizzas = [\n",
    "            {\"name\": \"Margarita\", \"description\": \"Tomato sauce, mozzarella cheese\", \"price\": 10},\n",
    "            {\"name\": \"Pepperoni\", \"description\": \"Tomato sauce, mozzarella cheese, pepperoni\", \"price\": 12},\n",
    "            {\"name\": \"Supreme\", \"description\": \"Tomato sauce, mozzarella cheese, pepperoni, mushrooms, peppers, onions\", \"price\": 15}\n",
    "        ]\n",
    "\n",
    "        # Define the available extra ingredients and their prices\n",
    "        self.extras = [\n",
    "            {\"name\": \"Mushrooms\", \"price\": 1},\n",
    "            {\"name\": \"Peppers\", \"price\": 1},\n",
    "            {\"name\": \"Onions\", \"price\": 1},\n",
    "            {\"name\": \"Pepperoni\", \"price\": 2},\n",
    "            {\"name\": \"Extra cheese\", \"price\": 2}\n",
    "        ]\n",
    "\n",
    "        # Create the pizza selection widgets\n",
    "        self.pizza_label = Label(master, text=\"Select a pizza:\")\n",
    "        self.pizza_label.pack()\n",
    "        self.pizza_var = StringVar()\n",
    "        self.pizza_var.set(self.pizzas[0][\"name\"])\n",
    "        for pizza in self.pizzas:\n",
    "            Radiobutton(master, text=f\"{pizza['name']} (${pizza['price']})\", variable=self.pizza_var, value=pizza[\"name\"]).pack()\n",
    "\n",
    "        # Create the extra selection widgets\n",
    "        self.extra_label = Label(master, text=\"Select any extras:\")\n",
    "        self.extra_label.pack()\n",
    "        self.extra_vars = {}\n",
    "        for extra in self.extras:\n",
    "            var = BooleanVar()\n",
    "            Checkbutton(master, text=f\"{extra['name']} (${extra['price']})\", variable=var).pack()\n",
    "            self.extra_vars[extra[\"name\"]] = var\n",
    "\n",
    "        # Create the price label\n",
    "        self.price_label = Label(master, text=\"\")\n",
    "        total_price = self.calculate_price()\n",
    "        self.price_label.config(text=f\"Total price: ${total_price:.2f}\")\n",
    "        self.price_label.pack()\n",
    "\n",
    "        # Create the order button\n",
    "        self.order_button = Button(master, text=\"Place order\", command=self.place_order)\n",
    "        self.order_button.pack()\n",
    "\n",
    "    def calculate_price(self):\n",
    "        # Calculate the total price of the order\n",
    "        pizza_price = next((p[\"price\"] for p in self.pizzas if p[\"name\"] == self.pizza_var.get()), 0)\n",
    "        extra_prices = sum(extra[\"price\"] for extra in self.extras if self.extra_vars[extra[\"name\"]].get())\n",
    "        total_price = pizza_price + extra_prices\n",
    "        return total_price\n",
    "\n",
    "    def place_order(self):\n",
    "        # Collect the customer's information and add it to the Orders_Database.csv file\n",
    "        pizza_name = self.pizza_var.get()\n",
    "        extras = [extra[\"name\"] for extra in self.extras if self.extra_vars[extra[\"name\"]].get()]\n",
    "        total_price = self.calculate_price()\n",
    "        customer_id = simpledialog.askstring(\"Customer ID\", \"Please enter your customer ID:\")\n",
    "        customer_name = simpledialog.askstring(\"Name\", \"Please enter your name:\")\n",
    "        credit_card_number = simpledialog.askstring(\"Credit card number\", \"Please enter your credit card number:\")\n",
    "        password = simpledialog.askstring(\"Password\", \"Please enter your password:\")\n",
    "        order_description = f\"{pizza_name} pizza with \"\n",
    "        for extra in extras:\n",
    "            order_description += f\"{extra}, \"\n",
    "        order_description = order_description.rstrip(\", \")\n",
    "        with open(\"Orders_Database.csv\", \"a\") as file:\n",
    "            writer = csv.writer(file)\n",
    "            writer.writerow([customer_id, customer_name, credit_card_number, password, order_description, total_price])\n",
    "        messagebox.showinfo(\"Order placed\", \"Your order has been placed. Thank you!\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
