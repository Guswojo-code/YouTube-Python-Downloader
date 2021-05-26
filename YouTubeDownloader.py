from pytube import YouTube 
#Before this will work you need to go to commandprompt and write pip install pytube

Link = input("Your youtube link: ")

yt = (Link)

w = YouTube(yt).streams.first()
w.download(output_path="Choose your folder") #Output folder
print("Made one new file from " + yt)
