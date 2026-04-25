class Twitter:

    def __init__(self):
        self.friendship = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None: #Publih a new tweet with ID tweetId by the userId. Each tweetId is unique 
        #I could just have a class variable hashmap that has the correspondance between userID and tweetID
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #This is where the heap will come in. I imagine we will need to find all the users friends and then the users posts. Once we have those we can populate a heap and pop 10 
        heap = []

        for i in range(len(self.posts[userId])):
            heapq.heappush(heap, self.posts[userId][i])
            if len(heap) > 10:
                heapq.heappop(heap)

        for friend in self.friendship[userId]:
            for i in range(len(self.posts[friend])):
                heapq.heappush(heap, self.posts[friend][i])
                if len(heap) > 10:
                    heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None: #Follow the user
        if followerId != followeeId and followeeId not in self.friendship[followerId]:
            self.friendship[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None: #unfollow the user
        if followeeId in self.friendship[followerId]:
            self.friendship[followerId].remove(followeeId)
        

#We could have a hashmap that stores the correspondance between a user and their tweets
#We will have a global time variable that will be updated each time a tweet is made. The higher the value the more recent
#We need to maintain the relationships, which we can do by using a graph. 
#When the user wants to getNewsFeed, we can go through all the friends posts and the individuals posts and populate a heap up to 10 