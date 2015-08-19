# coding: utf-8
import requests, re, os
from manager import randomStr

openurls = 'http://desk.zol.com.cn/bizhi'
list_pic_result = []


def downloadpic(pic_url):
    if not os.path.exists("/Users/lonres/Pictures/webpage/" + pic_url[str(pic_url).rfind('/'):]):
        r = requests.get(pic_url, stream=True)
        with open("/Users/lonres/Pictures/webpage/" + pic_url[str(pic_url).rfind('/'):], 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
            f.close()


def ispic(url):
    ''
    if url[str(url).rfind('.'):] < 5 and url[str(url).rfind('.'):] != 'html' and str(url).startswith('http'):
        return True
    else:
        return False


def download_img(web_url, url_list=[]):
    result = requests.get(web_url)
    img_url = re.findall(r'<img id="bigImg" src="(\S*960x600\S*)"', result.text, re.M)
    if img_url and isinstance(img_url, list):
        for url in img_url:
            if not url in url_list:
                print img_url
                url_list.append(url)
                downloadpic(url)
    elif img_url and isinstance(img_url, str) and not img_url in url_list:
        print img_url
        url_list.append(img_url)
        downloadpic(img_url)
    urllist = re.findall(r'href="(\S*)"', result.text, re.M)
    for urls in urllist:
        try:
            urls = str(urls)
            if urls.rfind('.') > 0:
                if len(urls[urls.rfind('.'):]) > 3 and len(urls[urls.rfind('.'):]) < 6 and not urls[
                        urls.rfind('.'):] in [
                    '.php', '.css', '.js', '.gif', '.cn/']:
                    if urls.startswith('http') and not urls in url_list:
                        print urls
                        url_list.append(urls)
                        download_img(urls)
                    elif urls.startswith('/') and not (openurls + urls) in url_list:
                        print openurls + urls
                        url_list.append(openurls + urls)
                        download_img(openurls + urls, urllist)
        except UnicodeEncodeError:
            pass




download_img(openurls)

