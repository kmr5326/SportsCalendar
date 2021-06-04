from selenium import webdriver
import pymongo


conn = pymongo.MongoClient('mongodb+srv://hg:5326@sportscalender.sosjb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
#print(conn.list_database_names())
db = conn.get_database('djangodb')

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('D:/hg/chromedriver_win32/chromedriver', options=options)
driver.implicitly_wait(3)
driver.get('https://www.kleague.com/rank?ch=081920')

collection = db.get_collection('kleague_Rank_rank')

table = driver.find_element_by_id('rank_data_lists')
rows = table.find_elements_by_tag_name('tr')
cnt = 0
for row in rows:
    td = row.text
    li_list = td.split('\n')
    split = li_list[2].split(' ')
    cnt += 1
    d = {
        "rank": li_list[0],
        "team": li_list[1],
        "gameCnt": split[0],
        "point": split[1],
        "win": split[2],
        "draw": split[3],
        "lose": split[4],
        "goal": split[5],
        "lost": split[6]
    }
    #collection.replace_one({"_id": str(cnt)}, d, upsert=True)
    print(d)



