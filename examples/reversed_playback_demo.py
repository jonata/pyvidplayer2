'''
This example shows how you can play videos in reverse

IMPORTANT:
Playing videos in reverse requires a large amount of memory
This particular example needs around 1.3gb
Reversing longer videos can temporarily brick your computer if there isn't enough memory
'''


from pyvidplayer2 import Video

v = Video(r"resources\birds.avi", reverse=True).preview()