'''
This example shows how videos can be queued and skipped through with the VideoPlayer object
'''

import pygame
from pyvidplayer2 import VideoPlayer, Video

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("queue demo")

vid = VideoPlayer(Video(r"resources\clip.mp4"), (0, 0, 1280, 720), loop=True)

vid.queue(Video(r"resources\ocean.mkv"))
vid.queue(Video(r"resources\birds.avi"))


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            vid.close()
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            vid.skip()
    
    pygame.time.wait(16)
    
    vid.update(events)
    vid.draw(win)
    
    pygame.display.update()