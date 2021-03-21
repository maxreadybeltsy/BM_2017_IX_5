import turtle

import libs.auxiliar as aux
import libs.input_dates as info
import libs.develops as dev

if __name__ == '__main__':



    # step - measure of one square#
    pas = 30

    # squere count in one cadran #
    n = 7

    #create grid and axes
    aux.draw_grid(n, pas)

    # ----------------------- #
    t = turtle.Turtle()
    steps = info.get_info()
    point_list = dev.create_point(steps)
    dev.draw_points(t, point_list, pas)
    # ----------------------
    turtle.Screen().mainloop()