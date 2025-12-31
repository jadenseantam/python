import keyboard

def on_key_event(event):
    print(event.name)

# Add a listener for keyboard events
keyboard.hook(on_key_event)

# Keep the program running
keyboard.wait("") 