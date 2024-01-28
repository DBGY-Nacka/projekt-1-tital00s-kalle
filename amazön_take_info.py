import requests
from bs4 import BeautifulSoup

def main():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
    
    link = "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb"
    try:
        response = requests.get(link, headers=headers)
        print(response.status_code)

        if response.status_code == 200:
            proccess_page_image_and_names_from_winter_sales_favorite(response)
        else:
            print("Failed to retrieve data from the website.")
    except requests.RequestException as e:
        pass

def proccess_page_image_and_names_from_winter_sales_favorite(response):
    soup = BeautifulSoup(response.text, 'lxml')
    slot_content = soup.find(id='slot-5')
    
    if slot_content:
        carousel_center = slot_content.find(class_='a-carousel-center')
        if carousel_center:
            items = carousel_center.find_all('li', class_='a-carousel-card')
            
            for item in items:
                img_tag = item.find('img')
                if img_tag and img_tag.has_attr('src'):
                    img_src = img_tag['src']
                    if ".jpg" in img_src:
                        print(img_src)

    #Ska den bort?
    soup = BeautifulSoup(response.text, 'lxml')
    slot_content = soup.find(id='slot-5')
    
    if slot_content:
        carousel_center = slot_content.find(class_='a-carousel-center')
        if carousel_center:
            items = carousel_center.find_all('li', class_='a-carousel-card')
            
            for item in items:
                name_span = item.find('span', class_='a-truncate-full')
                name = name_span.get_text(strip=True)
                
                if name:
                    print(name)

def process_page_images_and_names(response):
    soup = BeautifulSoup(response.text, 'lxml')
    slot_content = soup.find(id='slot-14')
    
    print(slot_content)
    if slot_content:
        thing_1 = slot_content.find(class_='GridContainer-module__gridMainContainer_24aSWvAi-VAzH5okoDOqpb')
        if thing_1:
            print(thing_1)
            items = thing_1.find_all(class_='Grid-module__gridDisplayGrid_2X7cDTY7pjoTwwvSRQbt9Y')
            if items:
                print(items)
                for item in items:
                    img_tag = item.find('img')
                    if img_tag and img_tag.has_attr('src'):
                        img_src = img_tag['src']
                        if ".jpg" in img_src:
                            print(img_src)


main()
            
        
    
    
    