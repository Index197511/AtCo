def callback(status: tweepy.Status):
    if (not status.retweeted) and ("RT @" not in status.text):
        for i, j in class_dict.items(): # i, j = key, value

            if i in status.text:
                tweet = "@" + str(status.user.screen_name) + "\n" + \
                        Class_list.get(str(j))
                api.update_status(tweet, str(status.id))
                api.create_favorite(str(status.id))
                break

        else:
            tweet = "@" + str(status.user.screen_name) + "\n" + \
                    "にゃーん"
            api.update_status(tweet, str(status.id))
            api.create_favorite(str(status.id))
