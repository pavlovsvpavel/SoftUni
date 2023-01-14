period = int(input())

treated_patients = 0
untreated_patients = 0
doctors = 7
for i in range(1, period + 1):
    patients = int(input())
    if i % 3 == 0:
        if untreated_patients > treated_patients:
            doctors = doctors + 1
        if patients <= doctors:
            treated_patients += patients
        elif patients > doctors:
            treated_patients += doctors
            untreated_patients = untreated_patients + (patients - doctors)
    else:
        if patients <= doctors:
            treated_patients += patients
        elif patients > doctors:
            treated_patients += doctors
            untreated_patients = untreated_patients + (patients - doctors)

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
