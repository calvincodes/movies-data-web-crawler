import json
import urllib.request
import re
import csv
from bs4 import BeautifulSoup
import time

columns = ["Name", "Release Year", "Rating", "Runtime", "Release Date", "Director Name", "Certificate", "genre","studio"]
result = [columns]
badLink = []
# path = "../resources/test.txt"
path = "../resources/rotten_tomatoes_movie_list.txt"

with open(path, 'r') as infile:
    for link in infile:
        try:
            response = urllib.request.urlopen(link)
            soup = BeautifulSoup(response, 'html.parser',from_encoding=response.info().get_param('charset'))
            # print(soup)
            data = json.loads(soup.find('script', type='application/ld+json').text)
            name=None
            rating=None
            releaseDate=None
            releaseYear=None
            runtime=None
            certificate=None
            genre=None
            directorName=None
            studio=None

            if(soup.find('script', type='application/ld+json') is not None):
                data = json.loads(
                    soup.find('script', type='application/ld+json').text)
                name = data['name']
                rating = data['aggregateRating']['ratingValue']
                certificate = data['contentRating']

            metaData = soup.findAll('div', class_="meta-value")
            if(metaData is not None):
                if(len(metaData) >=2):
                    genre = metaData[1].text.replace("\n", "")

                if (len(metaData) >= 3):
                    directorName = metaData[2].text.replace("\n", "")

                if (len(metaData) >= 5):
                    releaseDate = (metaData[4].text).split('\n')[1]
                    releaseYear =((metaData[4].text).split('\n')[1]).split(',')[-1].strip()


                if (len(metaData) >= 7):
                    runtime = metaData[6].text.strip()

                if(len(metaData) >= 8):
                    studio = metaData[7].text.strip()


            row = [name, releaseYear, rating, runtime, releaseDate, directorName, certificate, genre, studio]
            result.append(row)
            time.sleep(0.05)
        except:
            print(link + "\n")
            badLink.append(link)

filename = "../resources/output/RottenTomatoesData.csv"
with open(filename,'w',newline='') as f:
        w = csv.writer(f)
        for List in result:
            w.writerow(List)
