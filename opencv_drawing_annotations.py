import cv2
import  numpy as np
old_img=cv2.imread("New folder/img5.png")
txt=cv2.putText(img=old_img,
text="PAKISTAN" , 
org=(200,100),
fontScale=3,
fontFace=cv2.FONT_HERSHEY_SIMPLEX,
color=(111,6,111)     ,
thickness=3,
lineType=cv2.LINE_8,
bottomLeftOrigin=False)
new_img=cv2.circle(img=old_img, color=(0,0,255),center=(130,90),radius=60,thickness=4,lineType=4)
new_img=cv2.ellipse(img=old_img, color=(4,8,155),center=(140,80),axes=(40,60),angle=30,startAngle=0,endAngle=320,thickness=3,lineType=3)
new_img=cv2.polylines(img=old_img,pts=[np.array([[70,80],[90,100],[100,200],[200,400],[300,500]])],isClosed=True,color=(0,0,244),thickness=3,lineType=4)
cv2.imshow("wscube",old_img)
cv2.waitKey(0)
cv2.destroyAllWindows()