import arcade

arcade.open_window(600,600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

#draw a lrtb rectangle
arcade.draw_lrtb_rectangle_filled(0,599,300,0, arcade.csscolor.GREEN)

#or draw centerx, centery, width, height rectangle
arcade.draw_rectangle_filled(100,320,20,60,arcade.csscolor.SIENNA)

# circle centerx, centery, radius
arcade.draw_circle_filled(100,350,30,arcade.csscolor.DARK_GREEN)

#ellipse centerx, centery, width, height
#arcade.draw_rectangle_outline(300,300,350,200,arcade.csscolor.BLACK, 3)
#arcade.draw_ellipse_outline(300,300,350,200,arcade.csscolor.RED, 3)

arcade.draw_rectangle_filled(200,320,20,60,arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200,370,60,80,arcade.csscolor.DARK_GREEN)

#arc centerx, centery,width, height, color, start angle, end angle
arcade.draw_rectangle_filled(300,320,20,60,arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300,340,60,100,arcade.csscolor.DARK_GREEN,0,180)

arcade.draw_rectangle_filled(400,320,20,60,arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400,400,370,320,430,320,arcade.csscolor.DARK_GREEN)

# polygon list of point-pairs
arcade.draw_rectangle_filled(500,320,20,60,arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500,400),(480,360),(470,320),(530,320),(520,360)),arcade.csscolor.DARK_GREEN)

arcade.draw_circle_filled(500,550,40,arcade.csscolor.YELLOW)
arcade.draw_line(500,550,400,550,arcade.csscolor.YELLOW,3)
arcade.draw_line(500,550,600,550,arcade.csscolor.YELLOW,3)
arcade.draw_line(500,550,500,450,arcade.csscolor.YELLOW,3)
arcade.draw_line(500,550,500,650,arcade.csscolor.YELLOW,3)

arcade.draw_line(500,550,550,600,arcade.csscolor.YELLOW,3)
arcade.draw_line(500,550,550,500,arcade.csscolor.YELLOW,3)
arcade.draw_line(500,550,450,600,arcade.csscolor.YELLOW,3)
arcade.draw_line(500,550,450,500,arcade.csscolor.YELLOW,3)

#text text, x,y,color,font
arcade.draw_text("Arbor Day - Plant a Tree", 150,230,arcade.csscolor.BLACK,24)

arcade.finish_render()

arcade.run()
