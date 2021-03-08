## [Der PARITÄTISCHE Hessen](https://www.paritaet-hessen.org/ueber-uns/unsere-mitglieder.html) (*eng*)

The client needs csv file with the following columns:  
| Name | Street | House number | Zip code | City | Phone | Email | Website |
|:----:|:------:|:------------:|:-----------:|:----:|:-----:|:------:|:-------:|
... | ... | ... | ...| ...| ...| ...| ...

### We need to get data (img_1):
![img](https://github.com/PyWebChannel/Shadow/blob/master/paritaet-hessen/img/get_data.png "img_1")

## Input data:
Website --> [paritaet-hessen.org](https://www.paritaet-hessen.org/ueber-uns/unsere-mitglieder.html)  
Script Requirements (python3 (ver.3.8)):
* csv
* logging 
* re 
* time 
* BeautifulSoup
* selenium

## Output data:
![img](https://github.com/PyWebChannel/Shadow/blob/master/paritaet-hessen/img/output_data.png "excel table")

**Output files:**
- list_of_companies.csv
- list_of_companies.xlsx

📌 **NOTE:** [WebDriver.py](WebDriver.py) gets the instance of specified web driver (Firefox, Chrome - *default*, PhantomJS).

## Парсим сайт [paritaet-hessen.org](https://www.paritaet-hessen.org/ueber-uns/unsere-mitglieder.html) (*rus*)
Необходимо извлечь: имя компании, улицу, номер дома, индекс, город, номер тел., адрес эл.почты, ссылку на вебсайт компании.  
Наглядный пример [необходимых данных](#we-need-to-get-data-img_1) и [итоговый результат](#output-data) представлены выше.
