from requests_html import HTMLSession

def load_names():
    print("Getting names")
    url = 'https://www.sreality.cz/hledani/prodej/byty?strana=1#x=15.518784625&y=49.8040025&z=6'
    page_html = get_page(url)
    name_tags = page_html.find('.name')
    #print(name_tags)
    name_list =[]
    for tag in name_tags:
        name = tag.text
        name_list.append(name)
        #print(name)
    #print(len(name_tags))
    return name_list

def get_page(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render(timeout=25)
    page_html = r.html
    return page_html


def load_items():
    print("Getting flats data")
    pages= list(range(1,26))
    url_image_list = []
    name_list = []

    for page in pages:

        url = 'https://www.sreality.cz/hledani/prodej/byty?strana={page}'.format(page=page)
        page_html = get_page(url)
        name_tags = page_html.find('.name')

        for tag in name_tags:
            name = tag.text
            name_list.append(name)
            # print(name)
        # print(len(name_tags))

        image_tags = page_html.find('._2xzMRvpz7TDA2twKCXTS4R')
        for tag in image_tags:
            images = tag.find('img')
            #for image in images:
            start = "src='"
            end = "' alt"
            url_image = (str(images[0]).split(start))[1].split(end)[0]
            url_image_list.append(url_image)
                #print(url_image)
        print("Number of loaded items: ", len(url_image_list))
    return name_list, url_image_list



#if __name__ == '__main__':
    #download_web_image()
    #load_names()
    #load_web_image()
