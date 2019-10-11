from bs4 import BeautifulSoup
import requests

sitemap_url = 'https://www.brandwatch.com/sitemap--bw_report.xml'
links = []
titles = []

#Helper function
def souper(link="", parser="html.parser"):
    res = requests.get(link)
    soup = BeautifulSoup(res.text, parser)
    return soup

def get_sitemap_links(link=""):
    soup = souper(link, "lxml")
    sitemap_links = []
    for loc in soup.select('url > loc'):
        sitemap_links.append(loc.text)
    return sitemap_links

def get_page_title(link=""):
    soup = souper(link)
    title = soup.find('h1')
    return title

links = get_sitemap_links(sitemap_url)

for link in links[:5]:
    title = get_page_title(link).get_text()
    titles.append(title.strip())

print(titles)
