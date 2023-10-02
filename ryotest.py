import cv2
import numpy as np

def main():
    # Get the input image filename from the user
    filename = input("Enter an image name in the same directory: ")

    # Read the input image in grayscale
    imgtest = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur
    imgtest = cv2.GaussianBlur(imgtest, (21, 21), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(imgtest, 30, 30)

    # Convert the edges to a color image (red)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Create a mask of red color
    color = (0, 0, 255)
    mask = np.zeros_like(edges)
    mask[:] = color

    # Blend the edges with the red mask
    result = cv2.addWeighted(edges, 0.5, mask, 9, 0)

    # Save the result to "output_canny.png"
    cv2.imwrite("output_canny.png", result)

    # Read the saved image
    imgtest2 = cv2.imread("output_canny.png")

    # Convert the image to grayscale
    img_gray3 = cv2.cvtColor(imgtest2, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image
    _, im3 = cv2.threshold(img_gray3, 100, 255, cv2.THRESH_BINARY)

    # Split the original image into its color channels
    bgr3 = cv2.split(imgtest2)

    # Create a 4-channel image with the third channel replaced by the thresholded image
    rgba3 = [bgr3[0], bgr3[1], bgr3[2], im3]
    dst3 = cv2.merge(rgba3)

    # Save the result to "output_canny.png" (overwriting the previous file)
    cv2.imwrite("output_canny.png", dst3)

    # Read the original image
    image = cv2.imread(filename)

    # Convert the image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image
    _, im = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the binary image
    contours, _ = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an empty image for drawing contours
    res_img = np.zeros_like(image)

    # Draw contours on the empty image
    cv2.drawContours(res_img, contours, -1, (0, 255, 25), 2)

    # Convert the result to grayscale
    img_gray2 = cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image
    _, im2 = cv2.threshold(img_gray2, 25, 255, cv2.THRESH_BINARY)

    # Split the image into color channels
    bgr2 = cv2.split(res_img)

    # Create a 4-channel image with the third channel replaced by the thresholded image
    rgba2 = [bgr2[0], bgr2[1], bgr2[2], im2]
    dst2 = cv2.merge(rgba2)

    # Save the result to "output_lines.png"
    cv2.imwrite("output_lines.png", dst2)

if __name__ == "__main__":
    main()
