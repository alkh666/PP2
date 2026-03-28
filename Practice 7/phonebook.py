import csv
import psycopg2
from connect import get_connection


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id         SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name  VARCHAR(100),
            phone      VARCHAR(30) UNIQUE
        )
    """)
    conn.commit()
    cur.close()
    conn.close()


def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
                    (row['first_name'], row['last_name'], row['phone'])
                )
                conn.commit()
            except psycopg2.errors.UniqueViolation:
                conn.rollback()
                print(f"Phone {row['phone']} already exists, skipped.")
    cur.close()
    conn.close()


def insert_from_console():
    first_name = input("First name: ")
    last_name  = input("Last name: ")
    phone      = input("Phone: ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)",
            (first_name, last_name, phone)
        )
        conn.commit()
        print("Contact added.")
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("This phone already exists.")
    cur.close()
    conn.close()


def update_contact():
    name = input("Enter first name of contact to update: ")
    print("1 - Update first name")
    print("2 - Update phone")
    choice = input("Choice: ")
    conn = get_connection()
    cur = conn.cursor()
    if choice == '1':
        new_name = input("New first name: ")
        cur.execute("UPDATE contacts SET first_name = %s WHERE first_name = %s", (new_name, name))
    elif choice == '2':
        new_phone = input("New phone: ")
        cur.execute("UPDATE contacts SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()
    print(f"{cur.rowcount} record(s) updated.")
    cur.close()
    conn.close()


def search_contacts():
    print("1 - Search by name")
    print("2 - Search by phone prefix")
    choice = input("Choice: ")
    conn = get_connection()
    cur = conn.cursor()
    if choice == '1':
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM contacts WHERE first_name ILIKE %s OR last_name ILIKE %s",
            (f"%{name}%", f"%{name}%")
        )
    elif choice == '2':
        prefix = input("Enter phone prefix: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{prefix}%",))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found.")
    cur.close()
    conn.close()


def delete_contact():
    print("1 - Delete by first name")
    print("2 - Delete by phone")
    choice = input("Choice: ")
    conn = get_connection()
    cur = conn.cursor()
    if choice == '1':
        name = input("First name: ")
        cur.execute("DELETE FROM contacts WHERE first_name = %s", (name,))
    elif choice == '2':
        phone = input("Phone: ")
        cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
    conn.commit()
    print(f"{cur.rowcount} record(s) deleted.")
    cur.close()
    conn.close()


def list_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY id")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Phone book is empty.")
    cur.close()
    conn.close()


def main():
    create_table()
    while True:
        print("\n1 - List all")
        print("2 - Search")
        print("3 - Add from console")
        print("4 - Import from CSV")
        print("5 - Update")
        print("6 - Delete")
        print("0 - Exit")
        choice = input("Choice: ")

        if choice == '1':
            list_all()
        elif choice == '2':
            search_contacts()
        elif choice == '3':
            insert_from_console()
        elif choice == '4':
            filename = input("CSV filename [contacts.csv]: ") or "contacts.csv"
            insert_from_csv(filename)
        elif choice == '5':
            update_contact()
        elif choice == '6':
            delete_contact()
        elif choice == '0':
            break


main()
