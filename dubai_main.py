#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 2020
@author: Kir (kiril9ndi9@gmail.com | pyweb.channel@gmail.com)

Python Web Scraper:
[DUBAI CHAMBER](https://www.dubaichamber.com/resources/commercial-directory) -> next ->
"Click here to view the updated information of Dubai Chamber Members"

Script Requirements: Python3 (ver.3.6+), selenium, csv, logging, time

The client needs comma-separated csv files with the following columns:
Member Name, Email, Phone, Fax, URL, Product/Service, Product Description
"""

import csv
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level='ERROR', filename='log.txt', format='%(asctime)s - %(message)s')


class Bot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(30)

    def write_csv(self, data):
        with open("data.csv", 'a', encoding="utf-8") as f:
            writer = csv.writer(f)
            for item in data.values():
                writer.writerow((item["company_name"],
                                 item["email"],
                                 item["phone"],
                                 item["fax"],
                                 item["url"],
                                 item["product"],
                                 item["description"]))

    def get_data(self):
        try:
            self.driver.get("https://www.dubaichamber.com/resources/commercial-directory")
            self.driver.find_element_by_xpath("//div[@class='wpb_wrapper']").find_elements_by_tag_name("p")[-1].click()  # the landing page
            self.driver.switch_to.window(self.driver.window_handles[-1])  # switch to currently tab
            input_xpath = "//input[@aria-labelledby='Company_Name_Label']"
            # query = WebDriverWait(self.driver, 120).until(
            #                 EC.presence_of_element_located((By.XPATH, input_xpath)))  # explicit wait "input 'Company name'"
            # query.send_keys('a')
            # if WebDriverWait(self.driver, 130).until(lambda driver: query.get_attribute('value') == 'a'):
            #     self.driver.find_element_by_xpath("//span[contains(text(), 'Search')]").click()
            sleep(60)
            query = self.driver.find_element_by_xpath(input_xpath)
            sleep(5)
            query.send_keys('a')
            sleep(5)
            self.driver.find_element_by_xpath("//span[contains(text(), 'Search')]").click()
            sleep(5)

            c = 1
            while True:
                data = {}
                sleep(2)
                for row_num in range(1, 11):
                    sleep(1)
                    tds_data = self.driver.find_element_by_xpath(f"//tr[@id='{row_num}']").find_elements_by_tag_name("td")
                    company_name = tds_data[1].get_attribute('title').strip()
                    email = tds_data[2].text.strip()
                    phone = tds_data[3].text.strip()
                    fax = tds_data[4].text.strip()
                    url = tds_data[5].text.strip()
                    product = tds_data[6].text.strip()
                    description = tds_data[7].find_element_by_tag_name('div').text.strip()

                    data.update({row_num: {"company_name": company_name,
                                           "email": email,
                                           "phone": phone,
                                           "fax": fax,
                                           "url": url,
                                           "product": product,
                                           "description": description}})

                self.write_csv(data)
                print(f"step number {c} --> csv writing")
                self.driver.find_element_by_xpath(f"//span[@title='Next record set']").click()
                print("="*150)
                c += 1

        except Exception as e:
            print(f"Error: {e}")
            logging.error(f"Error: {e}")

        finally:
            sleep(5)
            self.driver.quit()
            print("Finish")


def main():
    b = Bot()
    b.get_data()


if __name__ == '__main__':
    main()
