import pandas as pd
import random
from datetime import datetime, timedelta

# Define study groups and programs
study_groups = [
    {"program": "Assistant Pharmacist", "group": "AP2020-2", "matriculation": "01.09.2020", "duration": 3, "ehis": 214475, "level": "514 rakenduskõrgharidusõpe", "dept": "Meditsiinitehnilise hariduse keskus"},
    # Add all 54 groups similarly...
]

# Initialize dataset
data = []
student_id = 1

# Generate 7 students per group
for group in study_groups:
    for _ in range(7):
        row = {}
        row["Matrikli number"] = f"S{student_id}"
        row["Sugu"] = random.choices(["Naine", "Mees"], weights=[0.75, 0.25])[0]
        row["Külalisõppija"] = random.choices(["Ei", "Jah"], weights=[0.9, 0.1])[0]
        row["Välisõppija"] = random.choices(["Ei", "Jah"], weights=[0.9, 0.1])[0]
        # Add other fields with similar logic...
        data.append(row)
        student_id += 1

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv("dummy_dataset.csv", index=False)