import chromedriver_autoinstaller
from selenium import webdriver

# chrome driver를 자동으로 설치함
chromedriver_autoinstaller.install() 

options = webdriver.ChromeOptions() # Browser 세팅하기
options.add_argument('lang=ko_KR') # 사용언어 한국어
options.add_argument('disable-gpu') # 하드웨어 가속 안함
# options.add_argument('headless') # 창 숨기기

# 브라우저 세팅
driver = webdriver.Chrome(options=options)

# 브라우저에 URL 호출하기
driver.get(url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8')

# 브라우저 탭 닫기
driver.close()
# 브라우저 종료하기 (탭 모두 종료)
driver.quit()