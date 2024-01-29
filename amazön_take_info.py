import requests
from bs4 import BeautifulSoup

def fetch_page():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    link = "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb"
    try:
        response = requests.get(link, headers=headers)
        print(f"Response Status Code: {response.status_code}")
        if response.status_code == 200:
            return response
        else:
            print("Failed to retrieve data from the website.")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def winter_sales():
    return_list = []
    response = fetch_page()
    if response:
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
                            return_list.append(img_src)  # Append only the image source

    return return_list

def all_deals():
    return_list = []
    response = fetch_page()
    if response:
        soup = BeautifulSoup(response.text, 'lxml')
        slot_content = soup.find(id='slot-14')

        if slot_content:
            thing_1 = slot_content.find(class_='GridContainer-module__gridMainContainer_24aSWvAi-VAzH5okoDOqpb')
            if thing_1:
                items = thing_1.find_all(class_='Grid-module__gridDisplayGrid_2X7cDTY7pjoTwwvSRQbt9Y')
                for item in items:
                    img_tag = item.find('img')
                    if img_tag and img_tag.has_attr('src'):
                        img_src = img_tag['src']
                        if ".jpg" in img_src:
                            return_list.append(img_src)  # Append only the image source
    return return_list

# Call the functions
winter_sales_images = winter_sales()
print(winter_sales_images)