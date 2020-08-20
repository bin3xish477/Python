from bs4 import BeautifulSoup
from requests import get

URL = "https://github.com/binexisHATT"
HTML = get(URL).content

if __name__ == "__main__":
    soup = BeautifulSoup(HTML, 'html.parser')
    print("*"*25, "Title", "*"*25)
    print(soup.title.string)

    print()
    print("*"*25, "Links", "*"*25)
    for link in soup.find_all('a'):
        print(link.get('href'))
