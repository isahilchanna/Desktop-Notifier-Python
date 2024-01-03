from plyer import notification
import time
def notifyy():
    title = 'Hi, Hello and Hi !'

    message = 'If u reading this ~I LOVE U TO THE MOON AND BACK !!'

    notification.notify(title = title,
                        message = message,
                        #creating icon for the notification
                        app_icon = "heart.ico",
                        #the notification stays for 15sec
                        timeout = 15,
                        toast = False)
if __name__ == '__main__':
    while True:
        notifyy()
        #sleep for 4 hrs => 60*60*4 sec
        time.sleep(0)