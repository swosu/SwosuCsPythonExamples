# Software Design Major Steps

Notes from 4/14 meeting with Marc Leonard, Jessica Massey, Riley Smith,
Brian Rickel, and Marc Crume.

## Install tensorflow
Get this to work on a laptop first and then on a raspberry pi.

## Detect a Single Cone
- Identify a cone in the camera feed
- Get X location of cone
  - cone_1_x_location = get_cone_center()
- Find range of x values for image
  - x_range = get_image_pixel_width()
- Find area of cone
  - cone_1_area = get_cone_area()

## Detect Second Cone
- ? Maybe hide or ignore first cone.
- Identify a (second) cone in the camera feed
- Get X location of (second) cone
  - cone_2_x_location = get_cone_center()
- Find area of cone
  - cone_1_area = get_cone_area()

## ? No Second Cone ?
If no second cone...
- if cone_1_x_location < x_range/2
  - transmit_turn_hard_left
- else
  - transmit_turn_hard_right

## Second Cone Found
else
- if cone_1_area > cone_2_area
  - if cone_1_x_location <  cone_2_x_location
    - transmit_turn_gentle_right
  - else
    - transmit_turn_gentle_left

- else (cone 2 is bigger)
  - if cone_2_x_location < cone_1_x_location
    - transmit_turn_gentle_right
  - else
    - transmit_turn_gentle_left

- if cone_1_area == cone_2_area
  - transmit_go_straight()

- if no cones found
  - transmit_go_straight
