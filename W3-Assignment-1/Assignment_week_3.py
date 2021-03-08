import requests
from bs4 import BeautifulSoup
import json

# save to text file
def save_to_text(content):
    f = open("data.text","a")
    f.write(content + "\n")
    f.close()
# get website data
def web_crawler(web_url):
    # web_url = "https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"
    response = requests.get(web_url)
    web_status = response.status_code

    if web_status != requests.codes.ok:
        print("Website Error!")
        return
    else:
        print("Connected to Website.")
        #get text
        web_text = response.text
        # convert dictionary string to dictionary
        web_text =json.loads(web_text)
        # get results
        view_results = web_text['result']['results']
        # print(view_results)
        # view_title, view_longitude, view_latitude, view_pic_url
        for result in view_results:
            # print(result)
            view_title = result['stitle']
            view_longitude = result['longitude']
            view_latitude = result['latitude']
            # judge jpg ot png
            view_pic_url_index_jpg = result['file'].lower().find('.jpg')
            view_pic_url_index_png = result['file'].lower().find('.png')
            if view_pic_url_index_png != -1 and view_pic_url_index_jpg != -1:
                if view_pic_url_index_png < view_pic_url_index_jpg:
                    view_pic_url = result['file'][:view_pic_url_index_png] + '.png'
                else:
                    view_pic_url = result['file'][:view_pic_url_index_jpg] + '.jpg'
            else:
                if view_pic_url_index_png == -1:
                    view_pic_url = result['file'][:view_pic_url_index_jpg] + '.jpg'
                else:
                    view_pic_url = result['file'][:view_pic_url_index_png] + '.png'

            total_view = view_title + ',' + view_longitude + ',' + view_latitude + ',' + view_pic_url
            # save to text file
            save_to_text(total_view)
        print("Save to text file done!")

web_url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
web_crawler(web_url)
