class Twitter:
    
    def __init__(self):
        self.tweets = {}   
        self.followers = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets: self.tweets[userId].append((self.count, tweetId))
        else: self.tweets[userId] = [(self.count, tweetId)]
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, maxHeap = [], []
        if userId not in self.followers: self.followers[userId] = set()
        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(maxHeap, (-count, tweetId, followeeId, idx - 1))
        while maxHeap and len(res) < 10:
            _count, tweetId, followeeId, idx = heapq.heappop(maxHeap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(maxHeap, (-count, tweetId, followeeId, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers: self.followers[followerId].add(followeeId)
        else: self.followers[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
