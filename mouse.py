from pymouse import PyMouse

def mouse_Click(x, y):
    m = PyMouse()
    m.position()
    m.move(x,y)
    m.click(x,y)
    m.press(x,y)
    m.release(x,y)
    m.press(x,y)
    m.release(x,y)
