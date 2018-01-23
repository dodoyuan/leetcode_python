from collections import defaultdict
class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.post_twitter = defaultdict(list)   # userId -> tweetId
        self.follow_map = defaultdict(set)     # userId -> followee
        self.time = 0



    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.time += 1
        self.post_twitter[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        allmessage = []
        allmessage.extend(self.post_twitter[userId])
        for user in self.follow_map[userId]:
            allmessage.extend(self.post_twitter[user])
        smessage = sorted(allmessage, key=lambda item: item[0], reverse=True)[0:10]
        return [item[1] for item in smessage]



    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId != followerId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId != followerId:
            self.follow_map[followerId].discard(followeeId)
