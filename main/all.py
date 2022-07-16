import pytest
#我把它放在工作台里面就是为了和UI测试用例以及接口测试用例分离执行.
#通过nodeid指定用例执行，nodeid由模块，分隔符，类名，方法名，函数名组成.
# if __name__ == '__main__':
#     pytest.main(['-vs','../Interface_testcase/test_interface.py::test_04_jiekou2'])
#通过nodeid指定用例执行，nodeid由模块，分隔符，类名，方法名，函数名组成.
if __name__ == '__main__':
    pytest.main(['-vs','../Interface_testcase/test_interface.py::TestInterface::test_03_jiekou1'])