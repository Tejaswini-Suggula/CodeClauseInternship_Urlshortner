import pyshorteners

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    return short_url


long_url = 'https://chatgpt.com/c/66f96fba-a558-8011-8b6f-526b8f98ae7d'
print("Shortened URL:", shorten_url(long_url))
