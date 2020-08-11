from time import sleep
from InstagramAPI import InstagramAPI

user = input('Username : ')
password = input('Password : ')
api=InstagramAPI(user,password)
api.login()

'''
-------------------------------
---------UNFOLLOW--------------
-------------------------------

'''

users_list = []
# followers_cloutaward1 = []
# my_followers = []
my_following = []
following_users = []
'''
def follow_users(users_list):
    api.login()
    api.getSelfUsersFollowing() # Get users which you are following
    result = api.LastJson
    for user in result['users']:
        following_users.append(user['pk'])
    for user in users_list:
        if not user['pk'] in following_users: # if new user is not in your following users
            print('Following @' + user['username'])
            api.follow(user['pk'])
            # after first test set this really long to avoid from suspension
            sleep(20)
        else:
            print('Already following @' + user['username'])
            sleep(10)
            
'''

'''
def get_likes_list(username):
    api.login()
    api.searchUsername(username)
    result = api.LastJson
    username_id = result['user']['pk'] # Get user ID
    user_posts = api.getUserFeed(username_id) # Get user feed
    result = api.LastJson
    media_id = result['items'][0]['id'] # Get most recent post
    api.getMediaLikers(media_id) # Get users who liked
    users = api.LastJson['users']
    for user in users: # Push users to list
        users_list.append({'pk':user['pk'], 'username':user['username']})
'''
def get_followers_list(username):
    followers = []
    # api.login()
    api.searchUsername(username)
    result = api.LastJson
    username_id = result['user']['pk'] # Get user ID
    user_followers = api.getUserFollowers(username_id)
    result = api.LastJson
    for i in result['users']:
        # if {'pk':i['pk'], 'username':i['username']} not in followers:
        followers.append({'pk':i['pk'], 'username':i['username']})
    print (len(result['users']))
    return followers

def get_following_list(username):
    following = []
    # api.login()
    api.searchUsername(username)
    result = api.LastJson
    username_id = result['user']['pk'] # Get user ID
    user_followers = api.getUserFollowings(username_id)
    result = api.LastJson
    for i in result['users']:
        # if {'pk':i['pk'], 'username':i['username']} not in following:
        following.append({'pk':i['pk'], 'username':i['username']})
    print (len(result['users']))
    return following

'''

def follow_users(users_list):
    api.login()
    api.getSelfUsersFollowing() # Get users which you are following
    result = api.LastJson
    for user in result['users']:
        following_users.append(user['pk'])
    for user in users_list:
        if not user['pk'] in following_users: # if new user is not in your following users
            print('Following @' + user['username'])
            api.follow(user['pk'])
            # after first test set this really long to avoid from suspension
            sleep(20)
        else:
            print('Already following @' + user['username'])
            sleep(10)
            
'''

if __name__ == '__main__':
    # get_followers_list('cloutboosted')
    while (1):
        # followers_cloutaward1  = get_followers_list('cloutaward1')
        # sleep(20)
        my_followers = get_followers_list('_n__anghel')
        sleep(20)
        my_following = get_following_list('_n__anghel')
        sleep(20)
        for i in my_following:
            # if i in followers_cloutaward1:
            if i not in my_followers :
                print('Unfollowing @' + i['username'])
                api.unfollow(i['pk'])
                sleep(60)
            else:
                print('User @' + i['username'] + 'is following me')
        break
            # else:
            #     print('User @' + i['username'] + 'is not following cloutaward1')
    # follow_users(users_list)


