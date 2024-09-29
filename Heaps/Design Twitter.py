from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.userTweetMap = {}
        self.userFollowingMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        uTM = self.userTweetMap
        if userId not in uTM:
            uTM[userId] = []
        
        uTM[userId].append((self.time, tweetId))
        self.time-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        uTM, uFM = self.userTweetMap, self.userFollowingMap
        tweets = []

        if userId in uTM and len(uTM[userId])>0:
            tTime, _ = uTM[userId][-1]
            tPos = len(uTM[userId])
            heapq.heappush(tweets, (tTime, userId, tPos-1))

        followings = uFM.get(userId, [])
        
        for fi in followings:
            if fi in uTM and len(uTM[fi])>0:
                tTime, _ = uTM[fi][-1]
                tPos = len(uTM[fi])
                heapq.heappush(tweets, (tTime, fi, tPos-1))

        res = []
        while len(res)<10 and len(tweets)>0:
            tTime, uID, tPos = heapq.heappop(tweets)
            res.append(uTM[uID][tPos][1])
            if tPos>0:
                heapq.heappush(tweets, (uTM[uID][tPos-1][0], uID, tPos-1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        uFM = self.userFollowingMap
        if followerId not in uFM:
            uFM[followerId] = set()

        uFM[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        uFM = self.userFollowingMap
        if followerId in uFM:
            uFM[followerId].remove(followeeId)


if __name__ == "__main__":
    t = Twitter()
    t.postTweet(2, 5)

    t.follow(1, 2)
    t.follow(1, 2)
    

    print(t.getNewsFeed(1))