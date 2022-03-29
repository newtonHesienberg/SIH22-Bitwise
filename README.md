# Smart India Hackathon 2022

+ Problem statement: [Video metadata generation and classification](https://sih.gov.in/sih2022PS)
+ Problem number: SS585

Team – <b>Bitwise</b>

<b>Team Members:</b>

Abhishek Tomar (<b>Team Lead</b>), Newton Kumar, Nitish Kumar, Shameek Pathak, Rohit Kumar Rajak, Anuprabha Bhardwaj;
Netaji Subhas University of Technology, Delhi, India


# Overview
<img src="https://github.com/newtonHesienberg/SIH22-Bitwise/blob/main/Block%20Diagram.png">

We are building an effective model for automating the process of video metadata generation, which is then used for video classification. The solution comprises of two parts:

    1. Deep Learning for metadata generation and classification
    2. Web interface 

The idea is to make use of a web interface to upload videos, and then sending this input to the deep learning model we have created to extract metadata and classify the video. We will extract the metadata from input video in 3 ways:
    
    1. Object detection 
    2. Audio analysis
    3. Video OCR

# DEEP LEARNING

The deep learning section comprises of:
    
    1. Key frame extraction
    2. Object detection
    3. Optical Character Recognition(OCR) on extracted key frames, followed by Name Entity Recognition (NER)
    4. Generating audio transcript followed by NER
    
The various techniques used to achieve the above steps are listed as follows:

    1. OpenCV
    2. Tensorflow
    3. Google Vision API

The proposed machine learning model is integrated into a web interface using the Flask framework. 
