from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置浏览器驱动路径（假设使用ChromeDriver）
driver_path = '/Users/heqifeng/bin/chromedriver'

# 初始化WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # 打开目标网页
    driver.get('http://example.com')  # 替换为你的目标URL

    # 等待页面加载并找到搜索框（假设页面上有一个输入框）
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q'))  # 替换'By.NAME, 'q'为实际的搜索框定位方式
    )

    # 输入关键字并提交搜索
    search_box.send_keys('你的关键字')  # 替换为你的实际关键字
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载并找到关键字对应的链接
    search_result_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '关键字'))  # 替换为你的实际关键字
    )

    # 点击链接
    search_result_link.click()

    # 等待新页面加载并找到磁力链接
    time.sleep(5)  # 等待页面加载（根据实际情况调整时间）
    page_source = driver.page_source

    # 查找包含“Magnet连接:”的行
    if "Magnet连接:" in page_source:
        start_index = page_source.find("Magnet连接:")
        end_index = page_source.find(' ', start_index)
        magnet_link = page_source[start_index:end_index]

        # 查找链接的标题
        title = driver.title

        # 打印标题和磁力链接
        print(f"Title: {title}")
        print(f"Magnet Link: {magnet_link}")
    else:
        print("找不到 Magnet连接:")

finally:
    # 关闭浏览器
    driver.quit()
