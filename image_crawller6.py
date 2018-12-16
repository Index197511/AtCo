if __name__ =='__main__':
    save_dirpath='test'
    start_page='https://gihyo.jp/book/list'
    maximum_download=10
    crawller=Imagecrawller(save_dirpath,start_page,maximum_download)
    crawller.run()
