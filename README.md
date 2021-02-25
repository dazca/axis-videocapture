Python project to set up a connection towards Axis Communications devices and to subscribe to specific events on the metadatastream.

## Install
Clone the repo, move to the folder and type with your desired python environment active:
```bash
pip install -e .
```

## Usage
Obtain the camera object to manipulate:
```python
import axispy

url_to_camera = "192.168.1.1"
cam = axispy.camera(url_to_camera, "admin", "password")
```

### Camera manipulation (PTZ and configuration)
To *manipulate* the camera we use [sensecam_control](https://github.com/smartsenselab/sensecam-control) library which contain an extensive usage of both VAPIX and ONVIF apis to control the camera:

```python

cam.absolute_move(10, 20, 1)
img_shape = cam.get_image_size()
```

For further usage check [sensecam_control](https://github.com/smartsenselab/sensecam-control) repository.

### Snapshot

To obtain a snapshot through http using urllib:
```python
img = cam.snapshot()
```

Otherwise, you can use native [sensecam_control](https://github.com/smartsenselab/sensecam-control) functions as `get_bitmap_request` or `get_jpeg_request`.

### Video Stream
Also, you can obtain an OpenCV *streamer* object to continuously capture a video stream:

```python
cap = cam.obtain_streamer()

# Coninuously visualize video stream
ret = True
k = -1
while ret and ord(k)!=113:
    ret, img := cap.read()
    cv2.imshow("img", img)
    k = cv2.waitKey(1)
```

