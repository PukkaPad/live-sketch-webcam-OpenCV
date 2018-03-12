import cv2

def sketch(image):
    """ 
    This function generates a sketch image.
    It will convert the image to gray scale image,
    Gaussian blur will be passed to the imaged, to smooth it and clean up any noise from it, 
    And then the edges will be extracted using Canny.

    Args:
        image: image captured from the webcam

    Returns:
        The sketch/masked image
    """

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    canny_edges = cv2.Canny(img_gray_blur, 15, 70) 
    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


# Initialize webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was sucessful (ret)
# It also contains the images collected from the webcam (frame)
cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    # ret is a boolean that returns True or False
    # frame is the actual image captured from the webcam

    cv2.imwrite("frame%d.jpg" % count, sketch(frame))    
    count += 1

    cv2.imshow('Live Sketcher', sketch(frame))
    if cv2.waitKey(1) & 0xFF == 13: #13 is the Enter Key
        break
        
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()