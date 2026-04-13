import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("Top_30_US_Tech_Companies_2022-2023.csv")


data = data.sort_values(by='Annual Revenue 2022-2023 (USD in Billions)', ascending=False)

top10 = data.head(10)
x = top10['Company Name']
y = top10['Annual Revenue 2022-2023 (USD in Billions)']


plt.figure(figsize=(10,6))
plt.barh(x, y, color='skyblue')
plt.xlabel("Annual Revenue (USD in Billions)")
plt.ylabel("Company Name")
plt.title("Bar Chart of Top 10 Companies by Revenue")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.gca().invert_yaxis()


for i, v in enumerate(y):
    plt.text(v, i, f" {v}", va='center')

plt.show()



plt.figure(figsize=(10,6))
plt.step(x, y, where='mid', color='green')
plt.xlabel("Company Name")
plt.ylabel("Annual Revenue (USD in Billions)")
plt.title("Stair Chart of Revenue")
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10,6))
plt.plot(x, y, marker='o', color='red')
plt.xlabel("Company Name")
plt.ylabel("Annual Revenue (USD in Billions)")
plt.title("Line Chart of Revenue")
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()




top5 = data.head(5)
others = data.iloc[5:]
others_sum = others['Annual Revenue 2022-2023 (USD in Billions)'].sum()

labels = list(top5['Company Name']) + ['Others']
sizes = list(top5['Annual Revenue 2022-2023 (USD in Billions)']) + [others_sum]

plt.figure(figsize=(7,7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Revenue Share (Top 5 + Others)")
plt.axis('equal')

plt.show()


plt.figure(figsize=(10,6))
plt.hist(data['Annual Revenue 2022-2023 (USD in Billions)'], bins=10, color='purple')
plt.xlabel("Annual Revenue (USD in Billions)")
plt.ylabel("Number of Companies")
plt.title("Histogram of Revenue Distribution")
plt.grid(True, linestyle='--', alpha=0.7)
plt.subplots_adjust(bottom=0.3)
plt.tight_layout()
plt.show()