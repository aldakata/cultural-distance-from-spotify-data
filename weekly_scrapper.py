from urllib.parse import uses_relative
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import confidential

import os

from datetime import datetime, timedelta

# from bushbaby import (
#     BushBaby,
# )
import time

target_dir = "/home/aldakata/Projects/Tuebingen/Data Literacy/project/spotify_data"
target_file = target_dir + "/{}_{}.html"
browser = webdriver.Chrome(
    executable_path=r"/home/aldakata/chromedriver_linux64/chromedriver"
)
browser.get(
    r"https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fcharts.spotify.com/login"
)

username = confidential.USERNAME
password = confidential.PASSWORD

user_in = browser.find_element("id", "login-username")
password_in = browser.find_element("id", "login-password")

user_in.clear()
user_in.send_keys(username)

password_in.clear()
password_in.send_keys(password)
password_in.send_keys(Keys.RETURN)


time.sleep(5)

week_start = datetime(
    day=12, month=1, year=2023
)  # must set this to the latest date which is always one day ahead of what is
# represented on the site
week_strings = []
for x in range(0, 52):
    week_start = week_start - timedelta(days=7)
    week_start_str = week_start.strftime("%Y-%m-%d")
    week_strings.append(week_start_str)

url = "https://charts.spotify.com/charts/view/regional-{}-weekly/{}"

countries = [
    # "global",  # DONE
    # "se",      # DONE
    # "us",      # DONE
    # "gb",      # DONE
    # "de",
    # "es",
    # "ie",
    # "ae",
    # "ar",
    # "at",
    # "au",
    # "be",
    # "bg",
    # "bo",
    # "br",
    # "ca",
    # "ch",
    # "cl",
    # "co",
    # "cr",
    # "cz",
    # "dk",
    # "do",
    # "ec",
    # "ee",
    # "eg",
    # "fi",
    # "gr",
    # "gt",
    "hk",
    # "hn",
    # "hu",
    "id",
    # "il",
    "in",
    "is",
    "th",
    "tr",
    "tw",
    "ru",
    "za",
    # "it",
    "jp",
    "kr",
    # "lt",
    # "lu",
    # "lv",
    "ma",
    "mx",
    "my",
    # "ni",
    # "nl",
    # "no",
    "nz",
    # "pa",
    # "pe",
    "ph",
    # "pl",
    "pt",
    # "py",
    # "ro",
    "sa",
    "sg",
    # "sk",
    # "sv",
    # "ua",
    # "uy",
    # "un",
    "fr",
]

for country in countries:
    for week in week_strings:
        scrape_url = url.format(country, week)
        print(f"COUNTRY : {country} WEEK : {week} URL : {scrape_url}")
        browser.get(scrape_url)
        time.sleep(5)
        with open(target_file.format(country, week), "w") as f:
            f.write(browser.page_source)
