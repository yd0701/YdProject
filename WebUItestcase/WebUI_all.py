import pytest
#-vs表示显示类，方法，打印值，通过还是失败
#使用WebUI_all执行，可以执行文件夹以内的所有用例，也可以选择性执行.
if __name__ == '__main__':
    pytest.main(['-vs'])
# if __name__ == '__main__':
#     pytest.main(['-vs','test_login.py'])
# if __name__ == '__main__':
#     pytest.main(['-vs','test_login.py','test_product.py'])