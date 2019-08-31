import sys
import os
arg1 = sys.argv[1]
os.system('rm /media/amirhossein/JEVOIS/share/tensorflow/catdog/model.tflite')
os.system('mv /media/amirhossein/JEVOIS/share/tensorflow/catdog/' + arg1 + '.tflite /media/amirhossein/JEVOIS/share/tensorflow/catdog/model.tflite')

