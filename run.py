import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from conf import config
from lib.case_log import case_log_info
all = unittest.defaultTestLoader.discover("./testcase")

if __name__ == '__main__':
    config.logging.info("测试开始"+"="*50)
    with open(config.report_file,"wb")as f:
        HTMLTestRunner(stream=f,title='User接口测试报告',description='测试报告').run(all)

    config.logging.info("测试结束"+"="*50)

