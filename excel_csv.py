import pandas as pd

def clean_and_prepare_data(file_path):
    # Read the Excel file directly (using the first sheet)
    # Ensure you have 'openpyxl' installed
    df = pd.read_excel(file_path)

    # ... rest of the code remains the same ...
    column_mapping = {
        'Full Name': 'name',
        'Roll Number': 'rollno',
        'Your overall experience with the Bootcamp. ( minimum 2 sentences)': 'feedback'
    }
    
    df = df[list(column_mapping.keys())].rename(columns=column_mapping)
    df = df.drop_duplicates(subset=['rollno'], keep='last')
    df['img'] = df['rollno'].apply(lambda x: f"/images/{x}.jpg")
    df.to_csv('cleaned_students.csv', index=False)
    print(f"✓ Cleaned {len(df)} unique student records.")

if __name__ == "__main__":
    # Update this with your exact Excel filename
    filename = 'KIET First Year Engineering Bootcamp Feedback (Feb 7th & 8th, 2026) (Responses) (1) (1).xlsx'
    clean_and_prepare_data(filename)
