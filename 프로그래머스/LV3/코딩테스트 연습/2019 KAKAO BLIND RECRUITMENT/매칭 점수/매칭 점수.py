from re import findall, search


class Page:
    def __init__(self, word, html, page_num, url):
        self.page_num = page_num
        self.url = url
        self.external_links = self.get_external_links(html)
        self.external_links_num = len(self.external_links)

        self.basic_score = self.get_basic_score(word, html)
        self.link_score = 0
        self.matching_score = 0
        self.pages_pointing_this_page = []


    def get_basic_score(self, word, html):
        pattern = f'(?<=[^a-z]){word}[^a-z]'
        return len(findall(pattern, html))
    

    def get_external_links(self, html):
        pattern = '<a href=\"https://[^ ]*\"'
        links = findall(pattern, html)
        for i in range(len(links)):
            links[i] = links[i][links[i].find("https://"):].rstrip('"')
        return links


    def set_link_score(self):
        for p in self.pages_pointing_this_page:
            self.link_score += p.basic_score / p.external_links_num


    def set_matching_score(self):
        self.matching_score = self.basic_score + self.link_score


class PageList:
    def __init__(self, word, pages):
        self.page_list = []
        self.url_page_dic = dict()

        for i, html in enumerate(pages):
            url = self.get_html_url(html)
            page = Page(word, html.lower(), i, url)
            self.page_list.append(page)
            self.url_page_dic[url] = page
    
    
    def get_html_url(self, html):
        pattern = '<meta.*property=\"og:url\".*content=\"https://[^ ]*\".*/>'
        url = search(pattern, html)[0]
        url = url[url.find('content="https://')+9:]
        url = url[:url.find('"')]
        return url
    

    def set_page_pointing_info(self):
        for i in range(len(self.page_list)):
            for j in range(len(self.page_list)):
                if i == j: continue
                if self.page_list[i].url in self.page_list[j].external_links:
                    self.page_list[i].pages_pointing_this_page.append(self.page_list[j])


    def set_link_matching_score(self):
        for page in self.page_list:
            page.set_link_score()
            page.set_matching_score()


    def sort(self):
        self.page_list.sort(key=lambda x:(-x.matching_score, x.page_num))


    def get_best_match(self):
        self.sort()
        return self.page_list[0].page_num


def solution(word, pages):
    word = word.lower()
    page_list = PageList(word, pages)
    page_list.set_page_pointing_info()
    page_list.set_link_matching_score()
    return page_list.get_best_match()