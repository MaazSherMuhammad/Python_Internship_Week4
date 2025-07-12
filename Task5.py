from datetime import datetime

#get user's birth date as input
birth_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_input, "%Y-%m-%d")

#get today's date
today = datetime.today()

#calculate age in years
age_years = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age_years -= 1

#calculate total days
days_lived = (today - birth_date).days

print(f"You are {age_years} years old.")
print(f"You have lived for {days_lived} days.")
