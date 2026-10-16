CREATE TABLE IF NOT EXISTS categories (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS expenses (
    id           SERIAL PRIMARY KEY,
    amount       NUMERIC(10,2) NOT NULL CHECK (amount > 0),
    category_id  INT NOT NULL REFERENCES categories(id),
    description  TEXT,
    expense_date DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE INDEX IF NOT EXISTS idx_expenses_date ON expenses(expense_date);

INSERT INTO categories (name) VALUES
    ('Food'), ('Transport'), ('Rent'), ('Shopping'), ('Entertainment'), ('Other')
ON CONFLICT (name) DO NOTHING;
