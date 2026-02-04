import csv

# Predefined phonebook dictionary
phonebook = {
    "Rahul": "9876543210",
    "Sakshi": "9123456780",
    "Aman": "9988776655",
    "Harsh": "4567890877"
}

def load_from_csv():
    """Loads data from phonebook.csv into phonebook dictionary in a simple way."""
    
    try:
        with open("phonebook.csv", "r") as file:
            reader = csv.DictReader(file)

            # Directly fill dictionary from CSV
            for row in reader:
                phonebook[row["name"]] = row["phone"]

        print("CSV loaded successfully!\n")

    except FileNotFoundError:
        print("CSV file not found. Starting with predefined phonebook.\n")


def save_to_csv():
    """Saves the phonebook dictionary to phonebook.csv"""
    
    with open("phonebook.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "phone"])      # header
        writer.writerows(phonebook.items())     # write all rows


def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")

    phonebook[name] = number
    save_to_csv()

    print("Contact added and saved to CSV!")


def search_contact():
    name = input("Enter name to search: ")
    if name in phonebook:
        print("Number:", phonebook[name])
    else:
        print("Contact not found")


def delete_contact():
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        save_to_csv()
        print("Contact deleted and CSV updated!")
    else:
        print("Contact not found")


def view_all():
    if not phonebook:
        print("Phonebook is empty")
    else:
        print("\nAll Contacts:")
        for name, number in phonebook.items():
            print(name, ":", number)


def summary():
    print("\n--- Phonebook Summary ---")
    print("Total contacts:", len(phonebook))


def exit_app():
    print("Exiting… Goodbye!")
    exit()


# MENU MAP
menu = {
    "1": add_contact,
    "2": search_contact,
    "3": delete_contact,
    "4": view_all,
    "5": summary,
    "6": exit_app
}

load_from_csv()

save_to_csv()

# MENU LOOP
while True:
    print("\nChoose an option:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. View Summary")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ")
    function = menu.get(choice)

    if function:
        function()
    else:
        print("Invalid choice. Try again.")
