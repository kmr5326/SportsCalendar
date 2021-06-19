from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'SportsCalender'

    def ready(self):
        # TODO: Write your codes to run on startup
        exec(open('kbo_rankCrawler.py', encoding="UTF-8").read())
        exec(open('kbo_crawler.py', encoding="UTF-8").read())
        exec(open('kleague_rankCrawler.py', encoding="UTF-8").read())
        exec(open('kleague_crawler.py', encoding="UTF-8").read())
        pass