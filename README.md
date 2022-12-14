# every-frame-twitter-bot
A Twitter bot to post every frame of a given .mp4 file.
<img align="right" src="https://media1.giphy.com/media/AKyXh7Zmx5UbpCz9nc/200w.gif?cid=82a1493bcy1mpewn49orxr1jf5h27o4b1avt5bbwyzvayivm&rid=200w.gif&ct=s" width = "266" height = "266">

## Setup
<i> This Twitter bot assumes you already have a Twitter developer account and have 'Elevated' access. </i>
### Requirements
This bot requires OpenCV and Tweepy to work. You can install them by using:
```
pip install -r requirements.txt
```
### Credentials
In the repository, there is a ```credentials.txt``` file. Fill in the fields with your Twitter API information and change the extensions to .py. The code will expect this file and pull in the values to use in authentication. Once again, you <b>MUST</b> have elevated access to Twitter's API to use this bot.
### Video Frames Generation
In the repository, there is a ```generate_frames.py``` file. In order to generate all the frames from your chosen mp4 file, first move the file inside the repository. Then run:
```
python generate_frames.py video_filepath frame_offset
```
<img align="left" src="https://giffiles.alphacoders.com/112/11288.gif" width = "200" height = "200">

The argument `video_filepath` is the filepath to the video you want to turn into a series of frames. The `frame_offset` argument is how fine you want the frame splicing to be. This argument is an integer, and will only choose every `frame_offset`'th frame to turn into a jpg file. If you want the frames as is (which might be necessary with videos with a slower framerate), simply put "1" as the argument.
<i><b>The generation process can take awhile especially on slower machines. If your video is excessively long or has a very high framerate, please consider this before running the program.</b></i>

### Constants
In the repository, there is a ```constants.txt``` file. Fill in the fields with information regarding your video, such as how many frames you have to sort through (the first frame will start at "frame0.jpg"), the video title, and the frequency of Twitter posting. Along with this there is a field for ```FILEPATH```. This fields is primarily for people who are running this code on servers who need absolute filepaths to run the code. If this does not apply to you, you can simply leave it as an empty string. If you <b>ARE</b> running this code on said server, fill the field out with the filepath where this repository is stored and where you are grabbing your frames from. Change the extension to ```.py``` after completion.

### Starting Frame
There is a file entitled ```last_frame.txt```. This file will be written to with the frame number that was last tweeted. This is specifically designed for programs that will have this bot always run in case the program crashes. Instead of starting over, the bot will continue from the last frame tweeted. It is set to -1 currently, but you can change this value if you would like to start the bot at a specific frame number.

### Deploying
To deploy the bot, simply run the ```main.py``` file, such as using the command:
```
python main.py
```
Your constants and credentials will be pulled in and the bot will run with your specifications. The bot will run for as long as it takes to post every frame. Due to the longevity of some videos, it is recommended to use a server to host the code so that it will run for as long as needed.

# License
This bot is under a [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use this bot for any purpose. Credit is not needed but is appreciated.

<p align="center">
<img align="center" src="https://benlilley.neocities.org/fmf.gif" width = "250" height = "200">
</p>
