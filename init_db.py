import psycopg2
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

def init_database():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS students')
    cursor.execute('''
        CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            rollno VARCHAR(50) UNIQUE NOT NULL,
            feedback TEXT,
            img VARCHAR(500)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()
    print("✓ Database table created!")

if __name__ == '__main__':
    init_database()
