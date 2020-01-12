# Import the needed libraries
import cv2

class Camera():
	def __init__(self, camera_type=0, camera_id=1, flip=0, width, height, fps=24, enforce_fps = False)
		# intialize all variables
		self.fps = fps
		self.camera_type = camera_type
		self.camera_id = camera_id
		self.flip_method = flip
		self.width = width
		self.height = height
		self.enforce_fps = enforce_fps

		# create the OpenCV camera inteface
		self.cap = None

		# open the camera interface
		self.open()

	def csi_pipeline (self) :   
	    return ('nvarguscamerasrc ! ' 
	    'video/x-raw(memory:NVMM), '
	    'width=(int)%d, height=(int)%d, '
	    'format=(string)NV12, framerate=(fraction)%d/1 ! '
	    'nvvidconv flip-method=%d ! '
	    'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
	    'videoconvert ! '
	    'video/x-raw, format=(string)BGR ! appsink'  % (self.width, self.height, self.fps, self.flip_method, self.width, self.height))

	def usb_pipeline (camara_type="/dev/video1", capture_width=image_width, capture_height=image_height, framerate=30) :   
	    return ('v4l2src device=%s ! ' 
	    'video/x-raw, '
	    'width=(int)%d, height=(int)%d, '
	    'format=(string)YUY2, framerate=(fraction)%d/1 ! '
	    'videorate ! '
	    'video/x-raw, framerate=(fraction)%d/1 ! '
	    'videoconvert ! '
	    'video/x-raw, format=BGR ! '
	    'appsink'  % (camara_type, capture_width,capture_height, framerate, framerate))

	def open(self):
		# open the camera inteface

	def __open_csi(self):
		# opens an inteface to the CSI camera
		try:
			self.cap = cv2.VideoCapture(usb_pipeline(camara_type="/dev/video2"), cv2.CAP_GSTREAMER)
		except:
			raise RuntimeError('Could not initialize camera.')

	def read(self):
		# reading elements

	def release(self):



if __name__ == '__main__':

	# intialize the camera instance

	cap = Camera(type=0, camera_id=0, flip=0, width=4, height=5, fps=20, enforce_fps = True)

	# check if camera is opened
	if cap.isOpened