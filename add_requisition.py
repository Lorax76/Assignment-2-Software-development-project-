req_counter = 0

def add_requisition():
    global req_counter
    
    print("Enter your information:")
    
    # Staff details (Using python input methods to collect info about a staff member)
    date = input("Please enter the date: ")
    staff_id = input("Please enter your staff ID: ")
    staff_name = input("Please enter your full name: ")
    
    # Create the requisition ID
    req_counter += 1
    req_id = 10000 + req_counter
    print("Generated Requisition ID:", req_id)
    
    print("\nAdd Items:")
    items = []
    total = 0
    
    # Using a while loop to keep adding items
    add_more = "yes"
    while add_more.lower() == "yes":
        item_name = input("Item Name: ")
        item_price = float(input("Item Price ($): "))
        
        # Store each item in a list
        items.append({"name": item_name, "price": item_price})
        total += item_price
        
        # Ask the user if they want to keep adding items
        add_more = input("Do you want to add another item (yes/no): ")
    
    print("The total cost of all items is $", total)
    
    return {
        "date": date,
        "staff_id": staff_id,
        "staff_name": staff_name,
        "req_id": req_id,
        "items": items,
        "total": total
    }

if __name__ == "__main__":
    add_requisition()
