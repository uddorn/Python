import psycopg2
from faker import Faker
import random
from tabulate import tabulate
import datetime

DB_PARAMS = {
    "host": "localhost",
    "database": "library_db",
    "user": "admin",
    "password": "adminpassword",
    "port": "5432"
}

fake = Faker('uk_UA')

def get_connection():
    return psycopg2.connect(**DB_PARAMS)

def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS borrows, readers, books CASCADE;")
        
        cur.execute("""
            CREATE TABLE books (
                id SERIAL PRIMARY KEY,
                author VARCHAR(100) NOT NULL,
                title VARCHAR(150) NOT NULL,
                section VARCHAR(50) CHECK (section IN ('технічна', 'художня', 'економічна')),
                publish_year INTEGER CHECK (publish_year > 1900 AND publish_year <= 2024),
                pages INTEGER DEFAULT 100,
                price DECIMAL(10, 2),
                type VARCHAR(50) CHECK (type IN ('посібник', 'книга', 'періодичне видання')),
                copies INTEGER DEFAULT 1,
                max_days INTEGER DEFAULT 14
            );
        """)

        cur.execute("""
            CREATE TABLE readers (
                id SERIAL PRIMARY KEY,
                last_name VARCHAR(50) NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                phone VARCHAR(15) CONSTRAINT chk_phone CHECK (phone SIMILAR TO '\+380[0-9]{9}'),
                address TEXT,
                course INTEGER CONSTRAINT chk_course CHECK (course BETWEEN 1 AND 4),
                student_group VARCHAR(20)
            );
        """)

        cur.execute("""
            CREATE TABLE borrows (
                id SERIAL PRIMARY KEY,
                issue_date DATE NOT NULL DEFAULT CURRENT_DATE,
                reader_id INTEGER REFERENCES readers(id) ON DELETE CASCADE,
                book_id INTEGER REFERENCES books(id) ON DELETE CASCADE
            );
        """)
    conn.commit()
    print("Таблиці успішно створено!")

def populate_data(conn):
    with conn.cursor() as cur:
        sections = ['технічна', 'художня', 'економічна']
        types = ['посібник', 'книга', 'періодичне видання']

        for _ in range(14):
            cur.execute("""
                INSERT INTO books (author, title, section, publish_year, pages, price, type, copies, max_days)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                fake.name(),
                fake.catch_phrase(),
                random.choice(sections),
                random.randint(1990, 2023),
                random.randint(50, 800),
                round(random.uniform(50.0, 1000.0), 2),
                random.choice(types),
                random.randint(1, 10),
                random.choice([7, 14, 30])
            ))

        for _ in range(9):
            cur.execute("""
                INSERT INTO readers (last_name, first_name, phone, address, course, student_group)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                fake.last_name(),
                fake.first_name(),
                f"+380{random.randint(100000000, 999999999)}",
                fake.city(),
                random.randint(1, 4),
                f"ІПЗ-{random.randint(20, 23)}"
            ))

        cur.execute("SELECT id FROM readers;")
        reader_ids = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT id FROM books;")
        book_ids = [row[0] for row in cur.fetchall()]
        
        for _ in range(11):
            cur.execute("""
                INSERT INTO borrows (issue_date, reader_id, book_id)
                VALUES (%s, %s, %s)
            """, (
                fake.date_between(start_date='-1y', end_date='today'),
                random.choice(reader_ids),
                random.choice(book_ids)
            ))

    conn.commit()
    print("Дані успішно згенеровано!")

def print_query(conn, query, title, params=None):
    with conn.cursor() as cur:
        cur.execute(query, params)
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]

        print(f"\n--- {title} ---")
        print(tabulate(rows, headers=colnames, tablefmt="grid"))

def execute_queries(conn):
    print_query(
        conn,
        "SELECT * FROM books WHERE publish_year > 2001 ORDER BY title ASC;",
        "1. Книги після 2001 року"
    )

    print_query(
        conn,
        "SELECT type, COUNT(*) as total_count FROM books GROUP BY type;",
        "2. Кількість книг кожного виду"
    )

    print_query(conn, """
        SELECT DISTINCT r.last_name, r.first_name, r.student_group 
        FROM readers r
        JOIN borrows b ON r.id = b.reader_id
        JOIN books bk ON bk.id = b.book_id
        WHERE bk.type = 'посібник'
        ORDER BY r.last_name ASC;
    """, "3. Читачі, які брали посібники")

    section_param = 'технічна'

    print_query(
        conn,
        "SELECT * FROM books WHERE section = %s;",
        f"4. Книги з розділу: {section_param}",
        (section_param,)
    )

    print_query(conn, """
        SELECT b.id as borrow_id,
               bk.title,
               b.issue_date,
               bk.max_days,
               (b.issue_date + bk.max_days) AS return_date
        FROM borrows b
        JOIN books bk ON b.book_id = bk.id;
    """, "5. Кінцевий термін повернення книг")

    print_query(conn, """
        SELECT section,
               COUNT(CASE WHEN type = 'посібник' THEN 1 END) AS posibnyk_count,
               COUNT(CASE WHEN type = 'книга' THEN 1 END) AS book_count,
               COUNT(CASE WHEN type = 'періодичне видання' THEN 1 END) AS journal_count
        FROM books
        GROUP BY section;
    """, "6. Перехресний запит: Види по розділах")

def print_all_tables(conn):
    print("\n================ ВМІСТ УСІХ ТАБЛИЦЬ ================")

    print_query(conn, "SELECT * FROM books;", "ТАБЛИЦЯ: BOOKS")
    print_query(conn, "SELECT * FROM readers;", "ТАБЛИЦЯ: READERS")
    print_query(conn, "SELECT * FROM borrows;", "ТАБЛИЦЯ: BORROWS")

if __name__ == "__main__":
    try:
        connection = get_connection()

        create_tables(connection)
        populate_data(connection)

        print_all_tables(connection)
        execute_queries(connection)

    except Exception as e:
        print(f"Помилка: {e}")

    finally:
        if connection:
            connection.close()