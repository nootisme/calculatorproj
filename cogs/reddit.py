from discord.ext import commands
from discord.utils import get
import asyncpraw
import random


#praw

reddit = asyncpraw.Reddit(

)

#disc


class RedditEvents(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command() # call client event (if CMD add para)
    async def hello(self, ctx): # the name is the func name, plus ctx is the paramater
        await ctx.send("Nooty Noot says hello back.") # result

    @commands.command()
    async def deals(self, ctx):
        sub = await reddit.subreddit("deals")
        hotPosts = sub.hot(limit=1000)
        all_subs = []

        # var ^
        # question 
        

        async for submission in hotPosts:
            all_subs.append(submission)
                
        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        await ctx.send(name)
        await ctx.send(url)


    @commands.Cog.listener()
    async def onMemberJoin(self, member):
        print('Log: User Joined: ' + member)

    @commands.Cog.listener()
    async def onError(self, ctx, error):
        print(ctx.command.name + "was executed incorrectly.")
        print(error)


def setup(bot):
    bot.add_cog(RedditEvents(bot))
