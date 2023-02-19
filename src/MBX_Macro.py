from PIL import ImageGrab
import keyboard
import pyautogui
import time

MAIN_RGB = (91, 87, 242) #보라색
COFIRM_RGB = (53, 50, 168) #팝업 보라색
SUB_RGB = (55,55,55) #회색
width, height = pyautogui.size()
print(width)
print(height)
print(int(width * 20 / 100), int(height * 21 / 100), int(width * 80 / 100), int(height * 44 / 100))

def RGB_CLICK(x1, y1, x2, y2, INPUT_RGB, RANGE, N): #RGB인식 영역 / RGB색 / 색인식범위 / 프로그램이 몇초뒤에 꺼질까요?
    start_time = time.time()
    end_time = start_time + N

    shot = 0 #목표물 찾았는지 확인하는 변수
    c_start = (x1,y1) #캡처영역 좌측상단 포인트
    c_end = (x2,y2) #캡처영역 우측하단 포인트
    c_xbox = INPUT_RGB #(91, 87, 242) #RGB값
    
    while start_time < end_time:
        screenshot = ImageGrab.grab()
        for i in range(c_end[0],c_start[0],-10):
            for j in range(c_end[1],c_start[1],-10):
                RGB = screenshot.getpixel((i,j)) #각 좌표에서 RGB값 추출
                #RGB 확인
                #print(abs(RGB[0]),abs(c_xbox[0]),abs(RGB[0]-c_xbox[0]),abs(RGB[1]),abs(c_xbox[1]),abs(RGB[1]-c_xbox[1]),abs(RGB[2]),abs(c_xbox[2]),abs(RGB[2]-c_xbox[2]))
                if abs(RGB[0]-c_xbox[0]) + abs(RGB[1]-c_xbox[1]) + abs(RGB[2]-c_xbox[2]) < RANGE:
                    print(abs(RGB[0]),abs(c_xbox[0]),abs(RGB[0]-c_xbox[0]),abs(RGB[1]),abs(c_xbox[1]),abs(RGB[1]-c_xbox[1]),abs(RGB[2]),abs(c_xbox[2]),abs(RGB[2]-c_xbox[2]))
                    pyautogui.click((i - 5,j - 5))
                    shot = 1
                    break
                elif shot == 1:
                    break
            if shot == 1:
                break
        break

def main():
    while True:
        #커넥트 월렛부분 클릭
        if keyboard.is_pressed('F2'):
            RGB_CLICK(int(width * 10 / 100), int(height * 21 / 100), int(width * 90 / 100), int(height * 50 / 100), MAIN_RGB, 50, 1)
        #메인화면에서 한단 내려가고 buynow 클릭
        if keyboard.is_pressed('F3'):
            keyboard.press_and_release('pagedown')
            RGB_CLICK(int(width * 10 / 100), int(height * 60 / 100), int(width * 90 / 100), int(height * 90 / 100), MAIN_RGB, 50, 1)
        #팝업창 뜨면 자동완성 비번치고 엔터
        if keyboard.is_pressed('F4'):
            time.sleep(1)
            keyboard.press_and_release('tab')
            time.sleep(1)
            RGB_CLICK(int(width * 10 / 100), int(height * 60 / 100), int(width * 90 / 100), int(height * 90 / 100), MAIN_RGB, 50, 1)
            keyboard.press_and_release('enter')
        elif keyboard.is_pressed('F10'):
            break

if __name__ == '__main__':
    main()