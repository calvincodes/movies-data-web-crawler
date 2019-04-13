import sys
import csv

csv.field_size_limit(sys.maxsize)

imdb_movie_names = {''}
rotten_tomatoes_movie_names = {''}

with open('../resources/output/IMDBData.csv') as sample_csv:
    csv_reader = csv.reader(sample_csv)
    for row in csv_reader:
        imdb_movie_names.add(str(row[0]).strip())

with open('../resources/output/RottenTomatoesData.csv') as sample_csv:
    csv_reader = csv.reader(sample_csv)
    for row in csv_reader:
        rotten_tomatoes_movie_names.add(str(row[0]).strip())

imdb_movie_names.remove('')
rotten_tomatoes_movie_names.remove('')

entity_match = 0
for imdb_movie in imdb_movie_names:
    if imdb_movie in rotten_tomatoes_movie_names:
        entity_match = entity_match + 1

print(str(entity_match))