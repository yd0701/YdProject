#公共操作：浏览器相关，但与软件业务无关
#打开指定浏览器的指定地址，设置隐式等待10秒
def openBrowser(url="",browser=""):
    from selenium import webdriver
    if browser=="firefox":
        driver = webdriver.Firefox()
    elif browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="ie":
        driver = webdriver.Ie()
    elif browser=="edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver
#界面截图，放在runningResult/img文件夹中，以当前系统时间命名
def getPhoto(driver):
    import time
    systime = time.strftime("%Y%m%d%H%M%S")
    driver.get_screenshot_as_file("..\\testReport\\img\\" + systime + ".png")

#定位下拉框，实例化Select
def selectOption(driver,id):
    from selenium.webdriver.support.select import Select
    s=Select(driver.find_element_by_id(id))
    return s