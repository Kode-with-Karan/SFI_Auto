import cv2
import keyboard
import pyautogui


def listen_key():
    keyboard.wait("alt gr+p")
    take_ss()

def take_ss():
    pyautogui.screenshot().save('ss.png')
    show_img()
    print("hello")

def show_img():
    path = r'ss.png'
    coordinates = []
    duo_coordinates =[]
    img = cv2.imread(path)
    cv2.imshow('image', img)
    def mouse_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:

            font = cv2.FONT_HERSHEY_TRIPLEX
            LB = '.'
        
            cv2.putText(img, LB, (x, y), font, 1, (255, 255, 0), 2) 
            cv2.imshow('image', img)

            duo_coordinates.append([x,y])
            print(duo_coordinates.__len__())
            print(duo_coordinates)
            if (duo_coordinates.__len__() == 2):


                cv2.rectangle(img, duo_coordinates[0], duo_coordinates[1], (0,0,0), 2)
                cv2.imshow('image', img)
                coordinates.append(duo_coordinates[0])
                coordinates.append(duo_coordinates[1])

                duo_coordinates.clear()


        if event == cv2.EVENT_RBUTTONDOWN:
            try:  
                croped_img = img[coordinates[0][1]:coordinates[1][1], coordinates[0][0]:coordinates[1][0]]
                cv2.imshow('croped', croped_img)
            except Exception as e:
                try:
                    croped_img = img[coordinates[1][1]:coordinates[0][1], coordinates[1][0]:coordinates[0][0]]
                    cv2.imshow('croped', croped_img)
                except Exception as e:
                    try:
                        croped_img = img[coordinates[0][1]:coordinates[1][1], coordinates[1][0]:coordinates[0][0]]
                        cv2.imshow('croped', croped_img)
                    except Exception as e:
                        try:  
                            croped_img = img[coordinates[1][1]:coordinates[0][1], coordinates[0][0]:coordinates[1][0]]
                            cv2.imshow('croped', croped_img)
                        except Exception as e:
                            print(e)
            coordinates.clear()


    cv2.setMouseCallback('image', mouse_click)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# def crop_img():
#     pass

# def raugh():
# # 3E -> [[233, 531], [508, 385]]
# # 3E -> [[233, 385], [508, 531]]
#     import cv2

#     path = r'ss.png'



    

#     img = cv2.imread(path)
#     cv2.imshow('image', img)
#     # [[71, 181], [300, 244]]
#     # [[59, 216], [327, 268]]
#     # 216 268 59 327

#     croped_img = img[385:531, 233:508]
#     cv2.imshow('croped', croped_img)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    


if __name__ == "__main__":
    show_img()
#     raugh()

