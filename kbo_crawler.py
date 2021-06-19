from selenium import webdriver
import pymongo


conn = pymongo.MongoClient('mongodb+srv://hg:5326@sportscalender.sosjb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
#print(conn.list_database_names())
db = conn.get_database('djangodb')
#print(db.list_collection_names())


options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('D:/hg/chromedriver_win32/chromedriver', options=options)
driver.implicitly_wait(3)
driver.get('https://www.koreabaseball.com/Schedule/Calendar.aspx')


selY = driver.find_elements_by_id("ddlYear")
year = []
for index, value in enumerate(selY):
    y = value.text
    year = y.split('\n')
selM = driver.find_elements_by_id("ddlMonth")
mon = []
for index, value in enumerate(selM):
    m = value.text
    mon = m.split('\n')

collection = db.get_collection('kbo_Schedule_schedule')

#모든 달(월별) 크롤링
'''
for m in mon:
    driver.find_element_by_id("ddlMonth").click()
    xpath_format = '//option[@value="{month}"]'
    driver.find_element_by_xpath(xpath_format.format(month=m)).click()
    table = driver.find_element_by_class_name('schedulCalender')
    tbody = table.find_element_by_tag_name("tbody")
    rows = tbody.find_elements_by_tag_name("tr")
    for row in rows:
        tds = row.find_elements_by_tag_name("td")
        for td in tds:
            lis = td.find_elements_by_tag_name("li")
            li_list = []
            for li in lis:

                if li.get_attribute("class") == 'rainCancel':
                    li_list.append(li.text + ' 우천취소')
                else:
                    li_list.append(li.text)
            print(li_list)
            if li_list[0] != '':
                d = {}
                for i in range(1, len(li_list)):
                    d["game" + str(i)] = li_list[i]
                day = m+"."+li_list[0]
                collection.replace_one({"_id": day}, d, upsert=True)
'''

#이번 달만 크롤링
table = driver.find_element_by_class_name('schedulCalender')
tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")
for row in rows:
    tds = row.find_elements_by_tag_name("td")
    for td in tds:
        lis = td.find_elements_by_tag_name("li")
        li_list = []
        for li in lis:

            if li.get_attribute("class") == 'rainCancel':
                li_list.append(li.text + ' 우천취소')
            else:
                li_list.append(li.text)
        print(li_list)
        if li_list[0] != '':
            d = {}
            for i in range(1, len(li_list)):
                d["game" + str(i)] = li_list[i]
            day = m+"."+li_list[0]
            collection.replace_one({"_id": day}, d, upsert=True)


driver.quit()
