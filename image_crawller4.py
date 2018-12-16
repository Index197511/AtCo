def get_image_url_list(self,url_list):
    try:
        image_url_list=[]
        for url in url_list:
            if url in self.stocked_url:#既出か確認
                continue

            if '.jpg' in url:
                image_url_list.append(url)
            elif '.png' in url:
                image_url_list.append(url)
            elif '.gif' in url:
                image_url_list.append(url)
            else:
                self.crawl_url_list.append(url)#画像でないならURLの取得

            self.stocked_url.add(url)

        return image_url_list

    except Exception as e:
        print('Error:{}'.format(e))
        return []
