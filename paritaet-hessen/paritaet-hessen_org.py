#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 2020
@author: Kir (kiril9ndi9@gmail.com | pyweb.channel@gmail.com)
Python Web Scraper: [Der PARITÄTISCHE Hessen](https://www.paritaet-hessen.org/ueber-uns/unsere-mitglieder.html)
Script Requirements: Python3 (ver.3.8), selenium, BeautifulSoup, csv, logging, re, time

The client needs comma-separated csv files with the following columns:
name, street, house number, postal code, city, phone, e-mail, website
"""

from WebDriver import WebDriver

import csv
import logging
import re
import time

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("paritaet_hessen") 

URL = "https://www.paritaet-hessen.org/ueber-uns/unsere-mitglieder.html"
HEADERS = (
    "Name",
    "Street",
    "House_number",
    "Zip_code",
    "City",
    "Tel",
    "Email",
    "Website",
)


def write_csv(data):
    with open("list_of_companies.csv", 'w', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        for item in data.values():
            writer.writerow( (item["name"],
                             item["street"],
                             item["house_number"],
                             item["zip_code"],
                             item["city"],
                             item["tel"],
                             item["email"],
                             item["website"]) )


def get_html(url, browser):
    try:
        # driver = webdriver.Firefox()
        # driver.maximize_window()
        browser.driver.get(url)
        time.sleep(5)
        html = browser.driver.page_source
        logger.info("Driver finished!")

        return html

    except WebDriverException as e:
        logger.info("Error: ", e)

    finally:
        browser.driver.quit()


def get_data(html):
    soup = bs(html, "lxml")
    data = {}
    pages_data = soup.find_all("div", class_="listview-item")
    for num, item in enumerate(pages_data, start=1):
        name = item.find("label", class_="mvname").text.replace("\n", " ")
        data_tag_p = item.find("p").text.strip().replace("\t", "").split("\n")

        # get the street and the house number
        address = data_tag_p[0]
        try:
            index = re.search(r"\d", address).start()
            street = address[:index - 1]
            house_number = address[index:]
        except:
            street = data_tag_p[0]
            house_number = ""

        # get zip code and city
        zip_code_city = data_tag_p[1]
        index_zip = re.search(r"\d+", zip_code_city).end()
        zip_code = zip_code_city[:index_zip]
        city = zip_code_city[index_zip + 1:]

        # get tel and email
        try:
            tel = "".join(re.findall(r"Tel\.:\s(.+)", item.find("p").text))
        except:
            tel = ""
        try:
            email = "".join(re.findall(r'E-Mail\.:\s(.+)', item.find('p').text))
        except:
            email = ""

        # get website
        try:
            website = item.find("a").get("href")
        except:
            website = ""

        # write data
        data.update({num: {"name": name,
                           "street": street,
                           "house_number": house_number,
                           "zip_code": zip_code,
                           "city": city,
                           "tel": tel,
                           "email": email,
                           "website": website}})

    logger.info("Data received!")
    return data


def main(url):
    browser = WebDriver(input("Enter Firefox, Chrome, PhantomJS or press 'Enter'").lower())
    write_csv(get_data(get_html(url, browser)))
    logger.info("Mission completed!")


if __name__ == "__main__":
    main(URL)
