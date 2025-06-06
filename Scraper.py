from selenium import webdriver
from selenium.webdriver.common.by import By
import time

keyword = input("請輸入搜尋關鍵字：")
driver = webdriver.Chrome()
driver.get(f"https://search.books.com.tw/search/query/key/{keyword}/cat/all")
time.sleep(3)  
books = driver.find_elements(By.CSS_SELECTOR, "div.table-td")[:3]
for book in books:
    try:
        title_element = book.find_element(By.CSS_SELECTOR, "h4 a")
        title = title_element.text.strip()
        link = title_element.get_attribute("href")
        print("書名：", title)
        print("連結：", link)
    except Exception as e:
        print("找不到相關書籍：", e)
driver.quit()