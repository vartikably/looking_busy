import pyautogui, time
width, height = pyautogui.size()
x,y = pyautogui.position()
while True:
    if (x>= 0 and x<(width-10)) and (y>= 0 and y<(height-10)):
        pyautogui.moveRel(15, 15, duration=0.10)
    elif (x>=(width-10)) and (y>=0 and y<(height-10)):
        pyautogui.moveTo(10, y+15, duration=0.10)
    elif (x >= 0  and x<(width-10)) and (y >= (height-10)):
        pyautogui.moveTo(x+15, 5, duration=0.10)
    elif (x>(width-10)) and y>(height-10):
        pyautogui.moveTo(10,5,duration=0.10)
    print("cursor mov")
    x, y = pyautogui.position()
    print(x, y)
    time.sleep(10)
