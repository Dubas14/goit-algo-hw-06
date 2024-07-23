from collections import UserDict

class Field():
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)
    
    @staticmethod
    def validate_phone(phone):
        return phone.isdigit() and len(phone) == 10


class Record:  # реалізація контролю номерів телефону, додання, видалення , рефакторінг
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)
        
    def remove_phone(self, phone_number):
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError("Phone number not found")
    
    def edit_phone(self, old_number, new_number):
        phone_to_edit = self.find_phone(old_number)
        if phone_to_edit:
            if not Phone.validate_phone(new_number):
                raise ValueError("New phone number must contain 10 digits")
            phone_to_edit.value = new_number
        else:
            raise ValueError("Old phone number not found")
        
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):   # реалізація додання , перепису, та пошуку користувача
    
    
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Record not found.")
    
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())    
        



book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


print(book)


john = book.find("John")
john.edit_phone("1234567890", "1112223333")   

print(john)    

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")