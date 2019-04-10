__author__ = "Srujana, Anshu, Arpit"

from bs4 import BeautifulSoup
import urllib.request

imdb_movie_set = {''}


def crawl_and_add_links(min, max, step_size, base_url):
    for page_num in range(min, max, step_size):
        resp = urllib.request.urlopen(base_url + str(page_num))
        soup = BeautifulSoup(resp, 'html.parser', from_encoding=resp.info().get_param('charset'))
        for link in soup.find_all('a', href=True):
            if link['href'].startswith("/title") and "hrid" not in link['href']:
                movie_id = link["href"].split("/")[2]
                if movie_id not in imdb_movie_set:
                    imdb_movie_set.add(movie_id)


# Feature Film, Action
action_movies_base_url = "https://www.imdb.com/search/title?title_type=feature" \
                         "&num_votes=25000,&genres=action&sort=user_rating,desc&ref_=adv_nxt&start="
crawl_and_add_links(1, 1210, 50, action_movies_base_url)
print("Crawling finished - Action movies")

# Feature Film, Thriller
thriller_movies_base_url = "https://www.imdb.com/search/title?title_type=feature" \
                           "&num_votes=25000,&genres=thriller&sort=user_rating,desc&ref_=adv_nxt&start="
crawl_and_add_links(1, 1622, 50, thriller_movies_base_url)
print("Crawling finished - Thriller movies")

# Feature Film, Drama
drama_movies_base_url = "https://www.imdb.com/search/title?title_type=feature" \
                        "&num_votes=25000,&genres=drama&sort=user_rating,desc&ref_=adv_nxt&start="
crawl_and_add_links(1, 2471, 50, drama_movies_base_url)
print("Crawling finished - Drama movies")

imdb_movie_set.remove('')

print("Crawling finished - Total movie links extracted: ")
print(len(imdb_movie_set))

for movie_link in imdb_movie_set:
    with open("../resources/imdb_movie_list.txt", "a") as imdb_movie_list_file:
        imdb_movie_list_file.write("https://www.imdb.com/title/" + movie_link)
        imdb_movie_list_file.write("\n")

