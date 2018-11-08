# video_to_image_tool
a video to image tool to generate dataset

## usage
python convertor.py convertor.py \<video filename\> \<concat_axis\> \<concat_size\> \<frame range\> \<frame clip\> \<resize\>

ex.

python convertor.py "v1.mp4" 1 3 "100,120" "0,320,720,960" "640,640"



### \<video filename\>
video filename (string)

ex. "video.mp4"

### \<concat_axis\>
Image concatenate axis. 

0: vertically concatenate

1: horizontally concatenate

### \<concat_size\>
Image concatenate window size. 

ex. 3

###  \<frame range\>
starting and ending frame number 

ex. "100,120"

### \<frame clip\> 
clip each frame by describing y1,x1,y2,x2

ex. "0,320,720,960"

### \<resize\>
resize the frame which run after th clip process and before the concatenation

ex. "640,640"


