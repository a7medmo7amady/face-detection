# Face Detection App

This Python application uses OpenCV to detect faces in images or video streams.

## Features

- Detect faces in static images
- Real-time face detection using webcam
- Supports multiple face detection

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- pip (Python package manager)

## Installation

### 1. Clone the repository

```
git clone https://github.com/a7medmo7amady/face-detection.git
cd face-detection
```

### 2. Set up a virtual environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install OpenCV and other dependencies

#### On all operating systems:

```
pip install opencv-python numpy
```

#### Additional steps for macOS:

If you encounter issues, you may need to install OpenCV using Homebrew:

```
brew install opencv
```

#### Additional steps for Linux:

You might need to install additional dependencies:

```
sudo apt-get update
sudo apt-get install python3-opencv
```

## Usage

1. To detect faces in an image:

```
python detect_faces_image.py --image path/to/your/image.jpg
```

2. To detect faces using your webcam:

```
python detect_faces_webcam.py
```

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV community for their excellent computer vision library
- [Haar Cascade classifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) for face detection
