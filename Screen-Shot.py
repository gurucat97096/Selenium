from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://github.com/search?q=oauth2.0++language%3APython&type=repositories&l=Python/")
driver.save_screenshot("shot.png")        
driver.close()