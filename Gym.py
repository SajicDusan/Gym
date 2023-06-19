import sqlite3

conn = sqlite3.connect('gym_management.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_card TEXT,
                    name TEXT,
                    surname TEXT,
                    age INTEGER,
                    number TEXT,
                    gender TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS trainers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    program TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS staff (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    surname TEXT,
                    shift TEXT,
                    number TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS equipment (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                )''')

class Member:
    def __init__(self, id_card, name, surname, age, number, gender):
        self.id_card = id_card
        self.name = name
        self.surname = surname
        self.age = age
        self.number = number
        self.gender = gender

    def add_member(self):
        cursor.execute("INSERT INTO members (id_card, name, surname, age, number, gender) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.id_card, self.name, self.surname, self.age, self.number, self.gender))
        conn.commit()

    @staticmethod
    def view_all_members():
        cursor.execute("SELECT * FROM members")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def update_member(self, member_id):
        cursor.execute("UPDATE members SET id_card=?, name=?, surname=?, age=?, number=?, gender=? WHERE id=?",
                       (self.id_card, self.name, self.surname, self.age, self.number, self.gender, member_id))
        conn.commit()

    @staticmethod
    def delete_member(member_id):
        cursor.execute("DELETE FROM members WHERE id=?", (member_id,))
        conn.commit()

class Trainer:
    def __init__(self, name, program):
        self.name = name
        self.program = program

    def add_trainer(self):
        cursor.execute("INSERT INTO trainers (name, program) VALUES (?, ?)",
                       (self.name, self.program))
        conn.commit()

    @staticmethod
    def view_all_trainers():
        cursor.execute("SELECT * FROM trainers")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def update_trainer(self, trainer_id):
        cursor.execute("UPDATE trainers SET name=?, program=? WHERE id=?",
                       (self.name, self.program, trainer_id))
        conn.commit()

    @staticmethod
    def delete_trainer(trainer_id):
        cursor.execute("DELETE FROM trainers WHERE id=?", (trainer_id,))
        conn.commit()

class Staff:
    def __init__(self, name, surname, shift, number):
        self.name = name
        self.surname = surname
        self.shift = shift
        self.number = number

    def add_staff(self):
        cursor.execute("INSERT INTO staff (name, surname, shift, number) VALUES (?, ?, ?, ?)",
                       (self.name, self.surname, self.shift, self.number))
        conn.commit()

    @staticmethod
    def view_all_staff():
        cursor.execute("SELECT * FROM staff")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def update_staff(self, staff_id):
        cursor.execute("UPDATE staff SET name=?, surname=?, shift=?, number=? WHERE id=?",
                       (self.name, self.surname, self.shift, self.number, staff_id))
        conn.commit()

    @staticmethod
    def delete_staff(staff_id):
        cursor.execute("DELETE FROM staff WHERE id=?", (staff_id,))
        conn.commit()

class Equipment:
    def __init__(self, name):
        self.name = name

    def add_equipment(self):
        cursor.execute("INSERT INTO equipment (name) VALUES (?)", (self.name,))
        conn.commit()

    @staticmethod
    def view_all_equipment():
        cursor.execute("SELECT * FROM equipment")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    @staticmethod
    def remove_equipment(equipment_id):
        cursor.execute("DELETE FROM equipment WHERE id=?", (equipment_id,))
        conn.commit()


def display_menu():
    print("\n*** GYM MANAGEMENT SYSTEM MENU ***")
    print("1. Member Management")
    print("2. Trainer Management")
    print("3. Staff Management")
    print("4. Equipment Management")
    print("5. Exit")


def display_member_menu():
    print("\n*** MEMBER MANAGEMENT MENU ***")
    print("1. Add New Member")
    print("2. View All Members")
    print("3. Update Member")
    print("4. Delete Member")
    print("5. Go Back")

def display_trainer_menu():
    print("\n*** TRAINER MANAGEMENT MENU ***")
    print("1. Add New Trainer")
    print("2. View All Trainers")
    print("3. Update Trainer")
    print("4. Delete Trainer")
    print("5. Go Back")


def display_staff_menu():
    print("\n*** STAFF MANAGEMENT MENU ***")
    print("1. Add New Staff")
    print("2. View All Staff Members")
    print("3. Update Staff Member")
    print("4. Delete Staff Member")
    print("5. Go Back")

def display_equipment_menu():
    print("\n*** EQUIPMENT MANAGEMENT MENU ***")
    print("1. Add New Equipment")
    print("2. View All Equipment")
    print("3. Remove Equipment")
    print("4. Go Back")

def add_member():
    print("\n*** ADD NEW MEMBER ***")
    id_card = input("Enter ID Card: ")
    name = input("Enter Name: ")
    surname = input("Enter Surname: ")
    age = int(input("Enter Age: "))
    number = input("Enter Number: ")
    gender = input("Enter Gender: ")
    member = Member(id_card, name, surname, age, number, gender)
    member.add_member()
    print("Member added successfully!")

def view_all_members():
    print("\n*** VIEW ALL MEMBERS ***")
    Member.view_all_members()

def update_member():
    print("\n*** UPDATE MEMBER ***")
    member_id = int(input("Enter Member ID to update: "))
    id_card = input("Enter ID Card: ")
    name = input("Enter Name: ")
    surname = input("Enter Surname: ")
    age = int(input("Enter Age: "))
    number = input("Enter Number: ")
    gender = input("Enter Gender: ")
    member = Member(id_card, name, surname, age, number, gender)
    member.update_member(member_id)
    print("Member updated successfully!")

def delete_member():
    print("\n*** DELETE MEMBER ***")
    member_id = int(input("Enter Member ID to delete: "))
    Member.delete_member(member_id)
    print("Member deleted successfully!")

def add_trainer():
    print("\n*** ADD NEW TRAINER ***")
    name = input("Enter Name: ")
    program = input("Enter Program: ")
    trainer = Trainer(name, program)
    trainer.add_trainer()
    print("Trainer added successfully!")

def view_all_trainers():
    print("\n*** VIEW ALL TRAINERS ***")
    Trainer.view_all_trainers()

def update_trainer():
    print("\n*** UPDATE TRAINER ***")
    trainer_id = int(input("Enter Trainer ID to update: "))
    name = input("Enter Name: ")
    program = input("Enter Program: ")
    trainer = Trainer(name, program)
    trainer.update_trainer(trainer_id)
    print("Trainer updated successfully!")

def delete_trainer():
    print("\n*** DELETE TRAINER ***")
    trainer_id = int(input("Enter Trainer ID to delete: "))
    Trainer.delete_trainer(trainer_id)
    print("Trainer deleted successfully!")

def add_staff():
    print("\n*** ADD NEW STAFF MEMBER ***")
    name = input("Enter Name: ")
    surname = input("Enter Surname: ")
    shift = input("Enter Shift: ")
    number = input("Enter Number: ")
    staff = Staff(name, surname, shift, number)
    staff.add_staff()
    print("Staff member added successfully!")

def view_all_staff():
    print("\n*** VIEW ALL STAFF MEMBERS ***")
    Staff.view_all_staff()

def update_staff():
    print("\n*** UPDATE STAFF MEMBER ***")
    staff_id = int(input("Enter Staff ID to update: "))
    name = input("Enter Name: ")
    surname = input("Enter Surname: ")
    shift = input("Enter Shift: ")
    number = input("Enter Number: ")
    staff = Staff(name, surname, shift, number)
    staff.update_staff(staff_id)
    print("Staff member updated successfully!")

def delete_staff():
    print("\n*** DELETE STAFF MEMBER ***")
    staff_id = int(input("Enter Staff ID to delete: "))
    Staff.delete_staff(staff_id)
    print("Staff member deleted successfully!")

def add_equipment():
    print("\n*** ADD NEW EQUIPMENT ***")
    name = input("Enter Equipment Name: ")
    equipment = Equipment(name)
    equipment.add_equipment()
    print("Equipment added successfully!")

def view_all_equipment():
    print("\n*** VIEW ALL EQUIPMENT ***")
    Equipment.view_all_equipment()

def remove_equipment():
    print("\n*** REMOVE EQUIPMENT ***")
    equipment_id = int(input("Enter Equipment ID to remove: "))
    Equipment.remove_equipment(equipment_id)
    print("Equipment removed successfully!")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        while True:
            display_member_menu()
            member_choice = input("Enter your choice (1-5): ")

            if member_choice == '1':
                add_member()
            elif member_choice == '2':
                view_all_members()
            elif member_choice == '3':
                update_member()
            elif member_choice == '4':
                delete_member()
            elif member_choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    elif choice == '2':
        while True:
            display_trainer_menu()
            trainer_choice = input("Enter your choice (1-5): ")

            if trainer_choice == '1':
                add_trainer()
            elif trainer_choice == '2':
                view_all_trainers()
            elif trainer_choice == '3':
                update_trainer()
            elif trainer_choice == '4':
                delete_trainer()
            elif trainer_choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    elif choice == '3':
        while True:
            display_staff_menu()
            staff_choice = input("Enter your choice (1-5): ")

            if staff_choice == '1':
                add_staff()
            elif staff_choice == '2':
                view_all_staff()
            elif staff_choice == '3':
                update_staff()
            elif staff_choice == '4':
                delete_staff()
            elif staff_choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    elif choice == '4':
        while True:
            display_equipment_menu()
            equipment_choice = input("Enter your choice (1-4): ")

            if equipment_choice == '1':
                add_equipment()
            elif equipment_choice == '2':
                view_all_equipment()
            elif equipment_choice == '3':
                remove_equipment()
            elif equipment_choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

conn.close()