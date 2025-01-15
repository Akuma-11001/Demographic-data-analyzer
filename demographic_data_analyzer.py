#Demographic-Data-Analyzer

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





#import data
df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/refs/heads/main/adult.data.csv")


def calculate_demographic_data(print_data=True):
    race_count = df.groupby(df["race"]).size()

    men = df.loc[:,("sex", "age")]
    men = men[men["sex"] == "Male"]
    average_age_men = men["age"].mean()
    average_age_men = average_age_men.astype(int)


    bachelors = df["education"]
    percentage_bachelors = (bachelors[(bachelors == "Bachelors")].count()) / bachelors.count()
    percentage_bachelors = round(percentage_bachelors *100, 2)


    education = df.loc[:,("education","salary")]
    adv_education = education[(education["education"] == "Bachelors") | (education["education"] == "Masters") | (education["education"] == "Doctorate")]
    no_adv_education = education[~((education["education"] == "Bachelors") | (education["education"] == "Masters") | (education["education"] == "Doctorate"))]

    higher_education = adv_education.count()
    higher_education = higher_education["education"]
    lower_education = no_adv_education.count()
    lower_education = lower_education["education"]


    over_adv_education = adv_education[(adv_education["salary"] == ">50K")]
    over_no_adv_education = no_adv_education[(no_adv_education["salary"] == ">50K")]

    higher_education_rich = (over_adv_education.count() / adv_education.count())*100
    higher_education_rich = round(higher_education_rich["education"], 2)
    lower_education_rich = round((over_no_adv_education.count() / no_adv_education.count())*100, 2)
    lower_education_rich = lower_education_rich["education"]


    hours_per_week = df["hours-per-week"]
    minimum_hours =  hours_per_week.min()


    workers = df.loc[:, ["hours-per-week","salary"]]
    rich_workers = workers[workers["salary"] == ">50K"]
    num_min_workers = len(rich_workers)


    rich_percentage = round(num_min_workers / len(workers)*100, 2)


    country = df.loc[:, ["native-country", "salary"]]
    country = country[country["native-country"] != "?"]
    country = country[country["salary"] == ">50K"]
    country2 = country[country["native-country"] == "United-States"]
    us_amount = len(country2)
    highest_earning_country = country.describe()
    highest_earning_country_percentage = (us_amount / num_min_workers)*100
    highest_earning_country_percentage = round(highest_earning_country_percentage, 2)

    india = df.loc[:, ["occupation","native-country", "salary"]]
    india = india[india["native-country"] != "?"]
    india = india[india["salary"] == ">50K"]
    india = india[india["native-country"] == "India"]
    occupations = india["occupation"].value_counts()

    top_occupation_count = occupations.max()
    top_occupation_name = occupations.idxmax()

    top_IN_occupation = f"{top_occupation_name}: {top_occupation_count}"

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
