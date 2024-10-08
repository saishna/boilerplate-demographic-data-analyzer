import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 
        'marital-status', 'occupation', 'relationship', 'race', 
        'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 
        'native-country', 'salary'
    ])

    # Convert age and hours-per-week to numeric in case of string issues
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['hours-per-week'] = pd.to_numeric(df['hours-per-week'], errors='coerce')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Advanced education: Bachelors, Masters, or Doctorate
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # Percentage of people with advanced education earning >50K
    higher_education_rich = round((df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0]) * 100, 1)

    # Percentage of people without advanced education earning >50K
    lower_education_rich = round((df[~advanced_education & (df['salary'] == '>50K')].shape[0] / df[~advanced_education].shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # Number of people who work the minimum number of hours per week
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    # Percentage of these people earning >50K
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # Country with the highest percentage of people that earn >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()

    highest_earning_country = (country_salary / country_total).idxmax()
    highest_earning_country_percentage = round((country_salary / country_total).max() * 100, 1)

    # Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
