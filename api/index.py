from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch records for current page
    cur.execute('SELECT name, rollno, feedback, img, rating FROM students ORDER BY id LIMIT %s OFFSET %s', (per_page, offset))
    students = cur.fetchall()

    # Get total count for pagination
    cur.execute('SELECT COUNT(*) FROM students')
    total_count = cur.fetchone()[0]
    total_pages = (total_count + per_page - 1) // per_page
    
    cur.close()
    conn.close()

    return render_template('index.html', students=students, page=page, total_pages=total_pages)

# Required for local testing
if __name__ == '__main__':
    app.run(debug=True)
