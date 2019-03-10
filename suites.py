import unittest
from testcase import test_user_login

suite = unittest.TestSuite()
suite.addTest(test_user_login.TestUserLogin('test_user_login_normal'))



if __name__=='__main__':
    print(suite)
    unittest.TextTestRunner(verbosity=2).run(suite)