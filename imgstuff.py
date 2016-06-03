from PIL import Image
from PIL import ImageDraw
import numpy as np

imo = Image.open("4_11_mask.tif")

a = np.asarray(imo)

nz = np.nonzero(a)
print np.shape(nz)
print nz

minval0 = np.min(nz[0])
maxval0 = np.max(nz[0])

minval1 = np.min(nz[1])
maxval1 = np.max(nz[1])

meanval0 = np.mean(nz[0])
meanval1 = np.mean(nz[1])

draw = ImageDraw.Draw(imo)


draw.point((minval1, minval0), 'white')

draw.point((maxval1, minval0), 'white')

draw.point((minval1, maxval0), 'white')

draw.point((maxval1, maxval0), 'white')

draw.point((meanval1, meanval0), 'blue')


#103
#227
#362
#452


#draw.ellipse((minval1, minval0, maxval1, maxval0), fill = 'blue', outline ='blue')

print minval0
print maxval0
print minval1
print maxval1




#im = imo.rotate(45)

#imf = imo.transpose(Image.FLIP_LEFT_RIGHT)

imo.save("test.tif")
#imf.save("test_flip.tif")

