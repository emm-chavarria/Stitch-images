# Import Pillow library and mount Drive folder with photos
from google.colab import drive
drive.mount('/content/drive')
from PIL import Image, ImageDraw

#Open first photo and use to get dimensions of composite image
# Modify 'dir' with actual directory containing photos
dir = '/content/drive/MyDrive/Colab Notebooks/75.5K/'

# Modify 'pic' with the names of photos
pic = '_24h_MA.JPG'

# Use first photo to base dimensions of composite image
photo = dir+'1'+pic
img = Image.open(photo)
img_size = img.size
print('Image 1:', img_size)

w = 6*img_size[0]
h = 2*img_size[1]
new_im1 = Image.new('RGB', (w,h), (250,250,250))
print('Composite image dimensions','(',w,',',h,')')

#Put Ara– photos together on top
for n in range(1,7):
  photo = dir+str(n)+pic
  img = Image.open(photo)
  img_size = img.size
	
  new_im1.paste(Image.open(photo), (img_size[0]*(n-1),0))
	
#Put Ara+ photos together at the bottom
for x in range(7,13):
  photo = dir+str(x)+pic
  img = Image.open(photo)
  img_size = img.size

  new_im1.paste(Image.open(photo), (img_size[0]*(x-7),img_size[0]))
	
#Save new composite image
new_im1.save("MA.JPG", "JPEG", quality=40)
