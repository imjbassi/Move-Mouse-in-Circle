<sup>I'm probably never going to update this again</sup>
# Move-Mouse-in-Circle
A testing script I made to see if Python runs properly on my mac

<img src="https://raw.githubusercontent.com/imjbassi/Move-Mouse-in-Circle/main/CarbonsCode.png" width="600">

## Explanation

The script includes two functions:

- `move_mouse_in_circle(center_x, center_y, radius, duration, num_points)`: This function moves the mouse cursor in a circular path on the screen. It calculates the coordinates of points along the circle's circumference based on the given parameters.

- `main()`: This function sets up the main parameters for the circular motion and enters a continuous loop. It repeatedly calls the `move_mouse_in_circle` function to move the mouse cursor in a circular path and then back to the starting point. The loop continues until a KeyboardInterrupt is detected.
