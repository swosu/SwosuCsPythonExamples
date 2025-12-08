import turtle
import random

width = 600 #pixels
height = 600 #pixels
delay = 100 # milliseconds
food_size = 32 #pixels
snake_size = 20 #pixels
score = 0

offsets = {
    "up": (0, snake_size),
    "down": (0, -snake_size),
    "left": (-snake_size, 0),
    "right": (snake_size, 0)
}

def game_loop():
    global score
    stamper.clearstamps()
    stamper.penup() 
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    #Check for collision with walls
    if new_head in snake or new_head[0] < -width // 2 or new_head[0] > width // 2 - 20 or new_head[1] < -height // 2 or new_head[1] > height // 2 - 20:
        stamper.goto(0, 0)
        reset()
        return
    
    else:

        snake.append(new_head)

        if not food_collision():
            snake.pop(0)


        for segment in snake[:-1]:
            stamper.shape("snake-head-20x20.gif")
            stamper.goto(snake[-1][0], snake[-1][1])
            stamper.stamp()
            stamper.shape("circle")
            
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        screen.title(f"Snake    Score: {score}")
        screen.update()
        screen.ontimer(game_loop, delay)

def reset():
    global snake, snake_direction, food_pos, score
    snake = [[0, 0], [snake_size, 0], [snake_size * 2, 0], [snake_size * 3, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    score = 0
    game_loop()

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def get_random_food_pos():
    x = random.randint(-width // 2 + food_size, width // 2 - food_size)
    y = random.randint(-height // 2 + food_size, height // 2 - food_size)
    return (x, y)

def bind_directions():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("right"), "Right")

def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":
            snake_direction = "up"
    
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"

    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"

    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgpic("bg2.gif")  # Ensure you have a background.gif file in the same directory
screen.register_shape("snake-food-32x32.gif")  # Ensure you have a snake-food-32x32.gif file in the same directory
screen.register_shape("snake-head-20x20.gif")  # Ensure you have a snake-head-32x32.gif file in the same directory
screen.tracer(0)


screen.listen()
bind_directions()



stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("#009ef1")
stamper.penup()


food = turtle.Turtle()
food.shape("snake-food-32x32.gif")
food.color("red")
food.shapesize(food_size / 20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)


snake = [[0, 0], [snake_size, 0], [snake_size * 2, 0], [snake_size * 3, 0]]
snake_direction = "up"
game_loop()
turtle.done()