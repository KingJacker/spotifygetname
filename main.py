import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get("https://duckduckgo.com");
search_box = driver.find_element_by_name('q')
search_box.send_keys('5gPfWWQrehelkcNTuU1ph2')
search_box.submit()
#driver.quit()
link = driver.find_element_by_partial_link_text("Spotify")
name = link.get_attribute('innerHTML')
print(name)
