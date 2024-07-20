def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner

def main():
    contacts = {}

    while True:
        command_input = input("Enter a command: ").strip().lower()

        if command_input in ['exit', 'close']:
            print("Exiting program...")
            break
        elif command_input == 'hello':
            print("How can I help you?")
        else:
            command, args = parse_input(command_input)

            if command == 'add':
                print(add_contact(contacts, *args))
            elif command == 'change':
                print(change_contact(contacts, *args))
            elif command == 'phone':
                print(show_phone(contacts, *args))
            elif command == 'all':
                show_all_contacts(contacts)
            else:
                print("Invalid command. Please try again.")

@input_error
def parse_input(command_input):
    parts = command_input.split()
    if len(parts) == 0:
        raise IndexError
    command = parts[0]
    args = parts[1:]  
    return command, args

@input_error
def add_contact(contacts, name, phone_number):
    if not name or not phone_number:
        raise ValueError
    contacts[name.lower()] = phone_number
    return f"Contact '{name.lower()}' added."

@input_error
def change_contact(contacts, name, new_phone_number):
    if not name or not new_phone_number:
        raise ValueError
    if name.lower() in contacts:
        contacts[name.lower()] = new_phone_number
        return f"Phone number for '{name.lower()}' updated."
    else:
        raise KeyError

@input_error
def show_phone(contacts, name):
    if not name:
        raise ValueError
    if name.lower() in contacts:
        phone_number = contacts[name.lower()]
        return f"Phone number for '{name.lower()}' is {phone_number}."
    else:
        raise KeyError

def show_all_contacts(contacts):
    if contacts:
        print("List of contacts:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
    else:
        print("No contacts saved.")

if __name__ == "__main__":
    print("Welcome to the assistant bot!")
    main()
