import cv2

def decrypt(img):
    # img = cv2.resize(img, (0, 0), fx=0.05, fy=0.05)
    message = ""
    for x in range(img.shape[0]):
        for y in range(img.shape[0]):
            liczba = 0
            a = img[x][y][0]/28
            b = img[x][y][1]/28
            c = img[x][y][2]/28
            if c==0 and b!=0 and a!=1:
                liczba = int((a*100+b*10+c)/10)
                message+=chr(liczba)
            else:
                liczba = int(a*100+b*10+c)
                message+=chr(liczba)
    return message

print(decrypt(cv2.imread('./msg.png')))