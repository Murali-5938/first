import cv2
import os
import numpy as np
from django.shortcuts import render
from .forms import UploadImageForm
from django.conf import settings

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(3-6)', '(7-12)', '(13-20)','(21-25)' ,'(26-32)', '(33-43)', '(44-53)', '(54-100)']
genderList = ['Male', 'Female']

faceNet = cv2.dnn.readNet("models/opencv_face_detector_uint8.pb", "models/opencv_face_detector.pbtxt")
ageNet = cv2.dnn.readNet("models/age_net.caffemodel", "models/age_deploy.prototxt")
genderNet = cv2.dnn.readNet("models/gender_net.caffemodel", "models/gender_deploy.prototxt")

def highlightFace(net, frame, threshold=0.7):
    frameOpencvDnn = frame.copy()
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []
    h, w = frameOpencvDnn.shape[:2]
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > threshold:
            x1 = int(detections[0, 0, i, 3] * w)
            y1 = int(detections[0, 0, i, 4] * h)
            x2 = int(detections[0, 0, i, 5] * w)
            y2 = int(detections[0, 0, i, 6] * h)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return frameOpencvDnn, faceBoxes

def index(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            filepath = os.path.join(settings.MEDIA_ROOT, image.name)
            with open(filepath, 'wb+') as dest:
                for chunk in image.chunks():
                    dest.write(chunk)

            frame = cv2.imread(filepath)
            resultImg, faceBoxes = highlightFace(faceNet, frame)

            for faceBox in faceBoxes:
                face = frame[max(0, faceBox[1] - 20):min(faceBox[3] + 20, frame.shape[0] - 1),
                             max(0, faceBox[0] - 20):min(faceBox[2] + 20, frame.shape[1] - 1)]
                blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
                
                genderNet.setInput(blob)
                gender = genderList[genderNet.forward()[0].argmax()]

                ageNet.setInput(blob)
                age = ageList[ageNet.forward()[0].argmax()]

                label = f'{gender}, {age}'
                cv2.putText(resultImg, label, (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

            output_path = os.path.join(settings.MEDIA_ROOT, "output.jpg")
            cv2.imwrite(output_path, resultImg)
            return render(request, 'index.html', {
                'form': form,
                'output_image': 'output.jpg',
                'MEDIA_URL': settings.MEDIA_URL
                })
    else:
        form = UploadImageForm()
    return render(request, 'index.html', {'form': form})
