class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets: self.tweets[userId] = []
        self.tweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followerSet, heap = set(), []
        if userId in self.followers: followerSet = self.followers[userId].copy()
        followerSet.add(userId)
        for user in followerSet:
            tweets = []
            if user in self.tweets: tweets = self.tweets[user]
            for count, tweet in tweets:
                heapq.heappush(heap, (count, tweet))
                if len(heap) > 10: heapq.heappop(heap)
        res = []
        while heap: res.append(heapq.heappop(heap)[1])
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers: self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
