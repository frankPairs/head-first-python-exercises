from url_utils import get_from_urls

urls = ['http://talkpython.fm', 'http://google.com', 'http://python.org']

for resp_len, status, url in get_from_urls(urls):
    print(resp_len, '->', status, '->', url)
