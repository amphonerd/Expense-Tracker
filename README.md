# Expense Tracker CLI

A command-line expense tracker built with Python and PostgreSQL.

## Features
- Add, view, update and delete expenses (CRUD)
- Normalized schema: `categories` and `expenses` linked by a foreign key
- Monthly total and category-wise report using SQL aggregation
- Top 5 largest expenses
- Input validation (positive amounts, valid dates, valid category)
- Export a month's report to CSV
- Parameterized queries to prevent SQL injection

## Setup
1. Install PostgreSQL and create a database: `createdb expense_db`
2. Install the driver: `pip install psycopg2-binary`
3. Open `db.py` and put in your own postgres user and password
4. Run: `python main.py` (tables are created automatically from `schema.sql`)

## Tech
Python, PostgreSQL, SQL, psycopg2

