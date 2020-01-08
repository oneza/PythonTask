# интерактивный проект

import numpy as np
import cv2

def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]
    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx*fx+fy*fy)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[...,0] = ang*(180/np.pi/2)
    hsv[...,1] = 255
    hsv[...,2] = np.minimum(v, 255)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return bgr

def warp_flow(img, flow):
    h, w = flow.shape[:2]
    flow = -flow
    flow[:,:,0] += np.arange(w)
    flow[:,:,1] += np.arange(h)[:,np.newaxis]
    res = cv2.remap(img, flow, None, cv2.INTER_LINEAR)
    return res

cam =  cv2.VideoCapture(0)
ret, prev = cam.read()
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
cur_glitch = prev.copy()
hsv = np.zeros_like(prev)
hsv[...,1] = 0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None,  0.9, 1, 1, 3, 1, 1, 0)
    prevgray = gray
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,gray,0,255,cv2.NORM_MINMAX)
        
    cur_glitch = warp_flow(cv2.blur(img,(1000,1000)), flow)
    cv2.imshow('progect', cv2.cvtColor(cur_glitch-draw_hsv(flow),cv2.COLOR_HSV2RGB))

    ch = 0xFF & cv2.waitKey(5)
    if ch == 27:
        break
    if ch == ord('1'):
        show_hsv = not show_hsv
    if ch == ord('2'):
        show_glitch = not show_glitch
        if show_glitch:
            cur_glitch = img.copy()
cv2.destroyAllWindows()