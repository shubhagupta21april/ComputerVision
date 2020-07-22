import cv2
img = cv2.imread('original1.jpg')
#cv2.imshow("original",img)
mask = cv2.imread('original_mask.jpg', 0)
#cv2.imshow("masked_image",mask)
ns = cv2.inpaint(img, mask, 1, cv2.INPAINT_NS)
telea = cv2.inpaint(img, mask, 1, cv2.INPAINT_TELEA)
#cv2.imshow("final",ns)
cv2.imshow("final2",telea)
cv2.waitKey(0)
cv2.destroyAllWindows()