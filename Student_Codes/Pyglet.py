
# Type "pip install pyglet" into the command terminal if you havent already installed the library

#import the necessary libraries to get started
import pyglet

#   Shapes are required for drawing and displaying the shapes used in this template (Wow thats sooo cool)
from pyglet import shapes

#   Mouse is used for mouse related funcitons (Who'd have thought?)
from pyglet.window import mouse

#   Key is necessary for all keyboard related functions (THATS CRAAAZYY)
from pyglet.window import key

#   Math was imported to make the circle pulsate (Line 102) and the star revolve around a given Anchor Point (Line 107/108)
from math import sin, cos

#   Here is how you get your window open
#   Changing the width and height of the window is measured in pixels and the caption is what the window is labeled at the top
window = pyglet.window.Window(width=1280, height=720, caption="Hello Pyglet!")
window.set_location(0, 30)

#Setting the mouse as invisible is how we were able to "Change the Cursor"
window.set_mouse_visible(False)


# Here we are setting a variable (I went with "batch" to keep it simple) so that we can efficiently 
# render all the shapes in this template
batch = pyglet.graphics.Batch()


#   A shapes location is reletive to the bottom left corner of the window
#   For the circle I set the radius to 100 followed by setting its color to green. color=Red,Green,Blue (Limited to 255)
#   The end I make all the shapes render in using the variable we set earlier 'batch=batch'
circle = shapes.Circle(x=600, y=150, radius=100, color=(50, 225, 30), batch=batch)


#   A square is just a rectangle but with even sides. We will be making this spin later on in the "Updates" function
square = shapes.Rectangle(x=300, y=300, width=200, height=200, color=(55, 55, 255), batch=batch)

#   I set the square's anchor position to half its height and width so that when we make it spin it won't be spinning relative to it's 
#   bottom right corner
square.anchor_position = (100, 100)


#   I Changed this rectangles opacity/transparency with '.opacity' with it set to 100 (0) is the least transparent
#   I also changed its rotation because I felt like it
rectangle = shapes.Rectangle(x=350, y=350, width=100, height=50, batch=batch)
rectangle.opacity = 100
rectangle.rotation = 33


#   A line is like a rectangle except you change it's length via coordinates
line1 = shapes.Line(x=100, y=100, x2=200, y2=200, width=19, batch=batch)
line2 = shapes.Line(x=150, y=150, x2=444, y2=111, width=4, color=(200, 20, 20), batch=batch)


#   Setting the star is fairly self explanitory. I will make this revolve around it's anchor point in the "Updates" function
star = shapes.Star(x=1000, y=300, outer_radius=60, inner_radius=40, num_spikes=8, color=(255, 255, 0), batch=batch)


#   First I made the cursor small and green
cursor = shapes.Circle(x=700, y=150, radius=10, color=(55, 255, 30), batch=batch)

#Then I created a dot. We will make this dot "Teleport" to wherever the mouse is when a left click is made
dot = shapes.Circle(x=100, y=100, radius=25, color=(255, 0, 0), batch=batch)

#   Keyboard Shape (That's right, it's a TRIANGLE)
#   Similar to lines, you set 3 points to create the triangle
triangle = shapes.Triangle(x=500, y=500, x2=550, y2=600, x3=600, y3=500, batch=batch)

#   Now that all of the shapes have been made, you might have noticed that they don't appear on screen when you run the program. 
#   We need to create a "@window.event" and draw function that creates the shapes
#   To do this, simply add the next 4 lines of code
@window.event
def on_draw():
    window.clear()
    batch.draw()

#   Now onto the good stuff
#   Start by creating another event
@window.event

#   This function sets the cursor shape's position to the mouse position
def on_mouse_motion(x: int, y: int, dx: int, dy: int):
    #   You can do this with any shape, not just one's named cursor
    cursor.position = (x, y)

#   Now we will set the "red" dot we made to move to wherever the user(Thats YOU :D) clicks
@window.event
def on_mouse_press(x: int, y: int, button: int, modifiers: int):
    #   You could technically bind this to any mouse key if you want instead of just LEFT
    if button & mouse.LEFT:
        dot.position = (x, y)


#Keyboard Functions

#   First I made a dictionary. This will allow us to create a continuous motion when a key is held instead of it simply "teleporting"
directions = {'left': False, 'right': False, 'up': False, 'down': False}
#   Speed sets how many pixels the shape moves
speed = 5

#   This is how you set your keys yo the directions
#   "What is happening?" you might ask
#   We are setting the directions in the dictionary to "True" when the corresponding key is pressed
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        directions['left'] = True
    if symbol == key.D:
        directions['right'] = True
    if symbol == key.S:
        directions['down'] = True
    if symbol == key.W:
        directions['up'] = True


#   Now we have a problem. You see without any code telling the directions to switch back to false, the shape would just keep moving in 
#   the same direction until the opposite direction is pressed. When that happens you will be unable to move the shape
#   Let's fix that problem by setting the directions back to false whenever a key is released
@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.A:
        directions['left'] = False
    if symbol == key.D:
        directions['right'] = False
    if symbol == key.S:
        directions['down'] = False
    if symbol == key.W:
        directions['up'] = False
    
#   Almost done
#   Here we are going to set a value to 0
#   This is so we can use math to our advantage and make coding this significantly easier
value = 0

# The bread and butter
def update(dt):
    # Wow it's that variable from earlier, we set it to global and begin incrementing the number so that when we use 
    # sin and cos functions from the math import we get the desired effects.
    global value
    value += 0.05

    #   Here we set the circle's radius to equal the sin of the constantly increasing value
    #   This gives us the pulsating effect we wanted
    circle.radius += sin(value)

    #   Now we increment the squared rotation so that it spins
    square.rotation += 1

    # I did the same this with the star, however I also used math to get the star to revolve around its anchor point
    star.rotation += 2

    # Read carefully here (I made typos and was confused)
    star.x += cos(value) * 8
    star.y += sin(value) * 8


    #   Here we update the triangle's position using these if statements
    #   Try not to mix any of them up
    if directions['left'] == True:
        triangle.x -= speed
    if directions['right'] == True:
        triangle.x += speed
    if directions['down'] == True:
        triangle.y -= speed
    if directions['up'] == True:
        triangle.y += speed

#   AAAAANNNDD FINALLY
#   All thats left to do is schedule an interval for the window to update at (I did 60 fps)
pyglet.clock.schedule_interval(update, 1/60)

#   And use this little gem to finish it all off
pyglet.app.run()



#   If you're feeling devious remove the "window.clear()" on line 78 then run the program again