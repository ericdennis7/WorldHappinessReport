<h1>The World Happiness Report</h1>

<h2>ℹ️ Information About the Study</h2>
<h3>Dataset and Project Information</h3>

Original Dataset Link: <a href = "https://www.kaggle.com/code/mayzannilarthein44/world-happiness-report-data-cleaning">World Happiness Report Cleaned Data 2015-2021</a>

Software/Tools Being Used:
- Python (Pandas)
- PowerBI

<h2>🔍 The Process</h2>
<b>PowerBI Dashboard:</b> <a href="https://app.powerbi.com/view?r=eyJrIjoiNTcyYjY4Y2ItMDgzMS00MjAwLWEyMjYtNzhhYWIzNDdkZjE1IiwidCI6ImU0YTdiMmYwLTRkM2QtNDI0OC05YTdiLWEyNjQ4ZTIzN2MxNSIsImMiOjF9&pageName=ReportSectionc1b182ee40bc969bbaba">The World Happiness Report (Power BI)</a>
<h3>Obtaining and Cleaning the Data</h3>

To start my analysis, I obtained a World Happiness Report dataset from <a href="https://www.kaggle.com/code/mayzannilarthein44/world-happiness-report-data-cleaning">Kaggle</a> which had already undergone some data cleaning. However, I decided to further refine the data by developing a <a href="HappinessReportDataCleaning.py">Python script</a> that leverages pandas to analyze each year and column, and rank each country according to its position in that year and column. With the data now clean and ranked, I moved on to creating an intuitive Power BI dashboard to visually represent my findings.

<h3>Power BI Report Creation</h3>

For my report, I carefully crafted three pages that each offer a unique perspective on the data. The first page provides a year-by-year breakdown of the world's happiest country, while the second page displays a happiness report map that showcases the happiness levels of different countries. The third page allows users to compare countries and explore the data in greater detail.

To make the report dynamic, I used various DAX measures that allow for the title to change based on the year and country selected by the user. Additionally, I imported a custom .json map that enhances the report's aesthetics, automatically zooming in on the country selected and displaying a tooltip of relevant information.

In order to ensure consistency across all pages, I connected all slicers so that any changes made by the user are properly reflected on each page. Lastly, I added flags from an image URL website to provide users with even more information about each country. This was achieved by using Power Query to automatically add a prefix and suffix to each row.

Overall, this project was an incredibly enriching learning experience. Please refer to the images below for a closer look at the Power BI report.

<h3>Conclusion</h3>

According to the data, Finland is the happiest country in the world and has been for the previous 4 years in a row (2018-2021).

<h3>Power BI Report Images</h3>

World Happiness Report: Happiest Country Per Year:

![Happiest Country Per Year](https://user-images.githubusercontent.com/130507070/235213154-d88a9c24-a7c6-49e3-b454-c5ab8bd95b36.png)

World Happiness Report: World Map Overview:

![World Map Overview](https://user-images.githubusercontent.com/130507070/235213371-ab3b06f3-6fb4-4fc9-b990-1f53353a192e.png)

World Happiness Report: Country vs. Country:

![Country vs  Country](https://user-images.githubusercontent.com/130507070/235213620-ec24152d-1391-45de-8b9a-8c9c287575ff.png)

<h2>📱 Contact Information</h2>

<b>LinkedIn Profile:</b> <a href="https://www.linkedin.com/in/ericdennis7/">ericdennis7</a>

