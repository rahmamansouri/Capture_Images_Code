import cv2  # Import the OpenCV library

# Initialize the video capture object with camera index 1 and set the preferred frame dimensions
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

num = 0  # Initialize a counter to keep track of saved images

# Start an infinite loop to continuously capture frames from the camera
while cap.isOpened():
    success, frame = cap.read()  # Read a frame from the camera

    height, width, _ = frame.shape  # Extract the dimensions of the frame
    # Split the frame into left and right images for stereo vision processing
    left_image = frame[:, 0:width // 2, :]
    right_image = frame[:, width // 2:, :]

    # Display the left and right images in separate windows
    cv2.imshow('Left Image', left_image)
    cv2.imshow('Right Image', right_image)

    k = cv2.waitKey(5)  # Wait for a key press with a timeout of 5 milliseconds

    if k == 27:  # If the 'Esc' key is pressed, exit the loop
        break
    elif k == ord('s'):  # If the 's' key is pressed, save the current images
        cv2.imwrite('images/stereoLeft/imageL' + str(num) + '.png', left_image)  # Save the left image
        cv2.imwrite('images/stereoRight/imageR' + str(num) + '.png', right_image)  # Save the right image
        print("Images saved!")
        num += 1  # Increment the counter for the next image

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

