import cv2, time
video=cv2.VideoCapture(0)#videocapture object
time.sleep(3)
a=1

while True:
    a=a+1
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#converts image to grayscale
    cv2.imshow('Click Q to capture',gray) #preview of image before capturing
    key=cv2.waitKey(1)#generates new frame after every 1 milisecond
    if key==ord('q'):#on entering 'q' the window will be destroyed
        cv2.destroyAllWindows()
        break
print(a)#prints number of frames
def greytosketch(frame,k_size):
    #displaying the captured image in grey
    gr=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # Invert Image
    invert_img=cv2.bitwise_not(gr)
    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)
    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    # Sketch Image
    sketch_img=cv2.divide(gr,invblur_img, scale=256.0)
    # Save Sketch
    cv2.imwrite('sketch.jpg', sketch_img)
    
    # Display sketch
    cv2.imshow('sketch image',sketch_img)
    cv2.waitKey(0)#waits until pressing any key
    cv2.destroyAllWindows()#destroys all the windows after clicking any button
    video.release()

greytosketch(frame,7)#calling the function which converts the image to sketch
