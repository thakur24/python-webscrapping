#install requests & Beatuiful soup libraries beforing improting 
# command - pip install requests
#pip install Beautifulsoup4 

import requests
import bs4

url=input("enter the url")

#sending a http request to the server using get function
response=requests.get(url)


filename="source.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")

#it will fromat all the content of the specific url
formatted_text=bs.prettify()
print(formatted_text)

with open(filename,"w+") as f:
    f.write(formatted_text) # A html file with all the formatted text of the specific url will be formed.


list_imgs=bs.find_all('img') # finding all img tags
no_of_imgs=len(list_imgs) #counting all img tags

list_as=bs.find_all('a') # finding all anchor tags
no_of_as=len(list_as) #counting all anchor tags

list_titles=bs.find_all('title') # finding all tilte tags
no_of_titles=len(list_titles) #counting all tilte tags

print("no of img tag",no_of_imgs)
print("no of anchor tags", no_of_as)
print("no of title tags",no_of_titles)