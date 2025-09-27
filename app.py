from flask import Flask, request, jsonify

app = Flask(__name__)

# Pizza menu (could be fetched from DB in real-world apps)
menu = [
    {
        "id": 1,
        "name": "Margherita",
        "toppings": ["Tomato", "Mozzarella", "Basil"],
        "sides": ["Garlic Bread", "Coke"]
    },
    {
        "id": 2,
        "name": "Pepperoni",
        "toppings": ["Tomato", "Mozzarella", "Pepperoni"],
        "sides": ["Cheesy Sticks", "Pepsi"]
    },
    {
        "id": 3,
        "name": "Veggie Delight",
        "toppings": ["Tomato", "Mozzarella", "Onions", "Capsicum", "Olives"],
        "sides": ["Salad", "Iced Tea"]
    }
]

# In-memory order storage
orders = []

@app.route("/menu", methods=["GET"])
def get_menu():
    return jsonify({"pizzas": menu})

@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    if not data or "pizza_id" not in data or "customer_name" not in data:
        return jsonify({"error": "Invalid order format"}), 400
    
    # Check if pizza exists
    pizza = next((p for p in menu if p["id"] == data["pizza_id"]), None)
    if not pizza:
        return jsonify({"error": "Pizza not found"}), 404

    order = {
        "order_id": len(orders) + 1,
        "customer_name": data["customer_name"],
        "pizza": pizza["name"],
        "sides": data.get("sides", []),
        "status": "confirmed"
    }
    orders.append(order)
    return jsonify(order), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
