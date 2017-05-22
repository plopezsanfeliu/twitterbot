import tweepy
from models import TwitterUser

class Bot():
    __slots__ = ['__consumer_key', '__consumer_secret', '__access_token',
                 '__access_token_secret', '__auth', '__api']

    def __init__(self, db, classifier, logger):
        self.__consumer_key = "cNbkKHve3645xLIVgJjQbrWg6"
        self.__consumer_secret = "B1SWKCIMFQjhh3Y5YGstKMvl8t7IAPTha1jxXy5b3IC6K8wz7w"
        self.__access_token = "3720533727-cBbDc2bDnDSU6f9SuC3ti4oQcfTkMk7VbVmh9ZW"
        self.__access_token_secret = "k2aioMNx3tCfw6jW9teksQ98WllWbKogVQF4YW0sRYTuW"

        self.__auth = tweepy.OAuthHandler(self.__consumer_key,
                                          self.__consumer_secret)
        self.__auth.set_access_token(self.__access_token,
                                     self.__access_token_secret)

        self.__api = tweepy.API(self.__auth)

    def getTweets(self, n_tweets):
        userList = TwitterUser.objects.all()

        for user in userList:
            print user
            #self.__db.addTweets(self.getTweetsByName(user, n_tweets))

    def getTweetsByName(self, name, number):
        tweetList = []  # llista de llistes amb tweets + info
        tweetInfo = []  # llista amb tweet + info associada

        tweets = self.__api.user_timeline(screen_name=name, count=number)

        for status in tweets:
            tweetInfo = []
            tweetInfo.append(status.id)
            tweetInfo.append(status.author.screen_name)
            tweetInfo.append(status.author.name)
            tweetInfo.append(status.lang)
            tweetInfo.append(status.retweet_count)
            tweetInfo.append(status.favorite_count)
            tweetInfo.append(status.coordinates)
            tweetInfo.append(status.text.replace('"', "\""))
            tweetInfo.append(status.created_at.strftime("%Y/%m/%d"))
            tweetInfo.append(status.created_at.strftime("%H:%m:%S"))
            tweetList.append(tweetInfo)

        return tweetList

    def getTrendingTopics(self):
        """Retorna una llista de Python amb els 10 Trending Topics."""
        trends1 = self.__api.trends_place(1)
        data = trends1[0]
        trends = data['trends']
        names = [trend['name'] for trend in trends]

        trendingTopics = []
        for name in names:
            trendingTopics.append(str(name))

        return trendingTopics

    def flushTweets(self):
        self.__db.flushTweetTable()
        self.__logger.info("Flush de tweets a BD")

    def classifyTweets(self):
        self.__classifier.classify()

    def reclassifyAll(self):
        self.__classifier.reclassifyAll()


def main():
    print "model working..."


if __name__ == "__main__":
    main()