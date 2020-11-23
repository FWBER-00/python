import sys
from urllib.parse import urlparse

url = urlparse(sys.argv[1])

if len(sys.argv) != 4:
    print("Insufficient arguments")
    sys.exit()

else:
    if str(sys.argv[2]) == 's':
        if url.scheme == str(sys.argv[3]):
            print(url)
        else:
            newurl = url.replace(url.scheme, str(sys.argv[3]))
            print(newurl)
 
    elif str(sys.argv[2]) == 'n':
        if url.netloc == str(sys.argv[3]):
            print(url)
        else:
            newurl = url.replace(url.netloc, str(sys.argv[3]))
            print(newurl)

    elif str(sys.argv[2]) == 'p':
        if url.path == str(sys.argv[3]):
            print(url)
        else:
            newurl = url.replace(url.path, str(sys.argv[3]))
            print(newurl)


    elif str(sys.argv[2]) == 'q':
        if url.query == str(sys.argv[3]):
            print(url)
        else:
            newurl = url.replace(url.query, str(sys.argv[3]))
            print(newurl)

    elif str(sys.argv[2]) == 'f':
        if url.fragment == str(sys.argv[3]):
            print(url)
        else:
            newurl = url.replace(url.fragment, str(sys.argv[3]))
            print(newurl)
    else:
        print("Wrong argument")


