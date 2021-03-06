import cv2
import Logger
import numpy as np

__author__ = 'emontenegro'


class SatelliteImage:
    # Constants
    TOP_LEFT = "tl"
    TOP_RIGHT = "tr"
    BOT_LEFT = "bl"
    BOT_RIGHT = "br"

    # Attributes
    currentImage = None
    imageContours = None
    transformedSatelliteImage = None
    transformedImageContours = None

    midPatternPointsTransformed = {TOP_LEFT: None, TOP_RIGHT: None, BOT_LEFT: None, BOT_RIGHT: None}

    botContourPoints = []
    rgtContourPoints = []
    lftContourPoints = []
    topContourPoints = []

    botContourPointsTransformed = []
    rgtContourPointsTransformed = []
    lftContourPointsTransformed = []
    topContourPointsTransformed = []

    def __init__(self, imageobject):
        self.currentImage = cv2.imread(imageobject, cv2.CV_LOAD_IMAGE_GRAYSCALE)  # open image in grayscale format

    def get_width(self):
        return self.currentImage.shape[1]

    def get_height(self):
        return self.currentImage.shape[0]

    def calculate_contours(self):
        # calculando contornos de la imagen original
        if self.currentImage is not None and self.imageContours is None:
            ret, thresh = cv2.threshold(self.currentImage, 127, 255, cv2.THRESH_BINARY)
            Logger.save_image('black_and_white_image_original.png', thresh)
            self.imageContours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

            for contour in self.imageContours[1:]:
                self.__get_contour_bot_points(contour)
                self.__get_contour_top_points(contour)
                self.__get_contour_rgt_points(contour)
                self.__get_contour_lft_points(contour)

        # calculando contornos de la imagen transformada
        if self.transformedSatelliteImage is not None and self.transformedImageContours is None:
            ret, thresh = cv2.threshold(self.transformedSatelliteImage, 127, 255, cv2.THRESH_BINARY)
            Logger.save_image('black_and_white_image_transformed.png', thresh)
            self.transformedImageContours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

            for contour in self.imageContours[1:]:
                self.__get_contour_bot_points_transformed(contour)
                self.__get_contour_top_points_transformed(contour)
                self.__get_contour_rgt_points_transformed(contour)
                self.__get_contour_lft_points_transformed(contour)

        # cImg = np.copy(self.currentImage)
        # for point in self.topContourPoints:
        #     cv2.circle(cImg, tuple(point), 1, 50)
        # Logger.save_image('/lala/top.png', cImg)
        # cImg = np.copy(self.currentImage)
        # for point in self.botContourPoints:
        #     cv2.circle(cImg, tuple(point), 1, 50)
        # Logger.save_image('/lala/bot.png', cImg)
        # cImg = np.copy(self.currentImage)
        # for point in self.rgtContourPoints:
        #     cv2.circle(cImg, tuple(point), 1, 50)
        # Logger.save_image('/lala/rgt.png', cImg)
        # cImg = np.copy(self.currentImage)
        # for point in self.lftContourPoints:
        #     cv2.circle(cImg, tuple(point), 1, 50)
        # Logger.save_image('/lala/lft.png', cImg)

    def __get_contour_top_points(self, contour):
        self.topContourPoints.append(tuple(contour[contour[:, :, 1].argmin()][0]))

    def __get_contour_bot_points(self, contour):
        self.botContourPoints.append(tuple(contour[contour[:, :, 1].argmax()][0]))

    def __get_contour_rgt_points(self, contour):
        self.rgtContourPoints.append(tuple(contour[contour[:, :, 0].argmax()][0]))

    def __get_contour_lft_points(self, contour):
        self.lftContourPoints.append(tuple(contour[contour[:, :, 0].argmin()][0]))

    def __get_contour_top_points_transformed(self, contour):
        self.topContourPointsTransformed.append(tuple(contour[contour[:, :, 1].argmin()][0]))

    def __get_contour_bot_points_transformed(self, contour):
        self.botContourPointsTransformed.append(tuple(contour[contour[:, :, 1].argmax()][0]))

    def __get_contour_rgt_points_transformed(self, contour):
        self.rgtContourPointsTransformed.append(tuple(contour[contour[:, :, 0].argmax()][0]))

    def __get_contour_lft_points_transformed(self, contour):
        self.lftContourPointsTransformed.append(tuple(contour[contour[:, :, 0].argmin()][0]))

    def get_pixel(self, x, y):
        return self.currentImage[y][x]

    def get_transformed_pixel(self, x, y):
        return self.transformedSatelliteImage[y][x]