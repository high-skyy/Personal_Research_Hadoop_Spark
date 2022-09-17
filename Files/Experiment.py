from PIL import Image
import numpy as np

name = "Experiment.jpg"
img = Image.open(name)
pix = np.array(img)
print(len(pix[0]))

# https://blog.naver.com/PostView.naver?blogId=roootwoo&logNo=221590352393&redirect=Dlog&widgetTypeCall=true&directAccess=false