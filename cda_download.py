import requests
from bs4 import BeautifulSoup

def get_links(Url):
    getURL = requests.get(Url, headers={"User-Agent": "Mozilla/5.0"}) # or Mozilla/5.0 , Chrome/104.0.5112.80
    soup = BeautifulSoup(getURL.text, 'html.parser')

    
    #link = soup.find("div", class_="brdPlayer brndPlayerPd")
    inner = soup.find('div', id ="mediaplayer15413628f2", recursive=True)
    #children = link.findChildren("div" , recursive=True)
    #for child in link:
        #print(child)
    print(inner)
    
Url = 'https://www.cda.pl/video/15413628f2'
get_links(Url)
print('koniec')

# to co potrzbuje się nie ładuje na czas dlatego wygląda jakby tego nie było, użyć selenium albo urlib ?
    

# POBIERNAIE STREAMA
cda = 'https://vwaw134.cda.pl/ka9b6Mn8JoVsy0a9Lb5KSA/1695945451/hde7c9d8fecc1d29f8583c464f1b52cd90.mp4'

def download_video(link): 

    file_name = link.split('/')[-1]    

    print("Downloading file:%s"%file_name)

    # create response object 
    r = requests.get(link, stream = True) 

    # download started 
    with open(file_name, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 100*100): 
            if chunk: 
                f.write(chunk)
    print('koniec')
    return

#download_video(cda)



def test1():
    html_source = '''
    <div class="category-bar">
        <h3>Categories</h3>
        <div class="categories">
            <ul>
            <li><a href="/category/python">Python</a></li>
            </ul>
        </div>
    </div>
    '''

    # Parse
    soup = BeautifulSoup(html_source, "html.parser")

    # Find Div with "category-bar" in class
    category_div = soup.find("div", class_="category-bar")

    # Get inner div
    inner = category_div.contents

    # Print contents of div one by one
    for el in inner:
        print(el)
        print('###')
#test1()
