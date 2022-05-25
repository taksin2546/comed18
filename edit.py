from email.mime import image
from PIL import Image
import PIL
image = Image.open('C:\Users\taksin\OneDrive - Khon Kaen University\Desktop\python\pro\pnj\_app1.png')
image = image.resize((1350,720),PIL.Image.ANTIALIAS)
print('r')
image.save('_ch_.png')