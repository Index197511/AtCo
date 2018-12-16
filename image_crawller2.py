def run(self):
    while True:
        #処理1　探索するURLが無ければ終了、規定数を集めていても終了
        if len(self.crawl_url_list)==0:
            break
        if self.download_counter>=self.maximum_download:
            break

        #処理2　次に調べるHTMLのURLを取得
        crawl_url=self.crawl_url_list.pop(0)

        #処理3　HTMLページからURLを抽出
        urls=self.get_abs_urls(crawl_url)

        #処理4　URLをイメージとHTMLに分類、イメージを返す
        image_url_list=self.get_image_url_list(urls)

        #処理5　リストに格納されたイメージを保存する
        self.save_images(image_url_list)

        print('finished')
