import keyboard

def on_key_event(event):
    print(f'Key {event.name} {event.event_type}')

# Add a listener for keyboard events
keyboard.hook(on_key_event)

# Keep the program running
keyboard.wait('esc')  # Press Esc to exit