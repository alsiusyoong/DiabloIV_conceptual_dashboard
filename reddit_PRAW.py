#Import modules
#--------------------------------------
import praw #to access Reddit
import requests #Might not need this
from praw.models import MoreComments #access Reddit comments
import sys #for .translate bmp code
import regex #regex matching
import datetime #converting timestamps
from pathlib import Path


#Assign Reddit Credentials
#---------------------------------------
r = praw.Reddit(client_id = "CLIENT_ID",
                client_secret = "CLIENT_SECRET",
                user_agent = "USER_AGENT")

print("Credentials have been accepted")

#Assign Subreddit
#------------------------------
# print("What subreddit are we mining through today?")
chosen_sub = "diablo4"
subreddit = r.subreddit(chosen_sub)
# print("Thanks")

#Create list to store submissions
subs = []
subCount = 0
sub_entries = {}

print("Placeholders have been assigned")

#Collect submission ids
#------------------------------
#For each submission within selected subreddit
    #sort – Can be one of: relevance, hot, top, new, comments. (default: relevance).
    #time_filter – Can be one of: all, day, hour, month, week, year (default: all).
print("And what are we searching for in this subreddit?")
sub_query = "."
#For most endpoints this results in 100 items per request.
#If you want to retrieve as many as possible pass in limit=None.
for submission in subreddit.search(sub_query, sort='top', time_filter='month', limit=None):
    subs.append(submission.id)
    subCount+=1


#Test list of submission ids
print(str(subCount) + " submissions have added to list")
print("1st entry is:")
print(r.submission(id=str(subs[0])).title + " created: " + str(datetime.datetime.fromtimestamp(r.submission(id=str(subs[0])).created)))
print("Last entry is:")
print(r.submission(id=str(subs[subCount-1])).title + " created on: " + str(datetime.datetime.fromtimestamp(r.submission(id=str(subs[subCount-1])).created)))

    
#Build Extract key submission data
def collectSubData(submission):
    post = r.submission(id=submission) #Access subreddit post based on submission id
    subData = list() #list to store key data of submission
    title = post.title
    url = post.url
    flair = post.flair
    author = post.author
    unique = post.id
    score = post.score
    bodytext = post.selftext
    created = datetime.datetime.fromtimestamp(post.created) #e.g. 1520561700.0 which can be converted later
    upratio = post.upvote_ratio
    topcommsCnt = len(post.comments)
    allcommsCnt = len(post.comments.list()) #or len(post.num_comments)
    
    subData.append((unique,title,bodytext,url,author,score,created,upratio,topcommsCnt,allcommsCnt,flair))
    sub_entries[unique] = subData

#Run Submission Data Extraction
#---------------------------------------
print("Shall begin collecting data on Submissions...")
for submission in subs:
    collectSubData(submission)

print("Submissions have been collected")
print(str(len(sub_entries)) + " entries have been added to the dictionary")

#Save submission Data in file
#---------------------------------------------
def updateSubs_file():
    upload_count = 0
    import csv
    # location = Path("C:/Users/Aloy/OneDrive/Desktop")
    # print("diablo4.csv") #don't forget to assign filetype
    # filename = input()
    file = Path("PATH_WHERE_YOU_WANT_THE_FILE")
    with open(file, 'w', encoding="utf-8", newline='') as file: #if you encounter encoding error use > encoding="utf-8"
        a = csv.writer(file, delimiter=',')
        headers = ["Post ID","Title","Selftext","Url","Author","Score","Publish Date","Upvote Ratio","Total No. of Top Comments","Total No. of Comments","Flair"]
        a.writerow(headers)
        for sub in sub_entries:
            a.writerow(sub_entries[sub][0])
            upload_count+=1
            
        print(str(upload_count) + " submissions have been uploaded")

updateSubs_file()