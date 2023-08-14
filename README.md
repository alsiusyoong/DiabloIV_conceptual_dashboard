# Diablo IV Conceptual Dashboard

## About 

Having spent more than 90 hours on the game, I wanted to pay tribute to my first Diablo game by creating a data project. Apart from tracking Diablo IV’s popularity, I want to focus on user telemetry, a player’s interaction with the game. Game telemetry consitutes any source of data obtained related to game development or game research. There are many game metrics in Diablo IV which I was particularly interested in due to a number of Reddit posts. Working with what I’ve got and know, I came up with 2 project ideas:

1. How do I track the the popularity of Diablo IV, or a game in general? (an attempt)
2. How do I use data to prove a point? (related to submissions on [r/diablo4] (https://www.reddit.com/r/diablo4/))

# Tracking the popularity of Diablo IV
I have never used pytrends, which is the unofficial API for Google Trends. I wanted to look at the search term for ‘Diablo IV’ to infer the overall popularity of the game. This is done using the pytrends.py file.

# Scraping Reddit using PRAW
The idea is to come up with a list of the top posts in r/diablo and see what opinions are being upvoted. There are many different ways to scrape Reddit, using the Pushshift API with PMAW or just plain and simple PRAW. Before you use PRAW, you will need to follow a series of steps to get create you Client ID and Client Secret Key. One thing to take note is that PRAW will by default, limit the number of search results to 100. However, you can set a parameter to increase that limit to 1,000. This is done using the reddit_PRAW.py file.

You can learn more about the idea behind this conceptual dashboard at https://www.notion.so/aloysiusong/Diablo-IV-Conceptual-Dashboard-339924e41acd48fb9a2751452087035b?pvs=4

![alt text](https://github.com/alsiusyoong/DiabloIV_conceptual_dashboard/blob/main/DiabloIV_socialMediaTracker.png)
