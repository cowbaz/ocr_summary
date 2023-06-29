import cv2


#  read image file
def readimage(imagePath):
    img = cv2.imread(imagePath)
    return img


# turn image to grayscale image
def turn_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# remove noise
def remove_noise(image):
    return cv2.medianBlur(image, 1)


# threshold
def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# out the processed image file
def output_image_file(imagePath):
    try:
        image = threshold(remove_noise(turn_grayscale(readimage(imagePath))))
        cv2.imwrite(f"post_{imagePath}.jpg", image)
    except Exception as e:
        print("Exception:".str(e))
    return f"post_{imagePath}.jpg"
