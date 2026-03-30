contacts = []

def add_contact():
    number = input("Введіть номер: ")
    contacts.append(number)

def show_contacts():
    for contact in contacts:
        print(contact)

while True:
    print("1 - Додати контакт")
    print("2 - Показати контакти")
    choice = input("Вибір: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()