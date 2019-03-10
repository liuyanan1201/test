import unittest
import requests
from lib.read_excel import get_sheet,get_case
import json
from conf import config
from lib.case_log import case_log_info

class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = get_sheet(config.data_file,"登录")

    def test_user_login_normal(self):
        case_data = get_case(self.sheet,"test_user_login_normal")
        url = case_data[2]
        data = json.loads(case_data[3])
        excpted_res = case_data[4]
        res = requests.post(url=url,data=data)
        case_log_info('test_user_login_normal',url,case_data[3],case_data[4],res.text)

        self.assertEqual(excpted_res,res.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)