import simpleguitk as simplegui

frame_width = 800;
frame_height = 600;
ball_position = [frame_width/2, frame_height/2];
ball_radius = 8;
ball_border = 2*ball_radius;
ball_vel = [3, 3];
gutter_width = 16;

left_bar_position_u = [0, (frame_height/2 - 50)];
left_bar_position_d = [0, (frame_height/2 + 50)];

right_bar_position_u = [frame_width, (frame_height/2 - 50)];
right_bar_position_d = [frame_width, (frame_height/2 + 50)];

left_count = 0;
right_count = 0;

def ball_bars_gutters(canvas):
    global left_count, right_count;

    #Creating Gutters
    canvas.draw_line([gutter_width, 0], [(frame_width - (frame_width - gutter_width)), frame_height], 4, "White");
    canvas.draw_line([(frame_width - gutter_width), 0], [(frame_width - gutter_width), frame_height], 4, "White");

    #Creating middle line
    canvas.draw_line([frame_width/2, 0], [frame_width/2, frame_height], 4, "White");

    #Creating Bars
    canvas.draw_line(left_bar_position_u, left_bar_position_d, 2*gutter_width, "Red");
    canvas.draw_line(right_bar_position_u, right_bar_position_d, 2*gutter_width, "Red");

    #Creating Ball
    canvas.draw_circle(ball_position, ball_radius, ball_border, "White");

    #Giving initial spark to ball
    ball_position[0] += ball_vel[0];
    ball_position[1] += ball_vel[1];

    #Limiting ball to the edges of the frame
    if((ball_position[0] <= ball_radius) or (ball_position[0] >= (frame_width-ball_radius))):
        ball_vel[0] = -ball_vel[0];
    if((ball_position[1] <= ball_radius) or (ball_position[1] >= (frame_height-ball_radius))):
        ball_vel[1] = -ball_vel[1];

    #Adding initial score
    canvas.draw_text(left_count, [(frame_width/2) - 250, 150], 14, "White");
    canvas.draw_text(right_count, [(frame_width/2) + 150, 150], 14, "White");

    #Bouncing back ball after hitting bars
    if(ball_position[0] <= (ball_radius + gutter_width)):
        if((ball_position[1] >= left_bar_position_u[1]) and (ball_position[1]) <= left_bar_position_d[1]):
            ball_vel[0] = -ball_vel[0] * 2;
            ball_vel[1] = -ball_vel[1];
            right_count += 1;
            canvas.draw_text(right_count, [(frame_width/2) + 150, 150], 14, "White");

    if(ball_position[0] >= ((frame_width - gutter_width) - ball_radius)):
        if((ball_position[1] >= right_bar_position_u[1]) and (ball_position[1] <= right_bar_position_d[1])):
            ball_vel[0] = -ball_vel[0]/2;
            ball_vel[1] = -ball_vel[1];
            left_count += 1;
            canvas.draw_text(left_count, [(frame_width/2) - 250, 150], 14, "White");

def keydown(key):

    #Movement of bars
    if(chr(key) == '%'):
        left_bar_position_u[1] -= 50;
        left_bar_position_d[1] -= 50;
    if(chr(key) == "'"):
        left_bar_position_u[1] += 50;
        left_bar_position_d[1] += 50;
    if(chr(key) == '&'):
        right_bar_position_u[1] -= 50;
        right_bar_position_d[1] -= 50;
    if(chr(key) == '('):
        right_bar_position_u[1] += 50;
        right_bar_position_d[1] += 50;

    #Limiting bars to the edge of the frame
    if(left_bar_position_u[1] <= 0):
        left_bar_position_u[1] = 0;
        left_bar_position_d[1] = 100;

    if(left_bar_position_d[1] >= 600):
        left_bar_position_u[1] = 500;
        left_bar_position_d[1] = 600;

    if(right_bar_position_u[1] <= 0):
        right_bar_position_u[1] = 0;
        right_bar_position_d[1] = 100;

    if(right_bar_position_d[1] >= 600):
        right_bar_position_u[1] = 500;
        right_bar_position_d[1] = 600;

#Creating Frame
frame = simplegui.create_frame("Pong Game", frame_width, frame_height);

frame.set_draw_handler(ball_bars_gutters);

frame.set_keydown_handler(keydown);

frame.start();