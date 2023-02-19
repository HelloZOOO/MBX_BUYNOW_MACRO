# MBX_BUYNOW_MACRO

이 페이지에서 내일 오후 21시가 되면 Buy Now 버튼이 

5A57E9 + FFFFFF 
로 바뀔 거예요

buy now 버튼을 누르면 그 다음 buy now 팝업이 뜹니다

5A57E9 피그마에서
(90,87,233)

5b57f2 내화면에서
(91, 87, 242)

# 1페이즈

가로값 = 그대로
세로값 = -400(400) 에서 -800 범위까지 (2K기준)



# 민팅 매크로 개발 02

날짜: 2023년 2월 20일
내용: xpath로 클릭하기 해치웠나? 못해치웠다
다중 선택: Macro, Python

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
