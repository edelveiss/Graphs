import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        # lookup table for User Objects given IDs
        self.users = {}
        #Adjacency List
        #Maps user_ids to a list of other users who are their friends
        self.friendships = {}

    def print_users(self):
        for user in self.users:
            print(user)

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        # Add users
        for i in range(num_users): #O(len(num_users))
            self.add_user(f"User {i}")

        # self.print_users()

        # Create friendships
        # we will generate all possible friendships
        possible_friendships = []

        #avoid duplicates by only creating friendships where user1 < user2
        # n = len(num_users)
        #O(n^2)
        for user in self.users: #O(n)
            #for friend_id in range(user_id + 1, len(self.users.keys())+1):
            for friend in range(user +1, self.last_id +1): #O(n-1)(worst case) -> O(n-2) -> O(n-3)...=>O(n/2) average, so O(n)
                possible_friendships.append((user, friend))

        # shuffle friendships
        random.shuffle(possible_friendships)

        random_friendships = num_users * avg_friendships // 2
       
        #O(n*m/2), if m=n, O(n^2/2)
        for i in range(random_friendships):
            user, friend = possible_friendships[i]
            self.add_friendship(user, friend)

    def add_friendship_linear(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def populate_graph_linear(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # !!!! IMPLEMENT ME

        target_friendships = (num_users * avg_friendships)
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship_linear(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        
        print(f"Collisions: {collisions}")


    def get_neighbors(self, user_id):
        return self.friendships[user_id] if user_id in self.friendships else set()

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        #O(n) where n is a number of nodes in the graph
        # using bft algorithm for finding the shortest path
        visited = {}  # Note that this is a dictionary, not a set
        queue = deque()
        queue.append([user_id])

        while len(queue) > 0:
            path = queue.popleft()
            current = path[-1]
            if current not in visited:
                visited[current] = path
                

                for friend in self.get_neighbors(current):
                    # copy_path = path.copy()
                    copy_path = list(path)
                    copy_path.append(friend)
                    queue.append(copy_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph_linear(10, 2)
    # sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)


 #To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why? 100*10//2 = 500 because add_friendship(1, 2) is the same as add_friendship(2, 1). To avoid duplicates first user< second user