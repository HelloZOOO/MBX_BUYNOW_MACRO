# MBX_BUYNOW_MACRO

# 민팅 매크로 개발 01

```python
py -m pip install pyautogui

py -m pip install keyboard

py -m pip install openpyxl

py -m pip install selenium

py -m pip install webdriver_manager

py -m pip install clipboard

py -m pip install pillow

py -m pip install xlrd
#utf-8 변환
py -m pip install chardet

py -m pip install pandas

py -m pip install lxml

py -m pip install tk
```

<aside>
🔥 MBX 서버위치 확인

[Site report for https://playone.marblex.io](https://sitereport.netcraft.com/?url=https://playone.marblex.io)

</aside>

<aside>
🔥 서버접속방법 컴퓨터를의 시간을 AWS서버시간과 동기화시킵니다

[수강 신청 및 티케팅 성공을 위한 Tip 및 Python 프로그램](https://medium.com/@whj2013123218/수강-신청-및-티케팅-성공을-위한-tip-및-python-프로그램-facc9107abc7)

```python
관리자 권한으로 CMD를 실행했다면 아래와 같은 명령어를 입력한다.

net start w32time

w32tm /config /manualpeerlist:13.215.62.163 /syncfromflags:manual /update

w32tm /query /configuration

실행 결과 NTP Server에 13.215.62.163가 출력됐다면 컴퓨터가 AWS 서버 시간과 동기화되는 데 성공한 것이다.
```

컴퓨터의 시간은 AWS와 동기화 됨

그 후에 다음코드 작성하여 실행

```python
import datetime as dt
import pyautogui
import time

endhope=False
while not endhope:
    tim=dt.datetime.now()
    if tim.second>=59 and tim.microsecond>600000:
        pyautogui.click(1301,722)
        endhope=True
        print(tim)
    else:
        time.sleep(0.1)
        print(tim)
```

[[Python] 수강신청, 티케팅, 서버 신호, 가장 정확한 시간에 신호보내기](https://purplechip.tistory.com/11)

</aside>

<aside>
🔥 모니터 해상도에 상관없이 비율대로 클릭하기 위해 백분율 계산으로 클릭 범위

- 전체값에서 값 구하기 코드
    
    ```python
    ###############################################
    # 전체값에서 일부값은 몇 퍼센트? 계산
    # 공식은 "일부값 나누기 전체값 곱하기 100.0"
    ###############################################
    
    # 10은 100에서 몇 퍼센트?
    print "%.2f%%" % (10.0 / 100.0 * 100.0)
    # 출력 결과: 10.00%
    
    # 33은 100에서 몇 퍼센트?
    print "%.2f%%" % (33.0 / 100.0 * 100.0)
    # 출력 결과: 33.00%
    
    # 105는 300의 몇퍼센트?
    print "%.2f%%" % (105.0 / 300.0 * 100.0)
    # 출력 결과: 35.00%
    
    # 한달 봉급 156만원인 사람이, 음식 값으로 21만원을 쓰면,
    # 그 음식값은 한 달 봉급의 몇 퍼센트?
    print "%.2f%%" % (210000.0 / 1560000.0 * 100.0)
    # 출력 결과: 13.46%
    
    # 만약 봉급 156만원으로 모두 먹는 데 사용했다면
    # 100% 가 나와야겠지요.
    print "%.2f%%" % (1560000.0 / 1560000.0 * 100.0)
    # 출력 결과: 100.00%
    
    # 만약 아무것도 먹지 않았면 0% 가 나와야합니다.
    print "%.2f%%" % (0.0 / 1560000.0 * 100.0)
    # 출력 결과: 0.00%
    
    ###############################################
    # 전체값의 몇 퍼센트는 얼마? 계산
    # 공식은, "전체값 곱하기 퍼센트 나누기 100.0"
    ###############################################
    
    # 100의 10퍼센트는 얼마?
    print "%.2f" % (100.0 * 10.0 / 100.0)
    # 출력 결과: 10.00
    
    # 100의 33퍼센트는 얼마?
    print "%.2f" % (100.0 * 33.0 / 100.0)
    # 출력 결과: 33.00
    
    # 300의 35퍼센트는 얼마?
    print "%.2f" % (300.0 * 35.0 / 100.0)
    # 출력 결과: 105.00
    
    # 156만원의 13.46퍼센트는 얼마?
    print "%.2f" % (1560000.0 * 13.46 / 100.0)
    # 출력 결과 (21만원에 가까운 값): 209976.00
    
    # 156만원의 100퍼센트는 얼마?
    print "%.2f" % (1560000.0 * 100.0 / 100.0)
    # 출력 결과: 1560000.00
    
    # 156만원의 0퍼센트는 얼마?
    print "%.2f" % (1560000.0 * 0.0 / 100.0)
    # 출력 결과: 0.00
    
    ```
    

```python
RGB_CLICK(int(width * 20 / 100), int(height * 21 / 100), int(width * 80 / 100), int(height * 50 / 100), 3)
```

</aside>

<aside>
🔥 우측하단에서 좌측상단 ↖️ 으로 이동하는 클릭구현

```python
def RGB_CLICK(x1, y1, x2, y2, N): #RGB인식 영역 / 프로그램이 몇초뒤에 꺼질까요?
    start_time = time.time()
    end_time = start_time + N

    shot = 0 #목표물 찾았는지 확인하는 변수
    c_start = (x1,y1) #캡처영역 좌측상단 포인트
    c_end = (x2,y2) #캡처영역 우측하단 포인트
    c_xbox = (91, 87, 242) #RGB값
    
    while start_time < end_time:
        screenshot = ImageGrab.grab()
        for i in range(c_end[0],c_start[0],-10):
            for j in range(c_end[1],c_start[1],-10):
                RGB = screenshot.getpixel((i,j)) #각 좌표에서 RGB값 추출
                if abs(RGB[0]-c_xbox[0]) + abs(RGB[1]-c_xbox[1]) + abs(RGB[2]-c_xbox[2]) < 100:
                    pyautogui.click((i - 10,j - 10))
                    shot = 1
                    break
                elif shot == 1:
                    break
            if shot == 1:
                break
        break
```

N초뒤에 프로그램이 종료되는 코드를 추가하려면 아래코드를 추가해준다

```python
while start_time < end_time:
            screenshot = ImageGrab.grab()
            for i in range(c_end[0],c_start[0],-10):
                for j in range(c_end[1],c_start[1],-10):
                    RGB = screenshot.getpixel((i,j)) #각 좌표에서 RGB값 추출
                    if abs(RGB[0]-c_xbox[0]) + abs(RGB[1]-c_xbox[1]) + abs(RGB[2]-c_xbox[2]) < 100:
                        pyautogui.click((i - 10,j - 10))
                        shot = 1
                        break
                if shot == 1:
                    shot = 0
                    break
            **if time.time() > end_time:                                                                                                                                 
                break**
```

</aside>

# 민팅 매크로 개발 02

# HTML에서 바로 xpath 뽑을걸… able하니까 클릭가능하게 바뀌네…
<img width="80%" src="https://user-images.githubusercontent.com/42949995/219965106-b8da6208-7623-4562-8e28-ff5fe80b50a7.png"/> 

//*[@id="headlessui-tabs-panel-:r1a:"]/div/div[1]/ul/li/div[2]/div/button

//*[@id="headlessui-tabs-panel-:r1a:"]/div/div[1]/ul/li/div[2]/div/button

# 얏됐다! 로그인게정마다 xpath가 조금씩 변해서 로그인하고나면 클릭이 안돼!!!!

```python
#//*[@id="headlessui-tabs-panel-:r3:"]/div/div[1]/ul/li/div[2]/div/button #(로그인안했을땐 동일)
#//*[@id="headlessui-tabs-panel-:**ro**:"]/div/div[1]/ul/li/div[2]/div/button #(A계정 로그인)
#//*[@id="headlessui-tabs-panel-:**ri**:"]/div/div[1]/ul/li/div[2]/div/button #(B계정 로그인)
```

## 크히힣!!! 난 잠 다잤다!!!

- 눈물의 해치웠나? 똥꼬쇼 기존코드
    
    ```python
    if __name__ == '__main__':
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time == "00:41:50":
                endhope=False
                while not endhope:
                    tim=datetime.datetime.now()
                    if tim.second>=59 and tim.microsecond>600000:
                        
                        ####웹사이트 BUY NOW 클릭 시도####
                        count = 0
                        while True:
                            try:
    														#xpath가 바뀐다....!!!!
                                **element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headlessui-tabs-panel-:r3:"]/div/div[1]/ul/li/div[2]/div/button')))
                                driver.find_element(By.XPATH, '//*[@id="headlessui-tabs-panel-:r3:"]/div/div[1]/ul/li/div[2]/div/button').click()
                                print("클릭성공 시간 : ",tim)
                                break**
                            except:
                                count += 1
                                print("시도실패",count)
                        ####팝업 BUY NOW 클릭 시도####
                        for i in range(10):
                            keyboard.press_and_release('down')
                        pyautogui.click(int(width * 20 / 100), int(height * 20 / 100))
                        RGB_CLICK(int(width * 10 / 100), int(height * 20 / 100), int(width * 90 / 100), int(height * 80 / 100), MAIN_RGB, 50, 3)
                        RGB_CLICK(int(width * 10 / 100), int(height * 20 / 100), int(width * 90 / 100), int(height * 80 / 100), MAIN_RGB, 50, 3)
                        ####Confrim 팝업 클릭(테스트부분 지워도 됩니다)####
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/button[2]')))
                        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/button[2]').click()
                        driver.switch_to.window(driver.window_handles[-1])
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":r1:"]')))
                        driver.find_element(By.XPATH, '//*[@id=":r1:"]').click()
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/section/div[1]/div/form/button')))
                        driver.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/div/form/button').click()
                        driver.switch_to.window(driver.window_handles[-1])
                        #확인차 다시 클릭하는부분
                        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headlessui-tabs-panel-:r3:"]/div/div[1]/ul/li/div[2]/div/button')))
                        driver.find_element(By.XPATH, '//*[@id="headlessui-tabs-panel-:r3:"]/div/div[1]/ul/li/div[2]/div/button').click()
                        endhope=True
                        break
                    else:
                        time.sleep(0.1)
                        print(tim)
    ```
    

> Xpath클릭도 실패했고… datetime 이나 time.sleep 으로는 고정 시간기준으로 클릭만 가능하여
Xpath가 아니라면 팝업을 인지하고 다음 단계로 이동하는걸 구현하지 못했었는데..
> 

## 해치웠다!!!(진짜로)

> Xpath 사용 없이 해결한 방법은 바로

**`”len(driver.window_handles)”`**

pyautogui 와 PIL 라이브러리를 활용해 만든 RGB_CLICK함수를 일단 한번 클릭하면 함수를 종료하게 만들고 while 문을 활용해 크롬탭이 하나뿐이라면 계속해서 RGB_CLICK을 하게 만들었다
> 
> 
> ```python
> while True:
> 		**windowTabs = len(driver.window_handles)**
> 		if windowTabs == 1:
> 		    RGB_CLICK(int(width * 10 / 100), int(height * 21 / 100), int(width * 90 / 100), int(height * 80 / 100), MAIN_RGB, 50, 1)
> 		    #print("클릭성공 시간 : ",tim)
> 		else :
> 		    print("팝업떴다!")
> 		    print(len(driver.window_handles))
> 		    break
> ```
> 
> 그리고 클릭을 계속 하다가 BUY NOW를 착실히 전부 잘 클릭해서 팝업이 뜬다면, 팝업창 자체는 새로운 탭으로 열리기때문에 **`len(driver.window_handles) == 2`** 코드를 탈출하며 다음과 같은 코드가 실행됩니다
> 
> ```python
> time.sleep(1)
> **driver.switch_to.window(driver.window_handles[-1]) #크롬 팝업창으로 이동**
> element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":r1:"]')))
> id_box = driver.find_element(By.XPATH, '//*[@id=":r1:"]')
> id_box.send_keys(Keys.ENTER)
> element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/main/section/div[1]/div/form/button')))
> driver.find_element(By.XPATH, '//*[@id="root"]/main/section/div[1]/div/form/button').click()
> driver.switch_to.window(driver.window_handles[-1])
> print("Confirm Done!")
> endhope=True
> break
> ```
> 
> 해당 부분은 단순하게 새로운 탭에서 로딩이 끝나면 바로 confirm을 하도록 만들었다
> 
> 앞에 time.sleep(1) 을 해준 이유는 팝업이 뜨는 시간을 기다려줘야 윈도우 스위치가 제대로 작동합니다
> 

쨌든 오늘 꿀잠…다행이다…
