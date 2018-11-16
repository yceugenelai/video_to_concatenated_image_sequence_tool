import sys
import imageio
import numpy as np
from skimage.transform import resize
import os

def simple_image_concat(filename , save_name, img_list, concat_axis):
	i_new = np.concatenate(tuple(img_list), axis=concat_axis)
	imageio.imwrite(filename + "/" + str(save_name) + ".jpg", i_new[:, :, :])


def video_to_dataset(filename, concat_axis, concat_size, frame_range = [0,-1] , frame_clip=[0,0,-1,-1]
	, frame_resize=[-1,-1]):
	reader = imageio.get_reader(filename,  'ffmpeg')
	img_list = []

	filename = os.path.splitext(filename)[0]

	if not os.path.exists("./" + filename):
		os.makedirs(filename)	

	save_file_count = 1
	for i, im in enumerate(reader):
		if i % 1000 == 0:
			print(i, im.shape)
		if i >= frame_range[0]:
			if len(img_list) >= concat_size:
				img_list.remove(img_list[0])

			if frame_clip != [0,0,-1,-1]:
				tmp_im = im[frame_clip[0]:frame_clip[2],frame_clip[1]:frame_clip[3],:]
			else:
				tmp_im = im
				
			if frame_resize != [-1,-1]:
				tmp_im = resize(tmp_im, (frame_resize[0], frame_resize[1]), anti_aliasing=True)			
			
			img_list.append(tmp_im)
			if len(img_list) == concat_size:
				simple_image_concat(filename, save_file_count, img_list,concat_axis)
				save_file_count = save_file_count + 1
		if frame_range[1] != -1 and i >= frame_range[1]:
			break

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("convertor.py <video filename> <concat_axis> <concat_size>")
	else:
		frame_range = [0,-1]		
		if len(sys.argv) > 4:
			if sys.argv[4] != "":
				frame_range = [int(i) for i in sys.argv[4].split(",")]		
			
		frame_clip = [0,0,-1,-1]
		if len(sys.argv) > 5:
			if sys.argv[5] != "":
				frame_clip = [int(i) for i in sys.argv[5].split(",")]	
			
		frame_resize = [-1,-1]
		if len(sys.argv) > 6:
			if sys.argv[6] != "":			
				frame_resize = [int(i) for i in sys.argv[6].split(",")]	

		print(type(sys.argv[1]), int(sys.argv[2]) ,int(sys.argv[3]), frame_range,frame_clip,frame_resize)
		video_to_dataset(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), frame_range,frame_clip,frame_resize)		
	#video_to_dataset("v1.mp4",1, 3, [100,110],[0,320,720,960],[-1,-1])

