## write logs to text file.

import csv
import logging

# Configure logging
logging.basicConfig(
    filename="logs.txt",                # log file
    filemode="a",                       # append mode
    format="%(levelname)s: %(message)s",  # show only log level + message
    level=logging.INFO                 # log everything from DEBUG and above
)

phonebook = {
    "Rahul": "9876543210",
    "Sakshi": "9123456780",
    "Aman": "9988776655"
}


def load_from_csv():
    """Loads data from phonebook.csv into phonebook dictionary."""
    try:
        with open("phonebook.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                phonebook[row["name"]] = row["phone"]

        print("CSV loaded successfully!\n")
        logging.info("Loaded phonebook from CSV.")

    except FileNotFoundError:
        print("CSV file not found. Starting with predefined phonebook.\n")
        logging.warning("CSV not found. Using predefined phonebook.")



def save_to_csv():
    """Saves phonebook dictionary to CSV file."""
    with open("phonebook.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "phone"])
        writer.writerows(phonebook.items())

    logging.info("Saved phonebook to CSV.")


def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")

    phonebook[name] = number
    save_to_csv()

    print("Contact added!")
    logging.info(f"Added contact: {name} - {number}")


def search_contact():
    name = input("Enter name to search: ")
    if name in phonebook:
        print("Number:", phonebook[name])
        logging.info(f"Searched for contact: {name} (FOUND)")
    else:
        print("Contact not found")
        logging.warning(f"Searched for contact: {name} (NOT FOUND)")


def delete_contact():
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        save_to_csv()

        print("Contact deleted!")
        logging.info(f"Deleted contact: {name}")
    else:
        print("Contact not found")
        logging.warning(f"Tried deleting contact: {name} (NOT FOUND)")


def view_all():
    if not phonebook:
        print("Phonebook is empty")
    else:
        print("\nAll Contacts:")
        for name, number in phonebook.items():
            print(name, ":", number)

    logging.info("Viewed all contacts.")


def summary():
    print("\n--- Phonebook Summary ---")
    print("Total contacts:", len(phonebook))

    logging.info("Viewed summary.")


def exit_app():
    print("Exiting… Goodbye!")
    logging.info("Exited the application.")
    exit()


menu = {
    "1": add_contact,
    "2": search_contact,
    "3": delete_contact,
    "4": view_all,
    "5": summary,
    "6": exit_app
}


load_from_csv()   # Only load CSV at startup


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
