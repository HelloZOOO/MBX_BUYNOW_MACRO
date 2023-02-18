from PIL import ImageGrab
import keyboard
import pyautogui
import time

width, height = pyautogui.size()
print(width)
print(height)

def RGB_CLICK(x1, y1, x2, y2, N): #RGB인식 영역 / 프로그램이 몇초뒤에 꺼질까요?
    start_time = time.time()
    end_time = start_time + N

    shot = 0 #목표물 찾았는지 확인하는 변수
    c_start = (x1,y1) #캡처영역 좌측상단 포인트
    c_end = (x2,y2) #캡처영역 우측하단 포인트
    c_xbox = (91, 87, 242) #RGB값
    
    while start_time < end_time:
        screenshot = ImageGrab.grab()
        for i in range(c_start[0],c_end[0],10):
            for j in range(c_start[1],c_end[1],10):
                RGB = screenshot.getpixel((i,j)) #각 좌표에서 RGB값 추출
                if abs(RGB[0]-c_xbox[0]) + abs(RGB[1]-c_xbox[1]) + abs(RGB[2]-c_xbox[2]) < 10:
                    pyautogui.click((i + 20,j + 20))
                    shot = 1
                    break
            if shot == 1:
                shot = 0
                break
        if time.time() > end_time:                                                                                                                                 
            break

def function_to_run():
    print("F2가 입력되었습니다.")

def main():
    while True:
        if keyboard.is_pressed('F2'):
            RGB_CLICK(100, 400, width-100, 800, 3)
            break
        elif keyboard.is_pressed('F3'):
            break

if __name__ == '__main__':
    main()

RGB_CLICK(100, 400, width-100, 800, 3)