import chromedriver_autoinstaller
from selenium import webdriver

# chrome driver를 자동으로 설치함
chromedriver_autoinstaller.install() 

# 브라우저 세팅
driver = webdriver.Chrome()

# 브라우저에 URL 호출하기
driver.get(url='https://www.naver.com/')

# 브라우저 탭 닫기
driver.close()
# 브라우저 종료하기 (탭 모두 종료)
driver.quit()