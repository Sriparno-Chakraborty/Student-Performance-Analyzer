
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = []

try:
    f = open('students.csv', 'r')

    for line in f:
        line = line.strip()

        if line == "":
            continue

        p = line.split(',')

        name = p[0]

        # Skip CSV header
        if name == "Name":
            continue

        if len(p) != 4:
            print("Invalid row. Row skipped.")
            continue

        try:
            m = float(p[1])
            ph = float(p[2])
            c = float(p[3])

        except ValueError:

            try:
                float(p[1])
            except ValueError:
                print(f"Invalid marks for {name} in Maths: '{p[1]}'. Row skipped.")
                continue

            try:
                float(p[2])
            except ValueError:
                print(f"Invalid marks for {name} in Physics: '{p[2]}'. Row skipped.")
                continue

            try:
                float(p[3])
            except ValueError:
                print(f"Invalid marks for {name} in Chemistry: '{p[3]}'. Row skipped.")
                continue

        if not 0 <=m <=100:
            print(f"Invalid marks for {name} in Maths. Row skipped.")
            continue

        if not 0 <= ph <=100:
            print(f"Invalid marks for {name} in Physics. Row skipped.")
            continue

        if not 0 <= c <= 100:
            print(f"Invalid marks for {name} in Chemistry. Row skipped.")
            continue

        data.append([name, m, ph, c])

    f.close()

except FileNotFoundError:
    print("File not found!")

df = pd.DataFrame(data, columns=['Name', 'Maths', 'Physics', 'Chemistry'])

if len(df) == 0:
    pass

else:

    # Calculate total and percentage
    df['Total'] = df['Maths'] + df['Physics'] + df['Chemistry']

    df['Percentage'] = (df['Total'] / 300) * 100

    # Calculate grades
    grades = []

    for per in df['Percentage']:

        if per >= 90:
            grades.append('A')

        elif per >= 75:
            grades.append('B')

        elif per >= 60:
            grades.append('C')

        elif per >= 40:
            grades.append('D')

        else:
            grades.append('F')

    df['Grade'] = grades

    # Menu
    while True:

        print("\n--- MENU ---")
        print("1. Result")
        print("2. Statistics")
        print("3. Exit")

        ch = input("Enter your choice: ")

        if ch == '1':

            print("\nStudent Results")

            for i in range(len(df)):

                print(f"{df.loc[i, 'Name']} | {df.loc[i, 'Total']:.2f} | {df.loc[i, 'Percentage']:.2f}% | {df.loc[i, 'Grade']}")

        elif ch == '2':

            # Class statistics
            per_arr = df['Percentage'].values

            print(f"Mean %: {np.mean(per_arr):.2f} | Median %: {np.median(per_arr):.2f} | Std Dev: {np.std(per_arr):.2f}")

            # Find topper
            top = df['Percentage'].idxmax()

            print(f"Topper: {df.loc[top, 'Name']} ({df.loc[top, 'Percentage']:.2f}%)")

            # Subject averages
            print(f"Subject averages: Maths {df['Maths'].mean():.2f}, Physics {df['Physics'].mean():.2f}, Chemistry {df['Chemistry'].mean():.2f}")

            # Bar chart
            plt.figure(figsize=(10, 4))

            plt.subplot(1, 2, 1)

            plt.bar(df['Name'], df['Percentage'])
            plt.title('Student Percentages')
            plt.xlabel('Students')
            plt.ylabel('Percentage')

            # Histogram
            plt.subplot(1, 2, 2)

            all_m = pd.concat([df['Maths'], df['Physics'], df['Chemistry']])

            plt.hist(all_m, bins=5, edgecolor='black', linewidth=1.5)
            plt.title('Marks Histogram')
            plt.xlabel('Marks')
            plt.ylabel('Frequency')

            plt.tight_layout()

            plt.show()

        elif ch == '3':

            print("Thank you!")
            break

        else:
            print("Invalid choice!")
