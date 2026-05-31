import requests
import os
import time
import numpy as np
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/6.0_2/bin/ffmpeg"
os.environ["IMAGEIO_IMAGEMAGICK_BINARY"] = "/opt/homebrew/Cellar/imagemagick/7.1.1-23/bin/convert"
import random
import moviepy.editor
from moviepy.video.fx.all import crop
from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip, AudioFileClip, CompositeAudioClip
import whisper
import whisper_timestamped
from gtts import gTTS

from getposts import posts

#Audio
redditPost = str(posts)
tts = gTTS(redditPost, lang='en', tld='us')
tts.save('output.mp3')

# Grab clips
length = 59

clip = moviepy.editor.VideoFileClip('Clip.mp4')
cropped_clip = crop(clip, width=1280, height=720, x_center=640, y_center=360)

# Ensure start and end times are within valid ranges
start = max(0, min(round(random.uniform(0, cropped_clip.duration - length), 2), cropped_clip.duration - length))
end = start + length

# Ensure the end time does not exceed the duration of the cropped video
end = min(end, cropped_clip.duration)

out_clip = cropped_clip.subclip(start, end)

# Load audio and trim it to match the duration of the video segment
audio_clip = moviepy.editor.AudioFileClip("output.mp3")

# Ensure that the audio duration matches the duration of the video segment
audio_duration = min(out_clip.duration, audio_clip.duration)

audio = audio_clip.subclip(0, audio_duration)

#Music
music_clip = moviepy.editor.AudioFileClip("music.mp3")
music_duration = min(out_clip.duration, music_clip.duration)
music = music_clip.subclip(0, music_duration)

finalaudio = CompositeAudioClip([audio, music])

# Set the audio of the video segment
videoclip = out_clip.set_audio(finalaudio)
videoclip.audio = finalaudio

#Subtitles
model = whisper_timestamped.load_model('base')
whisperaudio = 'output.mp3'
results = whisper_timestamped.transcribe(model, whisperaudio)

# Create an empty list to store subtitle clips
subs = []
subs.append(videoclip)
for segment in results['segments']:
    for word in segment['words']:
        text = word['text'].upper()
        start = word['start']
        end = word['end']
        duration = end - start
        txt_clip = TextClip(txt=text, fontsize=50, font='SF-Arabic-Bold', stroke_width=2, color='white', stroke_color='black')
        txt_clip = txt_clip.set_pos(('center', 'center')).set_start(start).set_duration(duration)
        subs.append(txt_clip)

#Add subs and create video
videoclip = CompositeVideoClip(subs)
videoclip.write_videofile("output.mp4")

audio_clip.close()
clip.close()
videoclip.close()