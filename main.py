from pyscript import display

restaurant_name = "🌀 Sea Breeze 🌀"
owner_name = "Alyza Lusica"

year_since = 2025

tax_rate = 0.08  # 8% tax

has_delivery = True
is_dine_in = True
is_takeaway = False

product_names = [
    "Venetian Shrimp with Polenta",
    "Seafood Paella",
    "Scallop Sliders",
    "Crispy Crab Cakes",
    "Lobster Rolls"
]

business_hours = ("9:00 AM", "10:00 PM")

menu_prices = {
    "Venetian Shrimp with Polenta": 375.00,
    "Seafood Paella": 450.00,
    "Scallop Sliders": 200.00,
    "Crispy Crab Cakes": 250.00,
    "Lobster Rolls": 300.00
}

common_allergens = {"Seafood", "Shellfish", "Dairy"}

display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Est. {year_since}", target="since")
display("Menu & Pricelist", target="heading1")

for i, product in enumerate(product_names, start=1):
    display(product, target=f"prod{i}")
    display(f"₱{menu_prices[product]:.2f}", target=f"price{i}")

display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

order_type_text = "Dine-in & Takeout Available"
if has_delivery:
    order_type_text += " | Delivery Available"
display(order_type_text, target="orderType")

display("Common Allergens: " + ", ".join(common_allergens), target="allergens")
display(f"Tax Rate: {tax_rate*100:.0f}%", target="taxRate")
