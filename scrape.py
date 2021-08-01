from lxml import html
import requests
page = requests.get('https://twitter.com/UniteAlbertans/status/899468829151043584')
tree = html.fromstring(page.content)
# text = tree.xpath('//div[contains(@class, "permalink-tweet-container")]//p[contains(@class, "tweet-text")]//text()')
# text = tree.xpath('id("main-content")//*[@class="tweet-text"][1]//text()')
text = tree.xpath('//span[text()="Tweet"]')
print(text)
