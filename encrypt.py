import cv2
import numpy as np

def is_first(liczba):
    if liczba==1 or liczba == 0: return False
    dzielniki = 0
    for x in range(1, liczba+1):
        if liczba%x==0:
            dzielniki+=1
    # print(dzielniki)
    if dzielniki>2: return False
    else: return True

def encrypt(img, message, message_len):
    i = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[0]):
            if i<message_len:
                if ord(message[i])/10<10:
                    temp = str(ord(message[i])*10)
                    for iter, char in enumerate(temp):
                        img[x][y][iter]=int(char)*28
                else:
                    temp = str(ord(message[i]))
                    for iter, char in enumerate(temp):
                        img[x][y][iter]=int(char)*28
            else:
                pass
            i+=1
    return img


message = input('Podaj wiadomość do zakdowania bez polskich znaków diakrytycznych: ')
print(message, '\n\n')

message_len = len(message)
optimal_len = int(np.ceil(message_len**.5))

print(f'Długość wiadomości: {message_len}\n', f'Optymalna szerokość/wysokość: {optimal_len}')

img = np.zeros((optimal_len, optimal_len, 3))
# img[0][0][0]=50
# img[optimal_len-1][optimal_len-1][0]=250

img = encrypt(img, message, message_len)

print(img)

cv2.imwrite('msg.png', img)

# img = cv2.resize(img, (0, 0), fx=20, fy=20)


cv2.imshow('msg', img)
# cv2.imwrite('messageWitek.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # print(decrypt(cv2.imread('./message.png')))

# # lista = [x for x in range(100) if is_first(x)]
# # print(lista)