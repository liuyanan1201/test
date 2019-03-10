import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from conf import config
from lib.send_email import send_report

all = unittest.defaultTestLoader.discover("./testcase")

if __name__ == '__main__':
    config.logging.info("测试开始"+"="*50)
    with open(config.report_file,"wb")as f:
        HTMLTestRunner(stream=f,title='User接口测试报告',description='测试报告').run(all)
    if config.is_send_report:
        send_report()
        config.logging.info("发送邮件成功")
    config.logging.info("测试结束"+"="*50)

