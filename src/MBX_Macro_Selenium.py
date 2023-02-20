from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

from PIL import ImageGrab
import keyboard
import pyautogui
import time
import datetime
import os

URL = "https://playone.marblex.io/ino/63dca20a2e19433d0e44ec1f/63edd3feb7b1b61da2d26360"
directory_chrome = r"C:\Users\thqud\AppData\Local\Google\Chrome\User Data" # 크롬 계정데이터 모여있는 폴더 chrome://version

USING_CHROME_PROFILE = False
NUM_CHROME_PROFILE = 0

#####################크롬 프로필 리스트화###################

# 해당 문자가 포함된 폴더만 리스트화 시키겠다 (프로필 뒤에 공백 필수)
include_text = 'Profile '

# 디렉토리명 필터링
DIR_PROFILE_LIST = (
    [d for d in os.listdir(directory_chrome) 
    if os.path.isdir(os.path.join(directory_chrome, d)) and include_text in d]
)

#####################셀레니움 기본 세팅#####################
options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(f"user-data-dir={directory_chrome}")

# 필요할 시 크롬 기타 프로필 (기본 프로필로 이용할거면 False 처리)
if USING_CHROME_PROFILE == True:
    options.add_argument("--profile-directory=" + DIR_PROFILE_LIST[NUM_CHROME_PROFILE])
else:
    pass

options.add_experimental_option("detach", True)  # 화면이 꺼지지 않고 유지
options.add_argument("--start-maximized")  # 최대 크기로 시작

service = Service(ChromeDriverManager().install()) # 웹드라이버 설치
driver = webdriver.Chrome(service=service, options=options) # 웹드라이버 불러오기
action = ActionChains(driver)
wait = WebDriverWait(driver, 2)

driver.get(URL)
############################################################

MAIN_RGB = (91, 87, 242) #보라색
COFIRM_RGB = (53, 50, 168) #팝업 보라색
SUB_RGB = (55,55,55) #회색
width, height = pyautogui.size()
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
                    x = i
                    y = j
                    shot = 1
                    break
                elif shot == 1:
                    break
            if shot == 1:
                break
        break
    return print(i,j)

#수동모드 
def main():
    print("수동모드 ON")
    print("에러나면 그냥 F5눌러서 새로고침하시고 BuyNow 버튼부분에서 F2 누르시면 됩니다")
    while True:
        if keyboard.is_pressed('F2'):
            while True:
                windowTabs = len(driver.window_handles)
                if windowTabs == 1:
                    RGB_CLICK(int(width * 10 / 100), int(height * 21 / 100), int(width * 90 / 100), int(height * 80 / 100), MAIN_RGB, 50, 1)
                    #print("클릭성공 시간 : ",tim)
                else :
                    print("팝업떴다!")
                    print(len(driver.window_handles))
                    break
            
            """#지워도되는부분테스트용
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/button[2]')))
            driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/button[2]').click()"""
            
            ####여기부터 BUY NOW 팝업 클릭 후 넣어주세요####
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1]) #크롬 팝업창으로 이동
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":r1:"]')))
            id_box = driver.find_element(By.XPATH, '//*[@id=":r1:"]')
            id_box.send_keys(Keys.ENTER)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/section/div[1]/div/form/button')))
            driver.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/div/form/button').click()
            driver.switch_to.window(driver.window_handles[-1])
            print("Confirm Done!")
            break
        elif keyboard.is_pressed('F10'):
            break

#//*[@id="root"]/main/section/section/div/div[2]/div/div/button[4] #트위터버튼
#//*[@id="allow"] #이전계정으로 로그인

if __name__ == '__main__':
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == "14:39:50":
            endhope=False
            while not endhope:
                tim=datetime.datetime.now()
                if tim.second>=59 and tim.microsecond>600000:
                    #미리 로그인해두고 buy now 가 중반쯤에 오도록 스크롤을 내려두도록 합시다
                    pyautogui.click(int(width * 90 / 100), int(height * 90 / 100))
                    #윈도우 팝업이 뜰때까지 계속 클릭합니다
                    while True:
                        windowTabs = len(driver.window_handles)
                        if windowTabs == 1:
                            RGB_CLICK(int(width * 10 / 100), int(height * 21 / 100), int(width * 90 / 100), int(height * 80 / 100), MAIN_RGB, 50, 1)
                            #print("클릭성공 시간 : ",tim)
                        else :
                            print("팝업떴다!")
                            print(len(driver.window_handles))
                            break
                    
                    """#지워도되는부분테스트용
                    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/button[2]')))
                    driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/button[2]').click()"""
                    
                    ####여기부터 BUY NOW 팝업 클릭 후 넣어주세요####
                    time.sleep(1)
                    try:
                        driver.switch_to.window(driver.window_handles[-1]) #크롬 팝업창으로 이동
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":r1:"]')))
                        id_box = driver.find_element(By.XPATH, '//*[@id=":r1:"]')
                        id_box.send_keys(Keys.ENTER)
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/section/div[1]/div/form/button')))
                        driver.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/div/form/button').click()
                        driver.switch_to.window(driver.window_handles[-1])
                        print("Confirm Done!")
                    except:
                        print("수동모드로 다시!")
                        pass
                    endhope=True
                    break
                else:
                    time.sleep(0.1)
                    print(tim)
            while True:
                main()

#화면이동을위한 buy버튼 클릭
#//*[@id="headlessui-tabs-tab-:r0:"] 
#//*[@id="headlessui-tabs-tab-:rf:"]

################################################################
#confirm 팝업띄우기
#//*[@id="__next"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/button[2]
#
#비번 클릭
#//*[@id=":r1:"]

#Confirm창
#//*[@id="root"]/main/section/div[1]/div/form/button
################################################################

##https://playone.marblex.io/ino/63dca20a2e19433d0e44ec1f/63edd3feb7b1b61da2d26360