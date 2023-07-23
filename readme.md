## instalation

		https://docs.ultralytics.com/quickstart/#install-ultralytics

## preparation data custom

- download model pretraining

		https://github.com/ultralytics/ultralytics

- using labelImg

		$ pip install labelImg

- make your own dataset 
- save label in folder labels
- copy classes.txt in labels to root folder
- separate result labeling in train and val 
- change data_custom.yaml with your own dataset

		- datasets	[magic folder in linux]
			- train
				+ images
				+ labels
			- val
				+ images
				+ labels
		data_custom.yaml
		classes.txt
		yolov8m.pt


## train:

	yolo task=detect mode=train epochs=100 data=data_custom.yaml model=yolov8m.pt imgsz=640

## detect
- copy best.pt from runs folder to root folder
- run image.py or video.py

## look at the tutorial video

	https://www.youtube.com/watch?v=gRAyOPjQ9_s

### author
	Danu Andrean
