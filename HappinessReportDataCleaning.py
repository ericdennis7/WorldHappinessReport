#Eric Dennis
#Last Updated: 2023
#Purpose: Cleaning and giving ranks to the World Happiness Report Data per year.

#Imports
import pandas as pd

#Load the data from the CSV file
data = pd.read_csv("C:\\Users\\ericd\\Desktop\\world-happiness-report-2015-2022-cleaned.csv")

#Define a list of the columns that we want to rank
rank_cols = ["Economy (GDP per Capita)", "Family (Social Support)", "Health (Life Expectancy)",
             "Freedom", "Generosity", "Trust (Government Corruption)"]

#Loop through each year in the dataset
for year in data["Year"].unique():

    #Create a subset of the data for the current year
    year_data = data[data["Year"] == year].copy()

    #Loop through each of the columns we want to rank
    for col in rank_cols:

        #Calculate the rank for the current column
        rank = year_data[col].rank(method="min", ascending=False)

        #Add the rank as a new column to the subset of data for the current year
        year_data[f"{col} Rank"] = rank.astype(int)

    #Update the original dataset with the new rankings for the current year
    data.loc[data["Year"] == year, year_data.columns] = year_data

#Save the updated dataset to a new CSV file
data.to_csv("C:\\Users\\ericd\\Desktop\\world-happiness-report-2015-2022-ranked.csv", index=False)
