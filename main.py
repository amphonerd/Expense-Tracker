from db import get_connection, create_tables
from expenses import add_expense, show_expenses, update_expense, delete_expense
from reports import monthly_report, top_five, export_csv


def main():
    connection = get_connection()
    create_tables(connection)

    while True:
        print()
        print("1. Add expense")
        print("2. View expenses")
        print("3. Update expense")
        print("4. Delete expense")
        print("5. Monthly report")
        print("6. Top 5 expenses")
        print("7. Export month to CSV")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_expense(connection)
        elif choice == "2":
            show_expenses(connection)
        elif choice == "3":
            update_expense(connection)
        elif choice == "4":
            delete_expense(connection)
        elif choice == "5":
            monthly_report(connection)
        elif choice == "6":
            top_five(connection)
        elif choice == "7":
            export_csv(connection)
        elif choice == "0":
            break
        else:
            print("Invalid choice")

    connection.close()


main()
