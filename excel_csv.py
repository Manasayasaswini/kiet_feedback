import pandas as pd
import subprocess

def clean_and_prepare_data(file_path):
    # Read the Excel file (first sheet)
    df = pd.read_excel(file_path, sheet_name=0)

    # Map columns
    column_mapping = {
        'Full Name': 'name',
        'Roll Number': 'rollno',
        'Your overall experience with the Bootcamp. ( minimum 2 sentences)': 'feedback'
    }
    df = df[list(column_mapping.keys())].rename(columns=column_mapping)

    # Cleanup
    df['rollno'] = df['rollno'].astype(str).str.strip().str.upper()
    df['feedback'] = df['feedback'].astype(str).str.replace('\n', ' ').str.strip()

    # Deduplicate
    df = df.drop_duplicates(subset=['rollno'], keep='last')

    # Image path
    df['img'] = df['rollno'].apply(lambda x: f"images/{x}.jpg")

    # Save
    df.to_csv('cleaned_students.csv', index=False)
    print(f"✓ Cleaned {len(df)} unique student records.")

    # Call upload_to_db.py automatically
    print("→ Uploading cleaned data to database...")
    subprocess.run(["python", "upload_to_db.py"], check=True)

if __name__ == "__main__":
    filename = 'KIET_feedback.xlsx'
    clean_and_prepare_data(filename)
