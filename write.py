import cv2
import numpy as np
import base64

# black blank image
blank_image = np.zeros(shape=[70, 150, 3], dtype=np.uint8)


def write_image(submitted_image, count):
    image = submitted_image.copy()

    count_display = str(count)
    # add zeros to left of count if not enough digits
    digits_needed = 7
    digits = len(count_display)
    digits_to_add = digits_needed - digits

    for i in range(digits_to_add):
        count_display = "0" + count_display

    font = cv2.FONT_HERSHEY_SIMPLEX

    bottomLeftCornerOfText = (4, 45)
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2

    cv2.putText(
        image,
        str(count_display),
        bottomLeftCornerOfText,
        font,
        fontScale,
        fontColor,
        lineType,
    )

    return image


def write(count):
    image = write_image(blank_image, count)

    text = cv2.imencode(".jpg", image)[1].tostring()

    return text


if __name__ == "__main__":
    print(write(6969))
