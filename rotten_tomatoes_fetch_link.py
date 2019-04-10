from bs4 import BeautifulSoup
import urllib.request

rotten_tomatoes_movie_list = []
for num in range(1900, 2020):
    movielistlink = "https://www.rottentomatoes.com/top/bestofrt/?year="
    resp = urllib.request.urlopen(movielistlink + str(num))
    soup = BeautifulSoup(resp, 'html.parser', from_encoding=resp.info().get_param('charset'))
    temp = []
    for link in soup.find_all('a', href=True):

        if link['href'].startswith("/m") and "hrid" not in link['href']:

            if link["href"] not in temp:

                temp.append(link["href"])

    rotten_tomatoes_movie_list.extend(temp)


my_set = set(rotten_tomatoes_movie_list)
# print(rotten_tomatoes_movie_list)
# print()
for i in my_set:
    # print(i)
    with open("rotten_tomatoes_movie_list.txt", "a") as myFile:
        myFile.write("https://www.rottentomatoes.com"+str(i))
        myFile.write("\n")
# print("Done!")

print("No. of movies: ", len(my_set))
