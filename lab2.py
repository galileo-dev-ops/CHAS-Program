import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Name": ["Bai Yun", "Bao Bao", "Da Mao", "Gu Gu", "He Hua", "Jiao Qing", "Lun Lun", "Mei Lan"],
    "Age (in years)": [32, 10, 15, 24, 3, 13, 26, 17],
    "Monday": [30, 12, 18, 21, 8, 20, 30, 28],
    "Tuesday": [35, 11, 20, 20, 12, 14, 31, 26],
    "Wednesday": [32, 15, 16, 25, 9, 19, 27, 24],
    "Thursday": [30, 18, 17, 27, 7, 20, 29, 23],
    "Friday": [35, 13, 16, 22, 10, 15, 30, 29],
    "Saturday": [30, 12, 16, 20, 11, 18, 28, 22],
    "Sunday": [38, 12, 19, 24, 7, 17, 29, 24],
}

df = pd.DataFrame(data)

df['Average'] = df[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']].mean(axis=1)

df = df.sort_values(by=['Age (in years)', 'Average'], ascending=True)

pandas_eating_more_than_28kg = df[df['Average'] > 28]

print(pandas_eating_more_than_28kg['Name'])

print(df)

np.polynomial.polynomial.polyfit(df['Age (in years)'], df['Average'], 1)

plt.scatter(df['Age (in years)'], df['Average'], marker='o', color='b')
plt.xlabel('Age (in years)')
plt.ylabel('Average Bamboo Eaten (kg)')
plt.title('Average Bamboo Eaten vs. Age of Pandas')
plt.grid(True)


