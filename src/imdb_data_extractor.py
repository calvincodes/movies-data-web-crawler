import csv
import json
import time
import urllib.request

from bs4 import BeautifulSoup

columns = ["Name", "Release Year", "Rating", "Runtime", "Release Date",
           "Director Name", "Certificate", "genre"]
result = [columns]
badLink = []
path = "../resources/imdb_movie_list.txt"
# path = "../resources/test.txt"
with open(path, 'r') as infile:
    for link in infile:
        try:
            response = urllib.request.urlopen(link)
            soup = BeautifulSoup(response, 'html.parser',
                                 from_encoding=response.info().get_param(
                                     'charset'))
            data = json.loads(
                soup.find('script', type='application/ld+json').text)
            print(data)

            name = None
            rating = None
            releaseDate = None
            releaseYear = None
            runtime = None
            certificate = None
            genre = None
            directorName = None
            if (data is None):
                badLink.append(link)
            else:
                name = data['name'].replace("\n", "")
                rating = data['aggregateRating']['ratingValue']
                releaseDate = data['datePublished']
                releaseYear = releaseDate.split('-')[0]
                certificate = data['contentRating']
                genre = data['genre']
                directorName = data['director']['name'].replace("\n", "")

            runtimeData = soup.findAll('time')
            if (runtimeData is not None and len(runtimeData) > 1):
                runtime = (runtimeData[1].text)
            row = [name, releaseYear, rating, runtime, releaseDate,
                   directorName, certificate, genre]
            result.append(row)
            time.sleep(0.05)

        except:
            badLink.append(link)

ouputFilePath = "../resources/output/IMDBData.csv"
with open(ouputFilePath, 'w', newline='') as f:
    w = csv.writer(f)
    for List in result:
        w.writerow(List)

print("Total No. of Failed link" +  str(len(badLink)))
print(badLink)
