import ffmpeg

input_video = ffmpeg.input('../example/video_short.mp4')
audio = input_video.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)