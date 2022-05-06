import argparse
import os
import os.path as osp
import sys
import random
from pathlib import Path

import cv2
import numpy as np


colors = [[random.randint(0, 255) for _ in range(3)] for cate in range(10)]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--imgp', type=str, required=True)
    parser.add_argument('--label', type=str, default=None)
    parser.add_argument('--lane', type=str, default=None)
    parser.add_argument('--freespace', type=str, default=None)
    args = parser.parse_args()
    print(args)
    return args

if __name__ == '__main__':
    args = parse_args()

    cv2.namedWindow('viewimg', cv2.WINDOW_NORMAL) 
    fnames = os.listdir(args.imgp)    
    idx = 0
    while 1:
        fname = fnames[idx]
        imgfpath = osp.join(args.imgp, fname)
        print('==> {:<5d}/{:<5d}, {}'.format(idx+1, len(fnames), imgfpath))

        # Load image
        img = cv2.imread(imgfpath)
        fuse = img.copy()

        # Load freespace
        if args.freespace is not None:
            freesp_fpath = osp.join(args.freespace, fname[:-4] + '.png')
            freesp = cv2.imread(freesp_fpath, cv2.IMREAD_GRAYSCALE)
            freesp_rgb = img.copy()
            freesp_rgb[freesp==255, 0] = 0
            freesp_rgb[freesp==255, 1] = 255
            freesp_rgb[freesp==255, 2] = 0
            # freesp_fuse = cv2.addWeighted(img, 0.8, freesp_rgb, 0.2, 0)
            fuse = cv2.addWeighted(fuse, 0.7, freesp_rgb, 0.3, 0)

        # Load Lane
        if args.lane is not None:
            lane_fpath = osp.join(args.lane, fname[:-4] + '.png')
            lane = cv2.imread(lane_fpath, cv2.IMREAD_GRAYSCALE)
            lane_rgb = img.copy()
            for i in range(1, 9):
                lane_rgb[lane==i, 0] = colors[i][0]
                lane_rgb[lane==i, 1] = colors[i][1]
                lane_rgb[lane==i, 2] = colors[i][2]
            # lane_fuse = cv2.addWeighted(img, 0.4, lane_rgb, 0.4, 0)
            fuse = cv2.addWeighted(fuse, 0.4, lane_rgb, 0.4, 0)
        
        # Load label
        if args.label is not None:
            label_fpath = osp.join(args.label, fname[:-4] + '.txt')
            with open(label_fpath, 'r') as f:
                for bbox in f.readlines():
                    bbox = bbox.strip()
                    if bbox == '': continue
                    bbox = bbox.split()
                    category = bbox[0]
                    x, y, w, h = [eval(i) for i in bbox[1:]]
                    xlt = int(x - w/2)
                    ylt = int(y - h/2)
                    xrb = int(x + w/2)
                    yrb = int(y + h/2)
                    # cv2.rectangle(img, (xlt, ylt), (xrb, yrb), (0, 0, 255), thickness=1)
                    cv2.rectangle(fuse, (xlt, ylt), (xrb, yrb), (0, 0, 255), thickness=1)

        imgshow = np.vstack([img, fuse])

        cv2.imshow('viewimg', imgshow)
        key = cv2.waitKey(0)
        if key == ord('q'):
            sys.exit(0) 
        elif key == ord('b'):
            idx -= 1
        else:
            idx += 1

        if idx < 0 or idx >= len(fnames):
            break

    cv2.destroyAllWindows()