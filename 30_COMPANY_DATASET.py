import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("company_dataset (2).csv")

# -------- Data Cleaning --------
def convert_reviews(x):
    x = str(x).lower().replace('(', '').replace(')', '').split()[0]
    return float(x.replace('k',''))*1000 if 'k' in x else float(x)

def convert_employees(x):
    x = str(x).lower()
    if 'lakh' in x:
        return 100000
    elif 'k' in x:
        return 10000
    return None

df['reviews_num'] = df['review_count'].apply(convert_reviews)
df['years_num'] = df['years'].str.extract('(\d+)').astype(int)
df['employees_num'] = df['employees'].apply(convert_employees)
df['hq_clean'] = df['hq'].str.replace(r'^\d+\s*years\s*old\s*', '', regex=True)

# -------- 1. Pie Chart (Employees) --------
top_emp = df.head(10)
plt.figure(figsize=(6,6))
plt.pie(top_emp['employees_num'], labels=top_emp['name'], autopct='%1.1f%%')
plt.title("Employee Distribution (Top 10)")
plt.show()

# -------- 2. Funnel Chart (Reviews) --------
funnel_df = df.sort_values(by='reviews_num', ascending=False).head(10)
plt.figure(figsize=(7,5))
plt.barh(funnel_df['name'], funnel_df['reviews_num'])
plt.gca().invert_yaxis()
plt.title("Funnel Chart - Reviews")
plt.xlabel("Reviews")
plt.show()

# -------- 3. HQ (Top 10) --------
print("\nTop 10 Company Headquarters:\n")
print(df[['name','hq_clean']].head(10).to_string(index=False))

# -------- 4. Bar Chart (Ratings) --------
top_rating = df.sort_values(by='ratings', ascending=False).head(10)
plt.figure(figsize=(8,5))
plt.bar(top_rating['name'], top_rating['ratings'])
plt.xticks(rotation=45)
plt.title("Top Ratings")
plt.ylabel("Rating")
plt.show()

# -------- 5. Line Chart (Years) --------
years_df = df.sort_values(by='years_num')
plt.figure(figsize=(9,5))
plt.plot(years_df['name'], years_df['years_num'], marker='o')
plt.xticks(rotation=90)
plt.title("Company Age (Years)")
plt.ylabel("Years")
plt.grid()
plt.show()
