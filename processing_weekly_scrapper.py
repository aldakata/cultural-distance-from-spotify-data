import bs4
import os
import pandas as pd

from datetime import datetime, timedelta


source_dir = "/home/aldakata/Projects/Tuebingen/Data Literacy/project/spotify_data/"
source_file = "global_2023-01-05.html"


def chart_scraper(source_dir, source_file):
    """Function to extract data from the html files"""
    with open(f"{source_dir}/{source_file}", "r") as input_file:
        data = input_file.read()
    # Turn the content into soup
    soup = bs4.BeautifulSoup(data, features="html.parser")

    # Find all the rows in the html
    rows = soup.findAll("tr")

    week_df = pd.DataFrame(
        columns=["week_start", "spotify_url", "song", "artist", "streams", "country"]
    )

    # Iterate through each row and identify pieces of data based on the tags. Note we start at index [1] here as the
    # first row is a link to an explanation link which we don't need

    for row in rows[1:]:
        row_data = {"spotify_url": row.find("a", href=True)["href"]}

        week_start = source_file.split(".")[0].split("_")[-1]
        row_data["week_start"] = week_start
        week_start.split("-")
        # week_end = datetime(day=, month=1, year=2023) + timedelta(days=7)

        # row_data["week_end"] = week_end

        row_data["song"] = row.find_all("strong")[0].text

        row_data["artist"] = row.find_all("span")[0].text.replace("by ", "")

        row_data["streams"] = int(
            row.find("td", attrs={"class": "chart-table-streams"}).text.replace(",", "")
        )

        # Save the dictionary to the dataframe
        week_df = week_df.append(row_data, ignore_index=True)

    return week_df
    # Save everything to an excel file
    # df.to_excel("spotify_sa_charts.xlsx", engine="openpyxl")


source_files = os.listdir("sources")
# Create a dataframe to hold all the extracted data
spotify_sa_df = pd.DataFrame(
    columns=["week_start", "spotify_url", "song", "artist", "streams"]
)

for f in source_files:
    print(f)
    spotify_sa_df = spotify_sa_df.append(chart_scraper(f))
spotify_sa_df.to_excel("spotify_sa_chart.xlsx", engine="openpyxl")
