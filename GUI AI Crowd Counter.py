from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, QtWebChannel
import re
from io import BytesIO
from PIL import Image
import base64
import cv2
import numpy as np
import os
import sys
import torch
from torchvision import transforms
from sfanet.models import M_SFANet_UCF_QNRF
from jinja2 import FileSystemLoader, Environment


class Backend(QtCore.QObject):
    @QtCore.pyqtSlot(str, result=str)
    def crowdcount(self, x):
        try:
            image_data = re.sub('^data:image/.+;base64,', '', x)
            img = Image.open(BytesIO(base64.b64decode(image_data))).convert('RGB')
            trans = transforms.Compose([transforms.ToTensor(),
                                        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                        ])
            height, width = img.size[1], img.size[0]
            height = round(height / 16) * 16
            width = round(width / 16) * 16
            img = cv2.resize(np.array(img), (width, height), cv2.INTER_CUBIC)
            img = trans(Image.fromarray(img))[None, :]

            model = M_SFANet_UCF_QNRF.Model()
            model.load_state_dict(torch.load("weights.pth",
                                             map_location=torch.device('cpu')))
            model.eval()
            density_map = model(img)
            est = round(torch.sum(density_map).item())
            display(est, x)
        except:
            displayB()
        return x


templateLoader = FileSystemLoader(searchpath="./")
templateEnv = Environment(loader=templateLoader)
TEMPLATE_FILE = "index.html"
tm = templateEnv.get_template(TEMPLATE_FILE)


def displayB():
    updatedHtlm = tm.render(preImg="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=")
    view.setHtml(updatedHtlm)


def display(num, x):
    updatedHtml = tm.render(estimateText="Approximately " + str(num) + " People", preImg=x)
    view.setHtml(updatedHtml)


app = QtWidgets.QApplication(sys.argv)

backend = Backend()

view = QtWebEngineWidgets.QWebEngineView()
view.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
view.setWindowTitle("GUI AI Crowd Size Estimator")

channel = QtWebChannel.QWebChannel()
view.page().setWebChannel(channel)
channel.registerObject("backend", backend)

current_dir = os.path.dirname(os.path.realpath(__file__))
initialHtml = tm.render(preImg="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=")
view.setHtml(initialHtml)

view.resize(512, 400)
view.show()
sys.exit(app.exec_())
