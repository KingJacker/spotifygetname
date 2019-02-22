from selenium import webdriver
import csv

p = []
errorcount = 0

def get_list():
    id_list = []
    with open('list.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            id_list.append(row)

    for i in range(0,len(id_list)):

        t = id_list[i][0].split("/")
        p.append(t[4])
    return p

def getname(id):
    search_box = driver.find_element_by_name('q')
    search_box.clear()
    search_box.send_keys(id)
    search_box.submit()
    try:
        link = driver.find_element_by_partial_link_text(", a song by ")
        inner = link.get_attribute('innerHTML')
        return inner
    except:
        return

get_list()

driver = webdriver.Chrome("C:/Users/Dan/AppData/Local/Programs/Python/Python36/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe")  # Optional argument, if not specified will search path.
driver.get("https://duckduckgo.com");

text_file = open("Songs.txt","w")

for i in range(0, len(p)):
    uncut = getname(p[i])
    try:
        song = uncut.split(", a song by ")[0]
        artist = uncut.split(", a song by ")[1].split(" on Spotify")[0]
        print(f"{artist} - {song}")
        text_file.write(f"{artist} - {song}\n")
    except:
        print("Error")
        errorcount += 1

text_file.write(f"Errors: {errorcount}")
text_file.close()
driver.quit()
