## [Dubai Chamber](https://www.dubaichamber.com/resources/commercial-directory) (*eng*)

### The task:
<img src="https://github.com/PyWebChannel/Shadow/blob/master/dubaichamber/dubaichamber_task.png" alt="task" width="1200"/>
We need to get data:
| Name | Email | Phone | URL | Fax | Product/Service | Product |
|:----:|:------:|:------------:|:-----------:|:----:|:-----:|:------:|
column 1 | column 2 | column 3 | column 4 | column 5 | column 6 | column 7

## Input data:
Website --> [dubaichamber.com](https://www.dubaichamber.com/resources/commercial-directory)
Script Requirements (python3 (ver.3.8)):
* csv;
* logging; 
* selenium.

## Output data:
![img](https://github.com/PyWebChannel/Shadow/blob/master/dubaichamber/dubaichamber_OutputFile.png "excel table")

**Output files:**
- dubaichamber_OutputFile.csv
- dubaichamber_OutputFile.xlsx

📌 **NOTE:** The instance of the web driver being used - **chromedriver** (*default*)

## The example how the script works:

![gif](https://github.com/PyWebChannel/Shadow/blob/master/dubaichamber/dubaichamber.gif)


## Парсим сайт [dubaichamber.com](https://www.dubaichamber.com/resources/commercial-directory) (*rus*)
Необходимо извлечь: имя компании, адрес эл.почты, номер тел., номер факса, ссылку на вебсайт компании (url), продукт/услугу, описание продукта.  
Наглядный пример [необходимых данных](#user-content-the-task), [итоговый результат](#output-data) и [пример работы парсера](#user-content-the-example-how-the-script-works) представлены выше.
