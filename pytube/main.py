from pytube import YouTube

def on_complete(stream,file_path):
    print(file_path)
    print(stream)

def on_progress(stream, chunk, bytes_remaining):
    print('progress')

video_object = YouTube(
    'https://www.youtube.com/watch?v=q_pOh8ISa0g', 
    on_complete_callback = on_complete,
    on_progress_callback = on_progress)

# video info
#print(video_object.title)
#print(video_object.views)
#print(video_object.length)
#print(video_object.description)

# video streams
for stream in video_object.streams:
    print(stream)

#print(video_object.streams.get_highest_resolution())
#print(video_object.streams.get_audio_only())

# downloads
video_object.streams.get_by_itag(140).download(output_path='/Users/phillipcarman/Desktop')