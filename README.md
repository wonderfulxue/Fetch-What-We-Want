# F Ⅲ W

## Introduction

**F Ⅲ W **(Fetch *What We Want*) is a feeding robot aimed to help those who cannot eat or drink independently. Feeding Robot can be controlled by natural language instructions. After receiving message from a user, **F Ⅲ W ** can extract keywords from user's instructions, locate what the user want on the table, and feed it into patients' mouth.

Demo is avaliable at [Youtube.](https://youtu.be/WOYQ2A6ZiRU) 

##Core Techniques 

* **Speech Recognition**
* **Image Recognition & Localization**
* **Grabbing Algorithm**
* **Human Computer Interaction**

## Hardware Setup

* SainSmart DIY 6-Axis Servos Control Palletizing Robot Arm
* Arduino 101 Board
* Logitech c270 web camera
* MacBook Pro 

## Code Structure

* Arduino - Serial communication logic & object grabbing algorithm
* Yolo-v3 - Main CV model for object detection & Localization
* Webcam - Integrated CV model with webcam videp stream with OpenCV
* Voice_recgonizer - Framework for processing user's instruction
* Supporting Files - Product Analytics & Presentation Slide

## Author

Zhijun Xue, School of Electronic Information and Communications, Huazhong University of Science & Technology(*HUST*)

## License

[MIT License](LICENSE)

Copyright (c) 2019 Zhijun Xue
