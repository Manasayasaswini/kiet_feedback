import pandas as pd

# Load Excel file
df = pd.read_excel("KIET_feedback.xlsx")

# Show actual column names
print("Columns in Excel:", df.columns)

# Normalize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Keep only required columns (adjust if feedback column has a different name)
df = df[['id', 'name', 'roll_no', 'feedback']]

# Remove duplicates
df = df.drop_duplicates(subset=['roll_no'])

# Save as CSV
df.to_csv("cleaned_students.csv", index=False)
