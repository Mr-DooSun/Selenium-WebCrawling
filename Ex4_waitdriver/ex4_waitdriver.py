import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

# chrome driver를 자동으로 설치함
chromedriver_autoinstaller.install() 

options = webdriver.ChromeOptions() # Browser 세팅하기
options.add_argument('lang=ko_KR') # 사용언어 한국어
options.add_argument('disable-gpu') # 하드웨어 가속 안함
# options.add_argument('headless') # 창 숨기기

# 브라우저 세팅
driver = webdriver.Chrome(options=options)

#######################################################################################################
# implicitly_wait

# 브라우저에 URL 호출하기
driver.get(url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8')

# 로딩 될때 까지 10초 대기 (로딩이 완료되면 즉시 다음 코드 실행)
driver.implicitly_wait(10)
# element 텍스트(현재 온도) 가져오기
temperature = driver.find_element_by_xpath('//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/strong').text
print(temperature)

#######################################################################################################
# WebDriverWait

# 브라우저에 URL 호출하기
driver.get(url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8')

# 해당 Element 로딩 될 때까지 10초 대기후 Element 텍스트 가져오기 (로딩이 완료되면 즉시 다음 코드 실행)
temperature = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/strong'))).text
print(temperature)

######################################################################################################

# 브라우저 탭 닫기
driver.close()
# 브라우저 종료하기 (탭 모두 종료)
driver.quit()