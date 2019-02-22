from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Dan/AppData/Local/Programs/Python/Python36/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe")  # Optional argument, if not specified will search path.
links = [["https://open.spotify.com/track/4DMKwE2E2iYDKY01C335Uw"],["https://open.spotify.com/track/2WOjLF83vqjit2Zh4B69V3"]]
driver.get(links[1][0])
