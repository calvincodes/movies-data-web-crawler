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

                temp.append("https://www.rottentomatoes.com"+link["href"])

    rotten_tomatoes_movie_list.extend(temp)


my_set = set(rotten_tomatoes_movie_list)
print(rotten_tomatoes_movie_list)
print()
print(len(my_set))
