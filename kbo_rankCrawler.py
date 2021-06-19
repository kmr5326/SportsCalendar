from selenium import webdriver
import pymongo

conn = pymongo.MongoClient('mongodb+srv://hg:5326@sportscalender.sosjb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
#print(conn.list_database_names())
db = conn.get_database('djangodb')

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('D:/hg/chromedriver_win32/chromedriver', options=options)
driver.implicitly_wait(3)
driver.get('https://www.koreabaseball.com/TeamRank/TeamRank.aspx')

collection = db.get_collection('kbo_Rank_rank')

table = driver.find_element_by_class_name('tData')
tbody = table.find_element_by_tag_name("tbody")
rows = tbody.find_elements_by_tag_name("tr")
cnt = 0
for row in rows:
    td = row.text
    li_list = td.split('\n')
    #print(li_list)
    for li in li_list:
        li_split = li.split(' ')
        print(li_split)
        cnt += 1
        d = {
            "rank": li_split[0],
            "team": li_split[1],
            "gameCnt": li_split[2],
            "win": li_split[3],
            "lose": li_split[4],
            "draw": li_split[5]
        }
        collection.replace_one({"_id": str(cnt)}, d, upsert=True)

driver.quit()