import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
token="5f254a86b88a4e188c3d6a768aeee536d8dd15effba"
proxyModeUrl = "http://{}:@proxy.scrape.do:8080".format(token)

proxies={
    "http": proxyModeUrl,
    "https": proxyModeUrl,
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

def top_25_movies():
    url="https://www.imdb.com/chart/top/"
    response=requests.get(url, headers=headers, proxies=proxies, verify=False)
    if response.status_code==200:
        soup=BeautifulSoup(response.text, "html.parser")
        print("Successfully Fetched the Top 25 Movies!")
        title_elements=soup.find_all(class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-a69a4297-2 bqNXEn cli-title with-margin")
        
        movie_elements=[title.text for title in title_elements]
        
        file_name=f"top_25_movies_{datetime.now().strftime('%d-%m-%Y')}.json"

        if not os.path.exists(file_name):
            with open(file_name, 'w', encoding="utf-8") as f:
                json.dump(movie_elements, f, ensure_ascii=False, indent=4)
            print(f"Top 25 Movies List saved to {file_name}")

    else:
        print(response.status_code)

def most_popular_movies():
    url="https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    response=requests.get(url, headers=headers, proxies=proxies, verify=False)
    if response.status_code==200:
        print("Successfully Fetched the Most Popular Movies!")
        soup=BeautifulSoup(response.text, "html.parser")
        file_path=f"Most_Popular_Movies{datetime.now().strftime('%d-%m-%Y')}.json"

        movie_elements=soup.find_all(class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-a69a4297-2 bqNXEn cli-title with-margin")

        movie_names=[movie.text for movie in movie_elements]

        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(movie_names, f, ensure_ascii=False, indent=4)
            print(f"Most Popular Movies List saved to {file_path}")
    else:
        print(f"Error Occured: {response.status_code}")

def top_box_office_us():
    url="https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht"
    response=requests.get(url, headers=headers, proxies=proxies, verify=False)

    if response.status_code==200:
        print("Successfully Fetched the Top Box Office of US!")
        soup=BeautifulSoup(response.text, "html.parser")
        file_path=f"Top_Box_Office_US_{datetime.now().strftime("%d-%m-%Y")}.json"
        top_list=soup.find_all(class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-a69a4297-2 bqNXEn cli-title with-margin")

        output_list=[list.text for list in top_list]

        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(output_list, f, ensure_ascii=False, indent=4)
            print(f"Top Box Office List saved to {file_path}")
    else:
        print(f"Error Occured: {response.status_code}")

def top_tv_shows():
    url="https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
    response=requests.get(url, headers=headers, proxies=proxies, verify=False)

    if response.status_code==200:
        print("Successfully Fetched the Top TV Shows")
        soup=BeautifulSoup(response.text, "html.parser")
        file_path=f"Top_TV_Shows_{datetime.now().strftime('%d-%m-%Y')}.json"

        top_shows=soup.find_all(class_= "ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-a69a4297-2 bqNXEn cli-title with-margin")
    
        top_shows_list=[list.text for list in top_shows]

        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(top_shows_list, f, ensure_ascii=False, indent=4)
            print(f"Top Shows List saved to {file_path}")

    else:
        print(f"Error Encountered: {response.status_code}")

def main():
    top_25_movies()
    most_popular_movies()
    top_box_office_us()
    top_tv_shows()

if __name__ == "__main__":
    main()