from selenium import webdriver
import csv
p = []
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
        #link = driver.find_element_by_partial_link_text(", a song by ")
        link = find_elements_by_class_name("react-contextmenu-wrapper//span")
        #link = driver.find_elements_by_xpath("//h2//a")
        inner = link.get_attribute('innerHTML')
        return inner
    except:
        return "error"



#get_list()

links = []
with open('list.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        links.append(row)
print(links)


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
#driver.get("https://duckduckgo.com");
for i in range(0,len(links)):
    driver.get(links[i][0])


#for i in range(0, len(p)):
#    name = getname(p[i])
#    print(name)

#search_box.send_keys('5gPfWWQrehelkcNTuU1ph2')
#search_box.submit()
#link = driver.find_element_by_partial_link_text("Spotify")
#name = link.get_attribute('innerHTML')
#print(name)
try:
    driver.quit()
except: print("aleardy closed")
