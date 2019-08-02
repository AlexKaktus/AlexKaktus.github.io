from urllib.request import urlopen, urljoin, Request
from urllib.error import HTTPError
import re
import os
def download_page(url):
    hdr = {'User-Agent': 'Mozzila/5.0'}
    req = Request(url, headers=hdr)
    return urlopen(req).read().decode('utf-8')

def extract_img_locations(page):
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    return img_regex.findall(page)


if __name__ == '__main__':
    dirname = input("Enter the dirname: ")
    os.mkdir(dirname)
    i = 0
    sources = []
    target_url = 'https://www.pexels.com/search/apple/'
    hdr = {'User-Agent': 'Mozzila/5.0'}
    try:
        pexels = download_page(target_url)
        locations = extract_img_locations(pexels)
        for location in locations:
            sources.append(urljoin(target_url,location))
        counter = 0
        for source in sources:
            req = Request(source, headers=hdr)
            resource = urlopen(req, verify=False).read()
            if (len(resource) > 10**6):
                output_file = open(os.getcwd() + "\\" + dirname + "\\" + "img" + str(counter) + ".jpg", 'wb')
                output_file.write(resource)
                output_file.close()
                counter += 1
            i += 1
    except HTTPError as e:
        assert e.code == 403
        
    

    
