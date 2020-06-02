import ddt
import unittest
from selenium import webdriver

users =[{'username':'root','userpw':'123'},{'username':'roo1t','userpw':'123f'}]
@ddt.ddt
class LoginCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Url = "http://localhost:88/CookiesDemo/login.jsp"
    @ddt.data(*users)
    def testa(self,u):
        """正确用户和密码登录用例"""
        self.driver.get(self.Url)
        login(self.fox,u['username'],u['userpw'])
        self.assertEqual(self.driver.title,u"登录","正确用户名和密码登录不成功")

    @ddt.data((2,3),(3,1))
    @ddt.unpack
    def testb(self,a,b):
        print(a,b)

    def tearDown(self):
        self.fox.quit()

if __name__ == '__main__':
    unittest.main()

