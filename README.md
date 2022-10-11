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

<i>***As a word of caution - the generation process can take awhile especially on slower machines. If your video is excessively long or has a very high framerate, please consider this before running the program.</i>

### Constants
In the repository, there is a ```constants.txt``` file. Fill in the fields with information regarding your frames, such as how many frames you have to sort through. Along with this there is a field for ```FILEPATH```. This field is primarily for people who are running this code on servers who need absolute filepaths to run the code. If this does not apply to you, you can simply leave it as an empty string. If you <b>ARE</b> running this code on said server, fill that field out with the filepath where this repository is stored.

***TBD***
