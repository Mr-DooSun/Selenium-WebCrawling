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
driver.get(url='https://www.naver.com/')

# 이전에 복사한 xpath값을 아래 함수에 붙여넣기 해줍니다.
# driver.find_element_by_xpath(XPATH)
search_box = driver.find_element_by_xpath('//*[@id="query"]')
search_button = driver.find_element_by_xpath('//*[@id="search_btn"]')

search_word = '셀레니움'
search_box.send_keys(search_word)
search_button.click()

# 브라우저 탭 닫기
driver.close()
# 브라우저 종료하기 (탭 모두 종료)
driver.quit()