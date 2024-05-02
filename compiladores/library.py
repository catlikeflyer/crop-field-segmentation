import numpy as np
import cv2 
import matplotlib.pyplot as plt

def load_image(path):
    path = path.strip()
    return cv2.imread(path)

def save_image(filename, image):
    cv2.imwrite(filename, image)

def show_image(img):
    cv2.imshow('window' , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

def show_histogram(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.xlabel('Pixel value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

def watershed_segmentation(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    _, markers = cv2.connectedComponents(sure_fg)
    markers += 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(image, markers)
    image[markers == -1] = [255, 0, 0]
    return image

def grabcut_segmentation(image):
    mask = np.zeros(image.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (50,50,450,290)
    cv2.grabCut(image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    image = image*mask2[:,:,np.newaxis]
    return image

def template_matching(image, template):
    res = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    h,w = template.shape[:2]
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image,top_left, bottom_right, 255, 2)
    return image

def canny_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edges

def search_cv2(function_name):
    try:
        return getattr(cv2, function_name) 
    except:
        return None    
    return None

def gen_matrix(a,b,*args):
    s = np.array(args)
    return s.reshape(int(a),int(b))

def gen_vector(*args):
    s = np.array(args)
    return s
