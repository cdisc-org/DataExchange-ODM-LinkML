import requests
import requests_cache
import os
import re
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

DEBUG = False

def print_debug(*args) -> None:
    if DEBUG:
        print(*args)

def main() -> None:
    headers = connect()
    element = 'RangeCheck'
    scraped = scrape_wiki_content(element, headers = headers)

def process_text(text) -> str:
    if not text:
        return None
    #return '\n'.join(re.sub(r'\s+', ' ', re.sub(r"^'|'$|^\"|\"$", "", t.strip())) for t in text.split('\n'))
    return re.sub(r'\s+', ' ', re.sub(r"^'|'$|^\"|\"$", "", text.strip()))

def connect() -> dict:
    requests_cache.install_cache('wiki_cache', expire_after=3600)
    # Set the TOKEN environment variable if needed using
    # export TOKEN=<your access token>
    TOKEN = os.getenv('TOKEN')
    headers = None
    if TOKEN:
        headers = {'Authorization': f'Bearer {TOKEN}'} 
    else:
        print('no access token provided via TOKEN environment variable')
    return headers

def scrape_wiki_content(
    element,
    url_prefix = 'https://wiki.cdisc.org/display/PUB/',
    headers = None
    ) -> dict:

    if not element:
        print('no element provided')
        return None
    
    url = url_prefix + element
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.status_code, 'Page', url, 'not found')
        return None
    soup = BeautifulSoup(response.content, 'html.parser')
    scraped = {'url' : url}

    print_debug('[Title and Introduction:]')
    title = soup.find('h1')
    if title:
        title = process_text(title.get_text())
        print_debug(title)
        scraped['title'] = title
    introduction = soup.find('div', class_='intro')
    if introduction:
        introduction = process_text(introduction.get_text())
        scraped['introduction'] = introduction
        print_debug(introduction)

    print_debug('[Paragraphs and Text:]')
    # Look for the description: first normal sentence/paragraph under main wiki content
    paragraphs = soup.find_all('p')
    examples = []
    description = None
    for paragraph in paragraphs:
        text = process_text(paragraph.get_text())
        if not text:
            continue
        word_count = len(re.findall('\w+', text))
        line_break_count = text.count('\n') or 0
        words_per_line = word_count / (line_break_count + 1)
        parent = paragraph.parent
        in_main_content = bool(parent.get('class', None) == ['wiki-content'] and \
                               parent.get('id', None) == 'main-content')
        is_part_of_table = (parent.name == 'td' or parent.name == 'th') and \
            (parent.find_parent('table') or parent.find_parent('table-wrap'))
        
        if not description and in_main_content and (words_per_line > 3) and not is_part_of_table:
            description = re.sub(r"^'|'$", "", text)
            start_of_table_after_description = 'Element Name'
            if not description.startswith(start_of_table_after_description):
                description = description.split(start_of_table_after_description)[0].strip()
                print_debug('Description found:', description)
                scraped['description'] = description

        is_example = bool(paragraph.get('class', None) == ['example-title'])
        if is_example:
            # print_debug('Example found', text)
            this_child = []
            for child in parent.contents:
                if type(child) != Tag:
                    if type(child) == NavigableString:
                        this_child.append(child.encode('utf8').decode('utf8'))
                    continue
                if child.get('class', None)  == 'error conf-macro output-block':
                    continue
                if child != paragraph:
                    print_debug(child.get('class'))
                    this_child.append(child.get_text(separator='\n'))
            if this_child:
                print_debug('Adding example')
                examples.append(this_child)
    scraped['examples'] = examples if examples else None

    print_debug('[Section:]')
    sections = soup.find_all('section')
    scraped['sections'] = None
    for section in sections:
        section_title = section.find('h2')
        if section_title:
            section_title = process_text(section_title.get_text())
            print_debug(section_title)
        section_content = section.find('div', class_='content')
        if section_content:
            section_content = process_text(section_content.get_text())
            print_debug('\n'.join(section_content))
        if section_title and section_content:
            scraped['sections']['title'] = section_title
            scraped['sections']['content'] = section_content

    print_debug('[Tables:]')
    # Step through table cells and map structured content 
    tables = soup.find_all('table')
    unknown_table_counter = 0
    for table in tables:
        table_headers = [header.get_text() for header in table.find_all('th')]
        table_data = []
        table_keys = []
        table_rows = table.find_all('tr')
        is_lookup_table = bool(max([len(r) for r in table_rows]) == 2)
        if is_lookup_table:
            row_dict = {}       
            for row in table_rows:
                cells = row.find_all('td')
                if not cells:
                    continue
                header = row.find_all('th')
                if header:
                    row_dict[header[0].get_text()] = process_text(cells[0].get_text(separator='\n'))
                elif len(cells) > 1:
                    row_dict[cells[0].get_text()] = process_text(cells[1].get_text(separator='\n'))

            table_data.append(row_dict)
        else:
            for row in table_rows:
                row_dict = {}
                cells = row.find_all('td')
                row_data = [process_text(cell.get_text(separator='\n')) for cell in cells]
                for i in range(len(row_data)):
                    if not table_headers or not row_data:
                        continue
                    row_dict[table_headers[i]] = process_text(row_data[i])
                if row_dict:
                    table_data.append(row_dict)
        table_rows = len(table_data)
        if table_rows:
            table_keys = list(table_data[0].keys())

        if table_rows == 1 and 'Element Name' in table_keys:
            print_debug('Element table parsed')
            scraped['element_table'] = table_data[0]
        elif table_rows and 'Attribute' in table_keys:
            print_debug('Attribute table parsed')
            scraped['attribute_table'] = table_data
        else:
            unknown_table_counter += 1
            unknown_table_name = 'Unidentified table ' + str(unknown_table_counter)
            print_debug(unknown_table_name)
            scraped[unknown_table_name] = table_data
        print_debug('rows:', table_rows, 'keys:', table_keys)

    # print_debug('[Lists:]')
    # lists = soup.find_all(['ul', 'ol'])
    # for lst in lists:
    #     list_items = [item.get_text() for item in lst.find_all('li')]
    #     print_debug('LIST ITEMS', list_items)

    print_debug('[Links:]')
    link_dict = {}
    links = soup.find_all('a')
    for link in links:
        link_url = link.get('href', '').strip()
        link_text = link.get_text().strip()
        link_dict[link_url] = link_text
        # print_debug('link', link_url, link_text)
    print_debug(len(link_dict), 'links found')
    scraped['links'] = link_dict

    print_debug('[Images:]')
    images = soup.find_all('img')
    images_out = []
    for image in images:
        image_url = image.get('src', '').strip()
        image_alt = image.get('alt', '').strip()
        print_debug(image_url, image_alt)
        images_out.append({'url' : image_url,
                           'alt' : image_alt if image_alt else None})
    scraped['images'] = images_out

    print_debug('[Examples:]')
    for example in examples:
        print_debug(example)
    
    return scraped
