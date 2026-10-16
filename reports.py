import csv
from validation import get_month


def monthly_report(connection):
    month = get_month()
    if month is None:
        return

    cur = connection.cursor()

    # total for the month
    cur.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM expenses "
        "WHERE date_trunc('month', expense_date) = %s",
        (month,),
    )
    total = cur.fetchone()[0]
    print("Total spent:", total)

    # split by category
    cur.execute(
        "SELECT c.name, SUM(e.amount) "
        "FROM expenses e JOIN categories c ON e.category_id = c.id "
        "WHERE date_trunc('month', e.expense_date) = %s "
        "GROUP BY c.name ORDER BY SUM(e.amount) DESC",
        (month,),
    )
    for row in cur.fetchall():
        print(row[0], ":", row[1])
    cur.close()


def top_five(connection):
    cur = connection.cursor()
    cur.execute(
        "SELECT e.expense_date, c.name, e.amount, e.description "
        "FROM expenses e JOIN categories c ON e.category_id = c.id "
        "ORDER BY e.amount DESC LIMIT 5"
    )
    for row in cur.fetchall():
        print(row[0], row[1], row[2], row[3])
    cur.close()


def export_csv(connection):
    month = get_month()
    if month is None:
        return

    cur = connection.cursor()
    cur.execute(
        "SELECT e.id, e.expense_date, c.name, e.amount, e.description "
        "FROM expenses e JOIN categories c ON e.category_id = c.id "
        "WHERE date_trunc('month', e.expense_date) = %s "
        "ORDER BY e.expense_date",
        (month,),
    )
    rows = cur.fetchall()
    cur.close()

    filename = "report_" + str(month)[:7] + ".csv"
    f = open(filename, "w", newline="")
    writer = csv.writer(f)
    writer.writerow(["id", "date", "category", "amount", "description"])
    for row in rows:
        writer.writerow(row)
    f.close()
    print("Saved", len(rows), "rows to", filename)
