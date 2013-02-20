#Take a picture using python2/pygame and upload it to flickr
import time
import os
import pygame
from pygame import camera
from pygame.locals import *
import flickrapi


pygame.init()
pygame.camera.init()

#resolutions = [(600,480), (800,600), (1024,768), (1280,1024), (1920,1080)]

cam = pygame.camera.Camera("/dev/video0",(640,480))

#flickr api
api_key = ''
api_secret = ''

flickr = flickrapi.FlickrAPI(api_key, api_secret)

#flickr authentication
(token, frob) = flickr.get_token_part_one(perms = 'write')
if not token:
    raw_input("Press ENTER after you authorized this program")
flickr.get_token_part_two((token, frob))

while 1:
    filename = time.strftime("%a, %d, %b, %H:%M:%S")
    fileToSend = os.path.basename(filename + '.png')
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, fileToSend)
    cam.stop()
    flickr.upload(filename + '.png')
    os.remove(filename + '.png')
    time.sleep(60 * 10)



