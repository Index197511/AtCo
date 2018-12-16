def get_abs_urls(selfs,url):
    try:
        #URLから文字列のHTMLを取得する
        response=requests.get(url)
        html=response.text

        #HTMlからURLを抜き出してリストに格納
        rerative_url_list=re.findall('<a href="?\'?([^"\'>]*)',html)


        #相対URLを絶対URLに変換
        abs_url_list=[]
        for rerative_url in rerative_url_list:
            abs_url=urllib.parse.urljoin(url,rerative_url)
            if abs_url.startswith('http://') or abs_url.startswith('https://'):
                abs_url_list.append(abs_url)

        return abs_url_list

    except Exception as e:
        print('Error: {}'.format(e))
        return[]
