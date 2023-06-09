from cloudscraper import CloudScraper
from bs4 import BeautifulSoup

url = "https://slickdeals.net"
# query = str(input("Enter the name of the item: "))
query = "zenbook"

FullUrl = f"https://slickdeals.net/newsearch.php?q={query}&searcharea=deals&searchin=first&isUserSearch=1"

scraper = CloudScraper.create_scraper()
# source_text = scraper.get(url=FullUrl).text
with open("out.html", "r") as f:
    source_text = f.read()


# with open("out.html", "w") as f:
#     f.write(source.text)


def temp_func_name_id(source, parser, id_name):
    # source = source of the text
    # parser = parser to be used
    # element_name = name of the element (<div id="searchResults"> will have #searchResults)
    soup = BeautifulSoup(source, parser)
    result = soup.select(id_name)
    results = []
    for x, i in enumerate(result):
        results.append(str(i))
    return results[0]


def temp_func_name_class(source, parser, class_name):
    # source = source of the text
    # parser = parser to be used
    # element_name = name of the element <div class="resultsRow"> will have .resultsRow)
    soup = BeautifulSoup(source, parser)
    result = soup.find_all('div', {'class', 'resultRow'})
    results = []
    for x, i in enumerate(result):
        results.append(str(i))
    results = ''.join(x for x in results)
    return results


searchResults = temp_func_name_id(source=source_text, parser='html.parser', id_name='#searchResults')

resultRow = temp_func_name_class(source=searchResults, parser='html.parser', class_name='.resultRow')

# with open('test1.html', "w") as f:
#     f.write(resultRow)

# mainDealInfo = temp_func_name_id(source=resultRow, parser='html.parser', id_name='mainDealInfo')

soup = BeautifulSoup(resultRow, 'html.parser')
lazyimg = soup.select('.lazyimg')
# for x, y in enumerate(lazyimg): # to get thumb image of individual product on resultRow
#     print(y['data-original'])
dealTitle = soup.select('.dealTitle')
# for x, y in enumerate(dealTitle):
#     print(y['title'])
dealInfo = soup.select('.dealInfo')
for x, y in enumerate(dealInfo):
    # print(y.text.strip())
    print(y)
username = soup.select('.username')
# for x, y in enumerate(username):
#     print(y.text.strip())
priceCol = soup.select('.priceCol')
# for x, y in enumerate(priceCol):
#     print(y)
ratingNum = soup.select('.ratingNum')
# for x, y in enumerate(ratingNum):
#     print(y.text)


def temp_interface():
    return 0


# with open('test2.html', "w") as f:
#     f.write(mainDealInfo).
