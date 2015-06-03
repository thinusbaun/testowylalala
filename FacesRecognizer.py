# -*- coding: utf-8 -*-
__author__ = 'michal'

import cv2
import os
import numpy

class FacesRecognizer:

    def __init__(self):
        self.model = cv2.createEigenFaceRecognizer()
        self.labels = []

    def trainModel(self):
        imagesDict = {}
        path = "./dane/"
        for dirname, dirnames, filenames in os.walk(path):
            for subdirname in dirnames:
                subject_path = os.path.join(dirname, subdirname)
                for fname in os.listdir(subject_path):
                    if ".bmp" in fname:
                        image = cv2.imread(os.path.join(subject_path, fname), cv2.CV_LOAD_IMAGE_GRAYSCALE)
                        resizedImage = cv2.resize(image, (100,100))
                        label = subject_path.split("/")[-1]
                        if label in imagesDict.keys():
                            imagesDict[label].append(resizedImage)
                        else:
                            imagesDict[label] = [resizedImage]
                        print os.path.join(subject_path, fname)
        tmp = self.createLists(imagesDict)
        tmp1 = numpy.asarray(tmp[0])
        tmp2 = numpy.asarray(tmp[1])
        self.labels = dict(zip(tmp2,tmp[2]))
        self.model.train(tmp1, tmp2)

    def createLists(self, imagesDict):
        images = []
        labels = []
        classes = []
        for key in imagesDict.keys():
            i = 0
            for image in imagesDict[key]:
                classes.append(i)
                labels.append(key)
                images.append(image)
            i += 1
        return (images, classes, labels)

    def recognizePerson(self, image):
        resizedImage = cv2.resize(image, (100, 100))
        return self.model.predict(numpy.asarray(resizedImage))
