import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult-data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    df_men = df[df['sex'] == 'Male']
    average_age_men = df_men['age'].mean(numeric_only=True).__round__(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = ((df['education'] == 'Bachelors').sum() / df['education'].count())*100
    percentage_bachelors = percentage_bachelors.__round__(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    lista = ['Bachelors','Masters','Doctorate']
    higher_education = df[df['education'].isin(lista)]['education'].count()
    lower_education = df[~df['education'].isin(lista)]['education'].count()
    # percentage with salary >50K
    higher_education_rich = (sum(df[df['education'].isin(lista)]['salary'].values == '>50K') / higher_education) * 100
    higher_education_rich = higher_education_rich.__round__(1)
    lower_education_rich = (sum(df[~df['education'].isin(lista)]['salary'].values == '>50K') / lower_education) * 100
    lower_education_rich = lower_education_rich.__round__(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = sum(df['hours-per-week'] == 1)
    rich_percentage = (sum(df[df['hours-per-week'] == 1]['salary'].values == '>50K') / num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    # Filtrar filas donde el salario es '>50K'
    df_gt_50k = df[df['salary'] == '>50K']

    # Contar el número total de personas por país
    total_por_pais = df['native-country'].value_counts()

    # Contar el número de personas que ganan más de 50K por país
    gt_50k_por_pais = df_gt_50k['native-country'].value_counts()

    # Calcular el porcentaje de personas que ganan más de 50K en cada país
    porcentaje_gt_50k_por_pais = (gt_50k_por_pais / total_por_pais) * 100
    highest_earning_country = porcentaje_gt_50k_por_pais.idxmax()
    highest_earning_country_percentage = porcentaje_gt_50k_por_pais.max().round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    # Filtrar filas donde el salario es '>50K' y el país es 'India'
    df_gt_50k_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]

    # Contar las ocurrencias de cada ocupación
    top_IN_occupation = df_gt_50k_india['occupation'].value_counts().idxmax()

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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
    
s = calculate_demographic_data()
s