import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned healthcare dataset
input_file = "data/cleaned_healthcare_data.csv"
df = pd.read_csv(input_file)

# Convert Visit_Date to datetime
df["Visit_Date"] = pd.to_datetime(df["Visit_Date"])

print("Healthcare Dataset Shape:", df.shape)

# -----------------------------
# Basic Statistical Analysis
# -----------------------------

print("\nAverage Age:", round(df["Age"].mean(), 2))
print("Average Waiting Time:", round(df["Waiting_Time"].mean(), 2))
print("Total Patients:", df["Patient_ID"].nunique())

print("\nAdmission Status:")
print(df["Admission_Status"].value_counts())

print("\nDischarge Status:")
print(df["Discharge_Status"].value_counts())

# -----------------------------
# 1. Department-wise Patients
# -----------------------------

department_count = df["Department"].value_counts()

print("\nDepartment-wise Patient Count:")
print(department_count)

plt.figure(figsize=(8, 5))
department_count.plot(kind="bar")
plt.title("Department-wise Patient Count")
plt.xlabel("Department")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("department_patient_count.png")
plt.close()

# -----------------------------
# 2. Doctor-wise Patients
# -----------------------------

doctor_count = df["Doctor"].value_counts()

print("\nDoctor-wise Patient Count:")
print(doctor_count)

plt.figure(figsize=(8, 5))
doctor_count.plot(kind="bar")
plt.title("Doctor-wise Patient Count")
plt.xlabel("Doctor")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("doctor_patient_count.png")
plt.close()

# -----------------------------
# 3. Gender Distribution
# -----------------------------

gender_count = df["Gender"].value_counts()

print("\nGender Distribution:")
print(gender_count)

plt.figure(figsize=(6, 6))
gender_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("gender_distribution.png")
plt.close()

# -----------------------------
# 4. Severity Level Analysis
# -----------------------------

severity_count = df["Severity_Level"].value_counts()

print("\nSeverity Level Distribution:")
print(severity_count)

plt.figure(figsize=(7, 5))
severity_count.plot(kind="bar")
plt.title("Severity Level Distribution")
plt.xlabel("Severity Level")
plt.ylabel("Number of Patients")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("severity_level_distribution.png")
plt.close()

# -----------------------------
# 5. Monthly Patient Trend
# -----------------------------

monthly_patients = df.groupby(
    df["Visit_Date"].dt.to_period("M")
).size()

print("\nMonthly Patient Trend:")
print(monthly_patients)

plt.figure(figsize=(9, 5))
monthly_patients.plot(kind="line", marker="o")
plt.title("Monthly Patient Trend")
plt.xlabel("Month")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_patient_trend.png")
plt.close()

# -----------------------------
# 6. Age Group Analysis
# -----------------------------

bins = [0, 18, 35, 50, 65, 120]
labels = ["0-18", "19-35", "36-50", "51-65", "66+"]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

age_group_count = df["Age_Group"].value_counts().sort_index()

print("\nAge Group Distribution:")
print(age_group_count)

plt.figure(figsize=(8, 5))
age_group_count.plot(kind="bar")
plt.title("Age Group Analysis")
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("age_group_analysis.png")
plt.close()

# -----------------------------
# 7. Waiting Time Analysis
# -----------------------------

print("\nWaiting Time Statistics:")
print(df["Waiting_Time"].describe())

# -----------------------------
# 8. Admission Analysis
# -----------------------------

admission_count = df["Admission_Status"].value_counts()

plt.figure(figsize=(6, 5))
admission_count.plot(kind="bar")
plt.title("Admission Status")
plt.xlabel("Admission Status")
plt.ylabel("Number of Patients")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("admission_status.png")
plt.close()

# -----------------------------
# 9. Discharge Analysis
# -----------------------------

discharge_count = df["Discharge_Status"].value_counts()

plt.figure(figsize=(6, 5))
discharge_count.plot(kind="bar")
plt.title("Discharge Status")
plt.xlabel("Discharge Status")
plt.ylabel("Number of Patients")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("discharge_status.png")
plt.close()

print("\nEDA completed successfully.")
print("All analysis charts have been generated.")