#数据库配置
db_host='115.28.108.130'
db_port=3306
db_user='test'
db_password='123456'
db='api_test'

#路径配置
import os
project_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_file = os.path.join(project_path,'data','data.xls')

log_file = os.path.join(project_path,'log','log.txt')

report_file = os.path.join(project_path,'report','report.html')


#日志配置
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="w")

#邮件配置
smtp_server = 'smtp.126.com'
smtp_user = 'liuyn120731@126.com'
smtp_password = 'liuyanan123'

receive=['694526779@qq.com','15910457235@163.com']
subject = '接口测试报告'
body='各位好，\n附件是接口测试报告，请查收'

is_send_report = True