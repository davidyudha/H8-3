from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=7s7zIv52NNU').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=7s7zIv52NNU')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
