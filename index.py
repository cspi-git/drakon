import requests, os, json, re, base64

class colors:
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[94m'
    end = '\033[0m'

try:
    from bs4 import BeautifulSoup
except ImportError:
    print(colors.red + "You don't have BeautifulSoup installed!" + colors.end)
    print(colors.yellow + "Installing BeautifulSoup..." + colors.end)
    os.system("pip install bs4")

print("\n")

try:
    links = []

    email = input(colors.blue + "Enter the email or phone number: " + colors.end)
    pageamount = input(colors.blue + "Enter the amount of pages you want to search: " + colors.end)
    
    # check if its a email or phone number
    if "@" not in email:
        print(colors.yellow + "Searching for phone number..." + colors.end)   
    else:
        print(colors.yellow + "Searching for email..." + colors.end)
    print(colors.yellow + "This might take a while..." + colors.end)


    for i in range(1, int(pageamount) + 1):
        url = "https://www.google.com/search?q=" + email + "&start=" + str(i)
        r = requests.get(url)
        
        if "captcha" in r.text:
            print(colors.red + "Captcha detected!" + colors.end)
            exit()

        soup = BeautifulSoup(r.text, "html.parser")

        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith("/url?q="):
                url = re.findall(r'/url\?q=(.*?)&', href)[0]
                
                if "google.com" in url or "/search" in url:
                    continue

                links.append(url)

    if not links:
        print(colors.red + "No links found!" + colors.end)
        exit()

    print(colors.green + "Done searching!" + colors.end)

    print(colors.yellow + "Getting links..." + colors.end)

    for link in links:
        print(link)

    print('\n')
    print(colors.green + "Done getting links!" + colors.end)
    print("Altorx the UFC 4 Undisputed Double Champion | G.O.A.T.")
except KeyboardInterrupt:
    print(colors.red + "Exiting..." + colors.end)
    exit()
else:
    pass
