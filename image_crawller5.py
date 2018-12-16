def save_images(self,image_url_list):
    for image_url in image_url_list:
        try:
            #決められた回数以上DLしたら終了
            if self.download_counter>=self.maximum_download:
                return

            #イメージを取得
            response=requests.get(image_url,stream=True)
            image=response.content

            #イメージをファイルに保存
            file_name=image_url.split('/').pop()
            save_path=os.path.join(self.save_dirpath,file_name)
            fout=open(save.path,'wb')
            fout.write(image)
            fout.close()

            self.download_counter+=1
            print('saved image:{}/{}'.format(self.download_counter,self.maximum_download))

        except Exception as e:
            print('Error:{}'.format(e))
