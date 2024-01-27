# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {"hat": 10, "gloves": 10, "scarf": 10}
for x in inventory.items():
    print(x)

# Function to add an item to the inventory
def add_item(item, quantity):
    # Check if the item exists in the inventory dictionary.
    if item in inventory:
        # Increase its quantity.
        inventory[item] += quantity
    else:
        # Add the item to the inventory with the given quantity.
        inventory[item] = quantity

# Function to view all items in the inventory
def view_inventory():
    # Loop through the inventory dictionary.
    for item, quantity in inventory.items:
        # Print each item's name and its quantity.
        print(f"{item}: {quantity}")

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    # Check if the item exists in the inventory.
    if item in inventory:
        # Update its quantity.
        inventory[item] = quantity
    else:
        # Print a message indicating it's not found.
        print(f"Item '{item}' not found in inventory.")

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("Inventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            break
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()
