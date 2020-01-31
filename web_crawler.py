import requests
from bs4 import BeautifulSoup

visited_pages = []

def parse_page(link):
    request_object = requests.get(link, auth=('user', 'pass'))
    soup = BeautifulSoup(request_object.content, "lxml")
    return soup

def status(link):
    try:
        error_code = requests.get(link).status_code
    except requests.exceptions.ConnectionError:
        error_code = -1
    return error_code

def find_page_data(main_url, depth=0):
    all_urls_info = []
    all_js_links = []
    all_css_links = []
    all_img_links = []

    soup = parse_page(main_url)
    a_tags = soup.findAll('a', href=True)
    js_tags = soup.findAll('script', src=True)
    css_tags = soup.find_all('link', rel='stylesheet', href=True)
    img_tags = soup.find_all('img')

    if main_url.endswith('/'):
        domain = main_url[:-1]
    else:
        domain = main_url

    for tag in js_tags:
        js_link = tag.get('src')
        if 'http' in js_link:
            all_js_links.append(js_link)
        else:
            if js_link.startswith('/'):
                all_js_links.append(domain + js_link)
            else:
                all_js_links.append(domain + '/' + js_link)

    for tag in css_tags:
        css_link = tag.get('href')
        if 'http' in css_link:
            all_css_links.append(css_link)
        else:
            if css_link.startswith('/'):
                all_css_links.append(domain + css_link)
            else:
                all_css_links.append(domain + '/' + css_link)

    for tag in img_tags:
        img_link = tag.get('src')
        if 'http' in img_link:
            all_img_links.append(img_link)
        else:
            if img_link.startswith('/'):
                all_img_links.append(domain + img_link)
            else:
                all_img_links.append(domain + '/' + img_link)

    for a_tag in a_tags:
        if 'http://' not in a_tag['href'] and 'https://' not in a_tag['href'] and '/' in a_tag['href']:
            url = domain + a_tag['href']
        elif 'http://' in a_tag['href'] or 'https://' in a_tag['href']:
            url = a_tag['href']
        else:
            continue

        if domain in url and url not in visited_pages:
            visited_pages.append(url)
            page_info = {}
            page_info['url'] = url
            page_info['js'] = all_js_links
            page_info['css'] = all_css_links
            page_info['imgs'] = all_img_links
            page_info['status_code'] = status(url)
            page_info['depth'] = depth
            all_urls_info.append(page_info)

    return all_urls_info


def crawl(site, search_depth):
    url = site
    depth = int(search_depth)
    all_page_data = []
    all_page_data.append(find_page_data(url, 0))

    if depth > 0:
        for i in range(1, depth+1):
            new_page_data = []
            for page in all_page_data[i-1]:
                new_page_data.append(find_page_data(page['url'], i))
            all_page_data.append(new_page_data)

    return all_page_data