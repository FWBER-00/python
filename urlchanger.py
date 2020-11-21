import sys
from urllib.parse import urlparse

url = urlparse(sys.argv[1])

if argv[2] == 's':
    if url.scheme == argv[3]:
        print(url)
    else:
        newurl = url.replace(url.scheme, argv[3])
        print(newurl)
