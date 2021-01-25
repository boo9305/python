import numpy as np 
import cv2 

from matplotlib import pyplot as plt 
from skimage.metrics import structural_similarity as ssim
import imutils

def template_match(name1, cv_capture):
    src = cv_capture
    templit = cv2.imread('./res/%s.png' % name1,0)
    #dst = cv2.imread("hats.png")

    result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    x, y = minLoc
    h, w = templit.shape
    
    if x == 0 and y == 0 : 
        print('fail template match!!!')
    src = cv2.rectangle(src, (x, y), (x +  w, y + h) , (255, 0, 255), 3)
    cv2.imshow("dst", src)
    cv2.waitKey(1000)

def match(name1, cv_capture):
    
    img1 = cv2.imread('./res/%s.png' % name1,0) # queryImage 
    img2 = cv_capture # trainImage 

    # Initiate SIFT detector 
    sift = cv2.SIFT_create() 
    # find the keypoints and descriptors with SIFT 
    kp1, des1 = sift.detectAndCompute(img1,None) 
    kp2, des2 = sift.detectAndCompute(img2,None) 
    # FLANN parameters 
    FLANN_INDEX_KDTREE = 0 
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5) 
    search_params = dict(checks=100) 
    # or pass empty dictionary 
    flann = cv2.FlannBasedMatcher(index_params,search_params) 

    matches = flann.knnMatch(des1,des2,k=2) 
    # Need to draw only good matches, so create a mask 
    matchesMask = [[0,0] for i in range(len(matches))] 
    # ratio test as per Lowe's paper 


    xmin = 9999
    ymin = 9999
    xmax = 0
    ymax = 0
    for i,(m,n) in enumerate(matches): 
        if m.distance < 0.7*n.distance: 
            matchesMask[i]=[1,0] 
            pt1 = kp1[m.queryIdx].pt
            pt2 = kp2[m.trainIdx].pt
            #print(i, pt1,pt2 )

            xmin = min( xmin , pt2[0])
            xmax = max( xmax , pt2[0])
            
            ymin = min( ymin , pt2[1])
            ymax = max( ymax , pt2[1])

    print(xmin ,ymin , xmax, ymax)
#            cv2.circle(img1, (int(pt1[0]),int(pt1[1])), 5, (255,0,255), -1)
#           cv2.circle(img2, (int(pt2[0]),int(pt2[1])), 5, (255,0,255), -1)

    cv2.rectangle(img2, (int(xmin), int(ymin)) , (int(xmax), int(ymax)) , (255,0,255), 3)

    draw_params = dict(matchColor = (0,255,0), 
                    singlePointColor = (255,0,0), 
                    matchesMask = matchesMask, flags = 0) 
    img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params) 
    #h ,w = img2.shape
    #plt.figure(figsize = (w,h))    
    plt.imshow(img2, aspect='auto'),plt.show()


def img_diff(img1 ,img2):
    (score, diff) = ssim(img1, img2, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))
    return score;

import pytesseract
def text_match(src,lang, isDigit, th=0, isTh=False, isShow=True):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    #img = cv2.imread('./res/%s.png' % name1,0) # queryImage 
    #img = cv2.GaussianBlur(img,(5,5),0)
    #img = src.copy()
    
    h, w  = src.shape[:2]
    img = cv2.resize(src, (w*2, h*2), interpolation=cv2.INTER_LINEAR)

    # img2 = cv2.imread('./res/save.png',0)    
    # img_diff(img,img2)

    kernel_sharpen_1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]) #정규화를 하지 않은 이유는 모든 값을 다 더하면 1이되기때문에 1로 나눈것과 같은 효과
    kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]])/8.0 #정규화위해 8로나눔 #img = cv2.pyrUp(src, dstsize=(w * 5, h * 5), borderType=cv2.BORDER_DEFAULT)
    
    if isTh :
        kernel = np.ones((3,3),np.uint8)
        img = cv2.threshold(img, th, 255, cv2.THRESH_BINARY)[1]
        img = cv2.filter2D(img,-1,kernel_sharpen_1)     

    if isShow :
    	cv2.imshow('a',img)
    #cv2.waitKey(100)
    if isDigit:
        text = pytesseract.image_to_string(img, lang=lang , config='digits')
    else:
        text = pytesseract.image_to_string(img, lang=lang)
        
    
    #print(text.strip())

    return text.strip();
   


def hp_mp_bar(img):
    img = img[50:85, 58:200]# y ,x
    r = text_match(img, lang='eng', isDigit=True, th=170, isTh=True).replace('.', '').replace(',','')
    l = r.split()
    
    if len(l) < 2 :
        return;

    if l[0].isdigit() :
        print('hp : %s' % l[0])

    if l[1].isdigit() :
        print('mp : %s' % l[1])

def dogam(img):
    img = img[ 214:240,49:90] # y ,x
    r = text_match(img, lang='eng', isDigit=True, th=170, isTh=False ).replace('.', '').replace(',','')
    if r == "" : r = "NONE"
    print(r)
    return r
def exp_bar(img):
    img = img[250:275, 100:175]# y ,x
    r = text_match(img, lang='kor', isDigit=False, th=170, isTh=False).replace('.', '').replace(',','')

    l = r.replace('/',' ').split()
    if len(l) < 2 :
        return;

    if l[0].isdigit() :
        print('cur_exp : %s' % l[0])

    if l[1].isdigit() :
        print('max_exp : %s' % l[1])


def normal_check(img):
    img = img[177:205,73:176]
    r = text_match(img, lang='kor', isDigit=False, th=120, isTh=False).replace('.', '').replace(',','')
    return r;
    #print(r)

def map_text(img):
    img = img[158:175, 851:931]
    if key == ord('c'):
        print('capture!!!')

        for i in range(1,100):
            if os.path.isfile('./res/map/map%d.png' % i) == False:
                cv2.imwrite('./res/map/map%d.png' % i, img);
                break;

    r = text_match(img, lang='kor', isDigit=False).replace('.', '').replace(',','')

    l = r.replace('/',' ').split()
    print('map : %s' % r)

if __name__ == '__main__':
    match('m2','test')
    match('ghost','test')
    match('img3','img')

