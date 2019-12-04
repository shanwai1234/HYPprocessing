import os
import numpy as np
import cv2
import zipfile

def merge(args, filename):
	'''
	myfolder contains all individual images generated from Lemnatec system
	'''
	mlist = os.listdir(args)
	try: # removing non-image files in the folder
		mlist.remove('0_0_0.png')
		mlist.remove('1_0_0.png')
	except ValueError:
		print "No 0_0_0 and 1_0_0 files existing!"

	tlist = [int(x.split('_')[0]) for x in mlist]

	init_img = cv2.imread('{0}/{1}'.format(args,'2_0_0.png')) # get uniform image size for hyperspectral image
	height = init_img.shape[0]
	width = init_img.shape[1]
	band = len(tlist)

	num = 1
	for h in sorted(tlist):
		name = str(h) + '_0_0.png'
		img = cv2.imread('{0}/{1}'.format(args,name))
		if num == 1:
			img3c = img[:,:,0]
		else:
			img3c = np.dstack((img3c,img[:,:,0])) # create 3 channels for HYP image through merging 243 channels
		num += 1

	np.save(filename, img3c)

