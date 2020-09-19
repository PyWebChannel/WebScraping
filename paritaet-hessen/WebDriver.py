#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 2020
@author: Kir (pyweb.channel@gmail.com | pyweb.channel@gmail.com)
Python Web Scraper: [Der PARITÄTISCHE Hessen](https://www.paritaet-hessen.org/ueber-uns/unsere-mitglieder.html)
Script Requirements: Python3 (ver.3.8), selenium

This class gets the instance of specified web driver.
"""

from selenium import webdriver


class WebDriver:

	def __init__(self, drivername):

		if drivername == "firefox":
			self.driver = webdriver.Firefox()
		elif drivername == "chrome":
			options = webdriver.ChromeOptions()
			options.add_argument("headless")
			self.driver = webdriver.Chrome(chrome_options=options)
		elif drivername == "phantomjs":
			self.driver = webdriver.PhantomJS()

		elif drivername not in ["firefox", "chrome", "phantomjs"]:
			print("Default driver selected - Chrome")
			options = webdriver.ChromeOptions()
			options.add_argument("headless")
			self.driver = webdriver.Chrome(chrome_options=options)
