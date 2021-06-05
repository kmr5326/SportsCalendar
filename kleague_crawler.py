from selenium import webdriver
import pymongo

conn = pymongo.MongoClient('mongodb+srv://hg:5326@sportscalender.sosjb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
#print(conn.list_database_names())
db = conn.get_database('djangodb')

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('D:/hg/chromedriver_win32/chromedriver', options=options)
driver.implicitly_wait(3)
driver.get('https://www.kleague.com/schedule?ch=073944&select_league=1')

collection = db.get_collection('kleague_Schedule_schedule')

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for i in range(0,12):
    m = driver.find_element_by_id("vw_month")
    driver.execute_script("arguments[0].innerText = "+"'"+month[i]+"'", m)
    driver.execute_script('get_schedule({},\'html\')')

    schedule_list = driver.find_element_by_class_name('data-body')
    tables = schedule_list.find_elements_by_tag_name("table")
    for t in tables:
        tbody = t.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        print(rows[0].get_attribute("id")[:-1])
        date = rows[0].get_attribute("id")[:-1]
        cnt = 0
        d = {}
        for row in rows:
            tds = row.find_elements_by_tag_name("td")
            #print(tds[1].text + ' / '+tds[3].text)
            cnt += 1
            d["game"+str(cnt)] = tds[1].text + ' [' + tds[3].text + ']'
        print(d)
        d["dataCnt"] = str(cnt)
        collection.replace_one({"_id": date}, d, upsert=True)






