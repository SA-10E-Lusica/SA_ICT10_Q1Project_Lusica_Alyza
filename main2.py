from pyscript import document, display

def create_order(e):

    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")
    
    prices = {
        "item1": float(item1.value),
        "item2": float(item2.value),
        "item3": float(item3.value),
        "item4": float(item4.value),
        "item5": float(item5.value)
    }
    
    total = (prices["item1"] * item1.checked +
             prices["item2"] * item2.checked +
             prices["item3"] * item3.checked +
             prices["item4"] * item4.checked +
             prices["item5"] * item5.checked)
    
    customer_name = document.getElementById("customer").value.strip()
    customer_address = document.getElementById("address").value.strip()
    contact_number = document.getElementById("contact_number").value.strip()
    
    display(f"Order for: {customer_name}", target="order_output1")
    display(f"Address: {customer_address}", target="order_output2")
    display(f"Contact number: {contact_number}", target="order_output3")
    display(f"Total: ₱{total:.2f}", target="show")
