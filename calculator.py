from graphics import *


def main():
    win = GraphWin("Calculator", 600, 600)
    ans = 0
    screen = ''
    input_box = Entry(Point(300, 75), 20)
    input_box.setText("0")
    input_box.draw(win)
    division = Rectangle(Point(600, 200), Point(450, 100))
    Text(Point(525, 150), '/').draw(win)
    x = Rectangle(Point(600, 300), Point(450, 200))
    Text(Point(525, 250), 'x').draw(win)
    mines = Rectangle(Point(600, 400), Point(450, 300))
    Text(Point(525, 350), '-').draw(win)
    plus = Rectangle(Point(600, 500), Point(450, 400))
    Text(Point(525, 450), '+').draw(win)
    equal = Rectangle(Point(600, 600), Point(450, 500))
    Text(Point(525, 550), '=').draw(win)
    division.draw(win)
    x.draw(win)
    mines.draw(win)
    plus.draw(win)
    equal.draw(win)

    percent = Rectangle(Point(450, 200), Point(300, 100))
    Text(Point(375, 150), '%').draw(win)
    nine = Rectangle(Point(450, 300), Point(300, 200))
    Text(Point(375, 250), '9').draw(win)
    six = Rectangle(Point(450, 400), Point(300, 300))
    Text(Point(375, 350), '6').draw(win)
    three = Rectangle(Point(450, 500), Point(300, 400))
    Text(Point(375, 450), '3').draw(win)
    two_xx = Rectangle(Point(450, 600), Point(300, 500))
    Text(Point(375, 550), '**').draw(win)
    nine.draw(win)
    percent.draw(win)
    six.draw(win)
    three.draw(win)
    two_xx.draw(win)

    change_sign = Rectangle(Point(300, 200), Point(150, 100))
    Text(Point(225, 150), '+/-').draw(win)
    eight = Rectangle(Point(300, 300), Point(150, 200))
    Text(Point(225, 250), '8').draw(win)
    five = Rectangle(Point(300, 400), Point(150, 300))
    Text(Point(225, 350), '5').draw(win)
    two = Rectangle(Point(300, 500), Point(150, 400))
    Text(Point(225, 450), '2').draw(win)
    zero = Rectangle(Point(300, 600), Point(0, 500))
    Text(Point(150, 550), '0').draw(win)
    change_sign.draw(win)
    eight.draw(win)
    five.draw(win)
    two.draw(win)
    zero.draw(win)

    ac = Rectangle(Point(150, 200), Point(0, 100))
    Text(Point(75, 150), 'AC').draw(win)
    seven = Rectangle(Point(150, 300), Point(0, 200))
    Text(Point(75, 250), '7').draw(win)
    four = Rectangle(Point(150, 400), Point(0, 300))
    Text(Point(75, 350), '4').draw(win)
    one = Rectangle(Point(150, 500), Point(0, 400))
    Text(Point(75, 450), '1').draw(win)
    ac.draw(win)
    seven.draw(win)
    four.draw(win)
    one.draw(win)

    operation = 0
    n = 0
    type_nums = False
    start = True
    equal=False

    while True:
        try:
            click = win.getMouse()
            a = click.getX()
            b = click.getY()

            if operation != 0 and not type_nums:
                input_box.setText('')

            if 300 < a < 450 and 200 < b < 300:
                if equal:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                else:
                    type_nums = True
                    screen = screen + "9"
                    input_box.setText(screen)
                    n = 0
                    start = False
            elif 300 < a < 450 and 300 < b < 400:
                if equal:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                else:
                    type_nums = True
                    screen = screen + "6"
                    input_box.setText(screen)
                    n = 0
                    start = False
            elif 300 < a < 450 and 400 < b < 500:
                if equal:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                else:
                    type_nums = True
                    screen = screen + "3"
                    input_box.setText(screen)
                    n = 0
                    start = False
            elif 150 < a < 300 and 200 < b < 300:
                if equal:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                else:
                    type_nums = True
                    screen = screen + "8"
                    input_box.setText(screen)
                    n = 0
                    start = False
            elif 150 < a < 300 and 300 < b < 400:
                if equal:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                else:
                    type_nums = True
                    screen = screen + "5"
                    input_box.setText(screen)
                    n = 0
                    start = False
            elif 150 < a < 300 and 400 < b < 500:
                type_nums = True
                screen = screen + '2'
                input_box.setText(screen)
                n = 0
                start = False
            elif 0 < a < 300 and 500 < b < 600:
                if equal or start == True:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                else:
                    type_nums = True
                    screen = screen + "0"
                    input_box.setText(screen)
                    n = 0
                    start = False
            elif 0 < a < 150 and 200 < b < 300:
                if equal:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                else:
                    type_nums = True
                    screen = screen + "7"
                    input_box.setText(screen)
                    n = 0
                    start = False
            elif 0 < a < 150 and 300 < b < 400:
                if equal:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                else:
                    type_nums = True
                    screen = screen + "4"
                    input_box.setText(screen)
                    n = 0
                    start = False
            elif 0 < a < 150 and 400 < b < 500:
                if equal:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                else:
                    type_nums = True
                    screen = screen + "1"
                    input_box.setText(screen)
                    n = 0
                    start = False
            # AC
            elif 0 < a < 150 and 100 < b < 200:
                type_nums = False
                input_box.setText("0")
                ans = 0
                screen = ""
                operation = 0
                n = 0
                start = True
                equal=False
            # plus (+)
            elif 450 < a < 600 and 400 < b < 500:
                type_nums = False
                if operation == 0 and start == False:
                    try:
                        ans = int(screen)
                    except:
                        ans = float(screen)
                    screen = ""
                elif n == 1 or start == True:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                    continue
                elif operation == 1:
                    try:
                        ans = ans + int(screen)
                    except:
                        ans = ans + float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 2:
                    try:
                        ans = ans * int(screen)
                    except:
                        ans = ans * float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 3:
                    try:
                        ans = ans / int(screen)
                    except:
                        ans = ans / float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 4:
                    try:
                        ans = ans - int(screen)
                    except:
                        ans = ans - float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 6:
                    try:
                        ans = ans ** int(screen)
                    except:
                        ans = ans ** float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 7:
                    try:
                        ans = ans % int(screen)
                    except:
                        ans = ans % float(screen)
                    input_box.setText(ans)
                    screen = ""
                operation = 1
                n = 1
                start = True
            # equal (=)
            elif 450 < a < 600 and 500 < b < 600:
                type_nums = False
                if start:
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal = False
                    continue
                elif operation == 0:
                    try:
                        ans = int(screen)
                    except:
                        ans = float(screen)
                    screen = ""
                elif operation == 1:
                    try:
                        ans = ans + int(screen)
                    except:
                        ans = ans + float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 2:
                    try:
                        ans = ans * int(screen)
                    except:
                        ans = ans * float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 3:
                    try:
                        ans = ans / int(screen)
                    except:
                        ans = ans / float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 4:
                    try:
                        ans = ans - int(screen)
                    except:
                        ans = ans - float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 6:
                    try:
                        ans = ans ** int(screen)
                    except:
                        ans = ans ** float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 7:
                    try:
                        ans = ans % int(screen)
                    except:
                        ans = ans % float(screen)
                    input_box.setText(ans)
                    screen = ""
                screen = str(ans)
                screen = screen.rstrip('0').rstrip('.') if '.' in screen else screen
                input_box.setText(screen)
                ans = 0
                operation = 0
                equal=True
            # mines (-)
            elif 450 < a < 600 and 300 < b < 400:
                type_nums = False
                if operation == 0 and start == False:
                    try:
                        ans = int(screen)
                    except:
                        ans = float(screen)
                    screen = ""
                elif n == 1 or start == True:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                    continue
                elif operation == 1:
                    try:
                        ans = ans + int(screen)
                    except:
                        ans = ans + float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 2:
                    try:
                        ans = ans * int(screen)
                    except:
                        ans = ans * float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 3:
                    try:
                        ans = ans / int(screen)
                    except:
                        ans = ans / float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 4:
                    try:
                        ans = ans - int(screen)
                    except:
                        ans = ans - float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 6:
                    try:
                        ans = ans ** int(screen)
                    except:
                        ans = ans ** float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 7:
                    try:
                        ans = ans % int(screen)
                    except:
                        ans = ans % float(screen)
                    input_box.setText(ans)
                    screen = ""
                operation = 4
                n = 1
                start = True
            # plus and mines (- +)
            elif 150 < a < 300 and 100 < b < 200:
                type_nums = False
                if start == True:
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    equal=False
                else:
                    try:
                        screen = int(screen) * -1
                    except:
                        screen = float(screen) * -1
                    input_box.setText(screen)
                    screen = str(screen)
                    n = 0
                    equal=False
            # Multiply (x)
            elif 450 < a < 600 and 200 < b < 300:
                type_nums = False
                if operation == 0 and start == False:
                    try:
                        ans = int(screen)
                    except:
                        ans = float(screen)
                    screen = ""
                elif n == 1 or start == True:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                    continue
                elif operation == 1:
                    try:
                        ans = ans + int(screen)
                    except:
                        ans = ans + float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 2:
                    try:
                        ans = ans * int(screen)
                    except:
                        ans = ans * float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 3:
                    try:
                        ans = ans / int(screen)
                    except:
                        ans = ans / float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 4:
                    try:
                        ans = ans - int(screen)
                    except:
                        ans = ans - float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 6:
                    try:
                        ans = ans ** int(screen)
                    except:
                        ans = ans ** float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 7:
                    try:
                        ans = ans % int(screen)
                    except:
                        ans = ans % float(screen)
                    input_box.setText(ans)
                    screen = ""
                operation = 2
                n = 1
                start = True
            # division (/)
            elif 450 < a < 600 and 100 < b < 200:
                type_nums = False
                if operation == 0 and start == False:
                    try:
                        ans = int(screen)
                    except:
                        ans = float(screen)
                    screen = ""
                elif n == 1 or start == True:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                    continue
                elif operation == 1:
                    try:
                        ans = ans + int(screen)
                    except:
                        ans = ans + float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 2:
                    try:
                        ans = ans * int(screen)
                    except:
                        ans = ans * float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 3:
                    try:
                        ans = ans / int(screen)
                    except:
                        ans = ans / float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 4:
                    try:
                        ans = ans - int(screen)
                    except:
                        ans = ans - float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 6:
                    try:
                        ans = ans ** int(screen)
                    except:
                        ans = ans ** float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 7:
                    try:
                        ans = ans % int(screen)
                    except:
                        ans = ans % float(screen)
                    input_box.setText(ans)
                    screen = ""
                operation = 3
                n = 1
                start = True
            # power (**)
            elif 300 < a < 450 and 500 < b < 600:
                type_nums = False
                if operation == 0 and start == False:
                    try:
                        ans = int(screen)
                    except:
                        ans = float(screen)
                    screen = ""
                elif n == 1 or start == True:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                    continue
                elif operation == 1:
                    try:
                        ans = ans + int(screen)
                    except:
                        ans = ans + float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 2:
                    try:
                        ans = ans * int(screen)
                    except:
                        ans = ans * float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 3:
                    try:
                        ans = ans / int(screen)
                    except:
                        ans = ans / float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 4:
                    try:
                        ans = ans - int(screen)
                    except:
                        ans = ans - float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 6:
                    try:
                        ans = ans ** int(screen)
                    except:
                        ans = ans ** float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 7:
                    try:
                        ans = ans % int(screen)
                    except:
                        ans = ans % float(screen)
                    input_box.setText(ans)
                    screen = ""
                operation = 6
                n = 1
                start = True
            # module (%)
            elif 300 < a < 450 and 100 < b < 200:
                type_nums = False
                if operation == 0 and start == False:
                    try:
                        ans = int(screen)
                    except:
                        ans = float(screen)
                    screen = ""
                elif n == 1 or start == True:
                    type_nums = False
                    input_box.setText("0")
                    ans = 0
                    screen = ""
                    operation = 0
                    n = 0
                    start = True
                    equal=False
                    continue
                elif operation == 1:
                    try:
                        ans = ans + int(screen)
                    except:
                        ans = ans + float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 2:
                    try:
                        ans = ans * int(screen)
                    except:
                        ans = ans * float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 3:
                    try:
                        ans = ans / int(screen)
                    except:
                        ans = ans / float(screen)
                    input_box.setText(ans)
                    screen = ""

                elif operation == 4:
                    try:
                        ans = ans - int(screen)
                    except:
                        ans = ans - float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 6:
                    try:
                        ans = ans ** int(screen)
                    except:
                        ans = ans ** float(screen)
                    input_box.setText(ans)
                    screen = ""
                elif operation == 7:
                    try:
                        ans = ans % int(screen)
                    except None:
                        ans = ans % float(screen)
                    input_box.setText(ans)
                    screen = ""
                operation = 7
                n = 1
                start = True
        except GraphicsError:
            win.close()
            break



main()
