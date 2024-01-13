from instabot import Bot
bot = Bot()
bot.login(username = "username_of_account",password = "password")
bot.follow("Give_ID_of_account_to_be_followed")  #==> follow an account with given username
bot.upload_photo("C:/Users/joshi/OneDrive/Pictures/Saved Pictures/python.webp",caption="python Insta Bot Demo")
bot.unfollow("Give_ID_of_account_to_be_unfollowed")  #==> accoun to be unfollowed
bot.send_message("text message to check if bot is working", ["user1","user2","user3"])

#get list of followers with details
followers = bot.get_user_followers("username_of_account")
for i in followers:
    print(bot.get_user_info(i))

#get list of following with details
following = bot.get_user_following("username_of_account")
for j in following:
    print(bot.get_user_info(j))
