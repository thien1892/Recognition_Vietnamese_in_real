# -*- coding: utf-8 -*-
import os
import numpy as np
import cv2
import imgproc
from scipy.spatial import distance
from PIL import ImageFont, ImageDraw, Image

###################
font_dir = "arial.ttf"
# ###################
def count_rec(box):
  dis1 = int(np.ceil(distance.euclidean(box[0], box[1])))
  dis2 = int(np.ceil(distance.euclidean(box[1], box[2])))
  dis3 = int(np.ceil(distance.euclidean(box[2], box[3])))
  dis4 = int(np.ceil(distance.euclidean(box[3], box[0])))
  max_1 = max(dis1, dis3)
  max_2 = max(dis2, dis4)
  width = max(max_1,max_2)
  height = min(max_1,max_2)
  return width, height

def plus_box(box, plus_pixel):
  box[0][1] -= plus_pixel
  box[1][1] -= plus_pixel
  box[2][1] += plus_pixel
  box[3][1] += plus_pixel
  return box

def vietocr_text(img, boxes, detector):
  pre_texts = []
  img = np.array(img)
  for i, box in enumerate(boxes):
    width,height = count_rec(box)
    box = plus_box(box, int(height * 0.1))
    pts1 = np.float32(np.vstack((box[0], box[1], box[3], box[2])))
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    img_output = cv2.warpPerspective(img, matrix, (width, height))
    rgb = cv2.cvtColor(img_output, cv2.COLOR_BGR2RGB)
    rgb = Image.fromarray(rgb)
    s = detector.predict(rgb)
    pre_texts.append(str(s).upper())
  return pre_texts

# borrowed from https://github.com/lengstrom/fast-style-transfer/blob/master/src/utils.py
def get_files(img_dir):
    imgs, masks, xmls = list_files(img_dir)
    return imgs, masks, xmls

def list_files(in_path):
    img_files = []
    mask_files = []
    gt_files = []
    for (dirpath, dirnames, filenames) in os.walk(in_path):
        for file in filenames:
            filename, ext = os.path.splitext(file)
            ext = str.lower(ext)
            if ext == '.jpg' or ext == '.jpeg' or ext == '.gif' or ext == '.png' or ext == '.pgm':
                img_files.append(os.path.join(dirpath, file))
            elif ext == '.bmp':
                mask_files.append(os.path.join(dirpath, file))
            elif ext == '.xml' or ext == '.gt' or ext == '.txt':
                gt_files.append(os.path.join(dirpath, file))
            elif ext == '.zip':
                continue
    # img_files.sort()
    # mask_files.sort()
    # gt_files.sort()
    return img_files, mask_files, gt_files

def saveResult(img_file, img, boxes,pre_texts_, dirname='./result/',  verticals=None, texts= True):
        """ save text detection result one by one
        Args:
            img_file (str): image file name
            img (array): raw image context
            boxes (array): array of result file
                Shape: [num_detections, 4] for BB output / [num_detections, 4] for QUAD output
        Return:
            None
        """

        img = np.array(img)
        # make result file list
        filename, file_ext = os.path.splitext(os.path.basename(img_file))

        # result directory
        res_file = dirname + filename + '.jpg.txt'
        res_img_file = dirname  + filename + '.jpg'

        if not os.path.isdir(dirname):
            os.mkdir(dirname)

        with open(res_file, 'w') as f:
            for i, box in enumerate(boxes):
                poly = np.array(box).astype(np.int32).reshape((-1))
                strResult = ','.join([str(p) for p in poly])+ ','+ pre_texts_[i] + '\r\n'
                f.write(strResult)

                poly = poly.reshape(-1, 2)
                cv2.polylines(img, [poly.reshape((-1, 1, 2))], True, color=(0, 255, 0), thickness=2)
                ptColor = (0, 255, 255)
                if verticals is not None:
                    if verticals[i]:
                        ptColor = (255, 0, 0)

                if texts:
                    width,height = count_rec(box)
                    # font = cv2.FONT_HERSHEY_SIMPLEX
                    # font_scale = 0.5
                    b,g,r,a = 0,0,255,0
                    font = ImageFont.truetype(font_dir, int(height * 0.6))
                    img_pil = Image.fromarray(img)
                    draw = ImageDraw.Draw(img_pil)
                    draw.text((poly[0][0]+1, poly[0][1]-10),  "{}".format(pre_texts_[i]), font = font, fill = (b, g, r, a))
                    # cv2.putText(img, "{}".format(pre_texts[i]), (poly[0][0]+1, poly[0][1]+1), font, font_scale, (0, 0, 0), thickness=1)
                    # cv2.putText(img, "{}".format(pre_texts[i]), tuple(poly[0]), font, font_scale, (0, 255, 255), thickness=1)
                    img = np.array(img_pil)

        # Save result image
        cv2.imwrite(res_img_file, img)

