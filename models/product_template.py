# -*- coding: utf-8 -*-

from odoo import models, fields, api
import io
from io import BytesIO
import base64
from PIL import Image
import numpy as np
import cv2
#import os


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    lote_img = fields.Binary(string="Lote Img", related='categ_id.lote_img')
    x0 = fields.Integer('X0')
    y0 = fields.Integer('y0')
    x1 = fields.Integer('X1')
    y1 = fields.Integer('y1')

    def set_gray(self):
        if self.lote_img:
            with io.BytesIO(base64.b64decode(self.categ_id.lote_img)) as f:
                x0 = self.x0
                y0 = self.y0
                x1 = self.x1
                y1 = self.y1
                # arr_image=Image.open("lote.jpg")
                arr_image = Image.open(f)
                array_image = np.array(arr_image)
                array_zeros = array_image

                for n in (range(array_image.shape[0])):
                    for m in (range(array_image.shape[1])):
                        R = G = B = suma = 0
                        # TODO Simplificar el algoritmo para pasar a escala de grises
                        if (n > x0 and n < x1) and (m > y0 and m < y1):

                            for j in (range(array_image.shape[2])):
                                if j == 0:
                                    R = array_image[n, m, j]*0.3
                                    suma = suma+R
                                elif j == 1:
                                    G = array_image[n, m, j]*0.59
                                    suma = suma+G
                                else:
                                    B = array_image[n, m, j]*0.11
                                    suma = suma+B
                            array_zeros[n, m] = suma
                        else:

                            array_zeros[n, m] = array_image[n, m]

                cv2.imwrite("otro_lote.jpg", array_zeros)
                #Este archivo se crea en el sistema de archivos
                variable = cv2.imread("otro_lote.jpg")
                print(type(variable))
                self.categ_id.lote_img = base64.b64encode(
                    open('otro_lote.jpg', 'rb').read())
