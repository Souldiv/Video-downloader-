from __future__ import unicode_literals
import youtube_dl
import os
import requests
#Master dictionary--will be expanding in future iterations of the project
#mark-1 of Tube.py
master={
 'Audio':{

 'format': 'bestaudio/best',
'noplaylist':True,
'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
         }]
},
'Video':{
'format': 'bestvideo+bestaudio/best',
'noplaylist':True,
'postprocessors': [{
        'key': 'FFmpegVideoConvertor'
                             }],
},
'list':{
    'listsubtitles':True
    },
'listformat':{
    'lisformats':True
    }
}

def Net():                                                                                                  #check if the user has connected to the internet
    try:
        requests.get("https://www.google.com",timeout=5)
        return True
    except:
        print("Please connect to the Internet")
        return False

def check(link):                                                                                        #checking the validity of the link
    try:
        requests.get(link)
        return True
    except:
        print('Bad link')
        return False

def download(link,data):                                                                        #helper function to download
    #  try:
        with youtube_dl.YoutubeDL(data) as ydl:
             ydl.download([link])
    #  except:
    #      print("File coud not be downloaded. Try again later.")

def main():
    if Net():
        link=input("Enter the link: ")
        if check(link):
            print("1.Download an audio playlist")
            print("2.Download a Video playlist")
            print("3.Download a Single Audio")
            print("4.Download a single video file")
            ch=int(input("Enter your choice: "))
            if ch in [1,2,3,4]:
                if ch==1:
                    master['Audio']['noplaylist']=False
                    download(link,master['Audio'])
                elif ch==2:
                    master['Video']['noplaylist']=False
                    download(link,master['Video'])
                elif ch==4:
                    download(link,master['Video'])
                else:
                    download(link,master['Audio'])
            else:
                print("Bad choice")

if __name__=="__main__":
    main()
