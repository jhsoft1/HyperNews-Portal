import json
import os


news = [{'created': '2020-02-22 16:40:00', 'text': 'A new star appeared in the sky.', 'title': 'A star is born',
         'link': 9234732}, {'created': '2020-02-09 14:15:10', 'text': 'Text of the news 1', 'title': 'News 1',
                            'link': 1},
        {'created': '2020-02-10 14:15:10', 'text': 'Text of the news 2', 'title': 'News 2', 'link': 2},
        {'created': '2020-02-09 16:15:10', 'text': 'Text of the news 3', 'title': 'News 3', 'link': 3}]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_JSON_PATH = os.path.join(os.path.dirname(BASE_DIR), 'task/hypernews/news.json')
with open(NEWS_JSON_PATH, 'w') as json_file:
    json.dump(news, json_file)
