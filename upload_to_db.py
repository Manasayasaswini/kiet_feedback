import pandas as pd
import psycopg2
import os

#DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_URL = 'postgresql://neondb_owner:npg_d0zJo1vTDBPs@ep-withered-voice-aiuftbv8-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

def upload_data():
    file_path = 'cleaned_students.csv'
    df = pd.read_csv(file_path)

    # Final safety cleanup
    df['rollno'] = df['rollno'].astype(str).str.strip().str.upper()
    df = df.drop_duplicates(subset=['rollno'], keep='last')

    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO students (name, rollno, feedback, img, rating)
        VALUES (%s, %s, %s, %s, %s)
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
            (row['name'], row['rollno'], row['feedback'], image_path, row['rating']) # Now saving the path
        )

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✓ {len(df)} records uploaded successfully!")

if __name__ == "__main__":
    upload_data()

