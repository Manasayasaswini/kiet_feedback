import pandas as pd
import psycopg2
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

def upload_data():
    file_path = 'cleaned_students.csv'
    df = pd.read_csv(file_path)

    # Final safety cleanup
    df['rollno'] = df['rollno'].astype(str).str.strip().str.upper()
    df = df.drop_duplicates(subset=['rollno'], keep='last')

    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO students (name, rollno, feedback, img)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (rollno) DO NOTHING
    """

    # Change this part in your for loop:
    for _, row in df.iterrows():
    # We create the path string based on the roll number
        image_filename = f"{row['rollno']}.jpg" 
    # This matches your folder structure: static/images/ROLLNO.jpg
        image_path = f"images/{image_filename}" 

        cursor.execute(
            insert_query,
            (row['name'], row['rollno'], row['feedback'], image_path) # Now saving the path
        )

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✓ {len(df)} records uploaded successfully!")

if __name__ == "__main__":
    upload_data()

