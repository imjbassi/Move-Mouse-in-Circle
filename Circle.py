import pyautogui
import math
import time

def move_mouse_in_circle(center_x, center_y, radius, duration, num_points=100):
    for i in range(num_points):
        angle = i * (2 * math.pi / num_points)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        pyautogui.moveTo(x, y, duration=duration / num_points)

def main():
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width / 2, screen_height / 2
    radius = 100
    duration = 5  # Time in seconds to complete one circle

    print("Press Ctrl-C to stop.")
    try:
        while True:
            move_mouse_in_circle(center_x, center_y, radius, duration)
            pyautogui.move(-radius, 0, duration=1)  # Move mouse back to the starting point
            time.sleep(1)  # Pause for 1 second before starting the next circle
    except KeyboardInterrupt:
        print("Script stopped.")

if __name__ == "__main__":
    main()