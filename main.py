def go_again():
    from turtle import Turtle, Screen
    import random

    # Size on screen
    size = 2

    # screen declaration and canvas size
    screen = Screen()
    screen.setup(width=(500*size), height=(400*size))

    # Turtle Attributes
    colors = ["purple", "red", "yellow", "blue", "orange", "green", "cyan"]
    # Turtle Colors
    colors_attribute = ["purple", "red", "yellow", "blue", "orange", "green", "cyan"]

    # Turtle Y axis starting position
    position = -150

    # Turtle attributes, generated with the names in the colors list
    for x in range(len(colors)):
        colors[x] = Turtle()
        colors[x].hideturtle()
        colors[x].penup()
        colors[x].speed(10)
        colors[x].shape("turtle")
        colors[x].color(colors_attribute[x])
        colors[x].shapesize((1.5 * size))
        colors[x].goto(x=-200*size, y=position*size)
        colors[x].showturtle()
        position += 50

    # User bet, prompt
    user_bet = screen.textinput(title="Make your bet", prompt=("Which turtle will win the race? Enter Color between \n"
                                                               f"{colors_attribute}: "))

    x = 0
    while 1 > x:
        for turtle in colors:
            if turtle.xcor() > (220*size):
                x += 1
                winning_turtle = turtle.pencolor()
                if winning_turtle == user_bet:
                    print(f"You've won, the winning turtle was {turtle.pencolor()}")
                    user_play_again = screen.textinput(title="Play again", prompt=f"You won, The winning turtle was "
                                                                                  f"{turtle.pencolor()} "
                                                                                  f"Do you want to play again? y / n: ")
                else:
                    print(f"You lost, winning turtle was {turtle.pencolor()}")
                    user_play_again = screen.textinput(title="Play again", prompt=f"You lost, the winning turtle was "
                                                                                  f"{turtle.pencolor()} "
                                                                                  f"Do you want to play again? y / n: ")
                if user_play_again == "y":
                    screen.clear()
                    go_again()

            random_pace = random.randint(0, 10)
            turtle.forward(random_pace)

    screen.exitonclick()


go_again()
