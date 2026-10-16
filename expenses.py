from validation import get_amount, get_date


def show_categories(connection):
    cur = connection.cursor()
    cur.execute("SELECT id, name FROM categories ORDER BY id")
    rows = cur.fetchall()
    cur.close()

    ids = []
    for row in rows:
        print(row[0], "-", row[1])
        ids.append(row[0])
    return ids


def add_expense(connection):
    amount = get_amount()
    if amount is None:
        return

    ids = show_categories(connection)
    try:
        category_id = int(input("Category number: "))
    except ValueError:
        print("Please enter a number")
        return
    if category_id not in ids:
        print("No such category")
        return

    description = input("Description: ")
    expense_date = get_date()
    if expense_date is None:
        return

    cur = connection.cursor()
    cur.execute(
        "INSERT INTO expenses (amount, category_id, description, expense_date) "
        "VALUES (%s, %s, %s, %s)",
        (amount, category_id, description, expense_date),
    )
    connection.commit()
    cur.close()
    print("Expense added")


def show_expenses(connection):
    cur = connection.cursor()
    cur.execute(
        "SELECT e.id, e.expense_date, c.name, e.amount, e.description "
        "FROM expenses e JOIN categories c ON e.category_id = c.id "
        "ORDER BY e.expense_date DESC"
    )
    rows = cur.fetchall()
    cur.close()

    if len(rows) == 0:
        print("No expenses yet")
        return

    for row in rows:
        print(row[0], row[1], row[2], row[3], row[4])


def update_expense(connection):
    try:
        expense_id = int(input("Id of expense to update: "))
    except ValueError:
        print("Please enter a number")
        return

    amount = get_amount()
    if amount is None:
        return
    description = input("New description: ")

    cur = connection.cursor()
    cur.execute(
        "UPDATE expenses SET amount = %s, description = %s WHERE id = %s",
        (amount, description, expense_id),
    )
    connection.commit()
    if cur.rowcount == 0:
        print("No expense with that id")
    else:
        print("Updated")
    cur.close()


def delete_expense(connection):
    try:
        expense_id = int(input("Id of expense to delete: "))
    except ValueError:
        print("Please enter a number")
        return

    cur = connection.cursor()
    cur.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
    connection.commit()
    if cur.rowcount == 0:
        print("No expense with that id")
    else:
        print("Deleted")
    cur.close()
