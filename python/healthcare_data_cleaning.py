import pandas as pd

# Load healthcare dataset
input_file = "../data/healthcare_emergency_room_data.csv"
output_file = "../data/cleaned_healthcare_data.csv"

df = pd.read_csv(input_file)

print("Original Dataset Shape:", df.shape)

# Display basic information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Convert Visit_Date to date format
df["Visit_Date"] = pd.to_datetime(df["Visit_Date"], errors="coerce")

# Remove rows with missing important values
df = df.dropna()

# Validate waiting time
df = df[df["Waiting_Time"] >= 0]

# Validate age
df = df[(df["Age"] >= 0) & (df["Age"] <= 120)]

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("\nCleaning completed successfully.")
print("Cleaned Dataset Shape:", df.shape)
print("Cleaned file saved at:", output_file)