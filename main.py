import pyshorteners

link = input('Enter link to shorten: ')
short = pyshorteners.Shortener()
shortened_link = short.tinyurl.short(link)

print(f"\nShortened link is : {shortened_link}")
