from bs4 import BeautifulSoup , SoupStrainer
import bs4
import requests
import csv
import io
import unicodedata

source = requests.get("https://www.youtube.com/feed/trending").text

trending_containers = SoupStrainer(class_="yt-lockup-content")
soup = BeautifulSoup(source, 'lxml', parse_only=trending_containers)


csv_file = open('YouTube Trending Titles on 12-30-18.csv','w' , encoding='utf-8')
csv_writer = csv.writer(csv_file, delimiter="\t")
##csv_writer.writerow([title, description])

for content in soup.select('.yt-lockup-content'):
    try:
        title = content.h3.a.text
        print(title)

        description = content.select_one('.yt-lockup-description.yt-ui-ellipsis.yt-ui-ellipsis-2').text
        print(description)

    except Exception as e:
        description = None

    print('\t')
    csv_writer.writerow([title, description])

csv_file.close()
