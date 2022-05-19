import cv2
import keyboard
import pyautogui
import webbrowser
import pytesseract

def listen_key():
    keyboard.wait("alt gr+p")
    take_ss()

def take_ss():
    pyautogui.screenshot().save('ss.png')
    show_img()


def show_img():
    path = r'ss.png'
    coordinates = []
    duo_coordinates =[]
    img = cv2.imread(path)
    cv2.imshow('image', img)

    def crop_img(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:

            font = cv2.FONT_HERSHEY_TRIPLEX
            LB = '.'
        
            cv2.putText(img, LB, (x, y), font, 1, (255, 255, 0), 2) 
            cv2.imshow('image', img)

            coordinates.append([x,y])
            if (coordinates.__len__() == 2):


                cv2.rectangle(img, coordinates[0], coordinates[1], (0,0,0), 2)
                cv2.imshow('image', img)
                duo_coordinates.append(coordinates[0])
                duo_coordinates.append(coordinates[1])

                coordinates.clear()

        if event == cv2.EVENT_RBUTTONDOWN:
            x1 = duo_coordinates[0][0]
            y1 = duo_coordinates[0][1]
            w = duo_coordinates[1][0]
            h = duo_coordinates[1][1]
            try:  
                croped_img = img[y1:h, x1:w]
                cv2.imshow('croped', croped_img)
            except Exception as e:
                try:
                    croped_img = img[h:y1, w:x1]
                    cv2.imshow('croped', croped_img)
                except Exception as e:
                    try:
                        croped_img = img[y1:h, w:x1]
                        cv2.imshow('croped', croped_img)
                    except Exception as e:
                        try:  
                            croped_img = img[h:y1, x1:w]
                            cv2.imshow('croped', croped_img)
                        except Exception as e:
                            print(e)
            duo_coordinates.clear()
            text = text_recogner(croped_img)

            search(text)


    cv2.setMouseCallback('image', crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def text_recogner(image):
    text =  pytesseract.image_to_string(image)
    return text

def search(query):
    query = 'https://www.google.com/search?q='+str(query)
    webbrowser.open_new_tab(query)


if __name__ == "__main__":
    listen_key()

