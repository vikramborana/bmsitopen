import os
from PIL import Image,ImageFilter,ImageEnhance

def brightness(image,bl):
	img=Image.open(image)
	enhancer=ImageEnhance.Brightness(img)
	img=enhancer.enhance(bl)
	img.save("./output/princeton_small_brightness_"+str(bl)+".jpg")

def contrast(image,cl):
	img=Image.open(image)
	enhancer=ImageEnhance.Contrast(img)
	img=enhancer.enhance(cl)
	img.save("./output/c_contrast_"+str(cl)+".jpg")
	
def blur(image,bll):
	img=Image.open(image)
	img=img.filter(ImageFilter.GaussianBlur(bll))
	img.save("./output/blur_"+str(bll)+".jpg")

def sharp(image):
	img=Image.open(image)
	img=img.filter(ImageFilter.SHARPEN)
	img.save("./output/sharpen.jpg")
	
	
def edge(image):
	img=Image.open(image)
	img=img.filter(ImageFilter.FIND_EDGES)
	img.save("./output/edgedetect.jpg")

def gaussian_sampling(image,gll):
	img=Image.open(image)
	img=img.filter(ImageFilter.GaussianBlur(gll))
	img.save("./output/scale_gaussian.jpg")
		
def point_sampling(image,pl):
	img=Image.open(image)
	img=img.point(lambda p: p >pl and 255)
	img.save("./output/scale_point.jpg")

def composite(image1,image2,mask):
	img1=Image.open(image1).convert('L')
	img2=Image.open(image2).convert('L')
	mask=Image.open(mask).convert('L')
	img=Image.composite(img1,img2,mask)
	img.save("./output/composite.jpg")

	
		
		
brightness("./input/princeton_small.jpg",0.0)
brightness("./input/princeton_small.jpg",0.5)
brightness("./input/princeton_small.jpg",2.0)		
contrast("./input/c.jpg",-0.5)
contrast("./input/c.jpg",0.0)
contrast("./input/c.jpg",0.5)
contrast("./input/c.jpg",2.0)
blur("./input/princeton_small.jpg",0.125)
blur("./input/princeton_small.jpg",2)	
blur("./input/princeton_small.jpg",8)
sharp("./input/princeton_small.jpg")	
edge("./input/princeton_small.jpg")
gaussian_sampling("./input/scaleinput.jpg",0.3)
point_sampling("./input/scaleinput.jpg",0.3)
composite("./input/comp_background.jpg","./input/comp_foreground.jpg","./input/comp_mask.jpg")

		

