# RTSPtoMJPEG
Python project to convert a rtsp stream to mjpeg using opencv.

# Installation
## Docker
Build the image:
```docker build -t rtsptomjpeg .```

Run the container: 
```docker run -p 8080:8080 -v ${PWD}:/home/app/src rtsptomjpeg```
