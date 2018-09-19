'''https://www.cnblogs.com/yoyoketang/p/7259993.html'''
# -*- coding: utf-8 -*-

import os
import unittest
import time
import HTMLTestRunner
#当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
print('cur_path: '+cur_path)

def add_case(caseName = 'case', rule = 'test*.py'):
        '''第一步：加载所有测试用例'''
        case_path = os.path.join(cur_path,caseName) #用例文件夹
        #如果不存在case文件夹，就自动创建一个
        #if not os.path.exists(case_path):os.mkdir(case_path)
        print('test case path: %s'%case_path)
        #定义discover方法的参数
        discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
        print(discover)
        return discover

def run_case(all_case, reportName = 'report'):
        '''第二步：执行所有的用例，并把结果写入HTML测试报告'''
        now = time.strftime ('%Y_%M_%D_%H_%M_%S')
        report_path = os.path.join(cur_path,reportName)#用例文件夹
        print('report path : %s' % report_path)
        # 如果不存在report文件夹，就自动创建一个
        #if not os.path.exists(report_path):os.mkdir(report_path)
        report_abspath = os.path.join(report_path,now + "result.html")
        print('report abspath : %s'% report_abspath)

        runner = unittest.TextTestRunner()  # run跑用例
        runner.run(all_case)
        # fp = open('my_report.html', 'wb')
        # runner = HTMLTestRunner.HTMLTestRunner(
        #     stream=fp, title=u'自动化测试报告', description=u'用例执行情况')
        # '''stream:测试报告写入文件的存储区域'''

        # runner.run(all_case)
        # fp.close()



'''
def get_report_file(report_path):
        第三步：获取最新的测试报告
        lists = os.listdir(report_path)
        lists.sort(key=lambda  fn:os.path.getmtime((os.path.join(report_path))))
        print(u'最新测试生成报告： ' + lists[-1])
        #找到最新生产的报告文件
        report_file = os.path.join(report_path, lists[-1])
        return report_file


    def send_mail(sender, psw, receiver, smtp_server, report_file, port):
        pass
    
        #邮箱配置
        from config import readConfig
        sender = readConfig.sender
        psw =readConfig.psw
        smtp_server = readConfig.smtp_server
        port = readConfig.port
        receiver = readConfig.receiver
        send_mail(sender,psw, receiver,smtp_server,report_file,port)
    '''

if __name__ == "__main__":
        all_case = add_case()#1 加载用例
        #生成测试报告的路径
        run_case(all_case) #2 执行用例
        #获取最新的测试报告文件
        #report_path = os.path.join(cur_path % 'report') #用例文件夹
        report_path = os.path.join(cur_path, 'report')
        #print('report path:'+ report_path)
        print('report path : %s' % report_path)
        #report_file = get_report_file(report_path)#3 获取最新的测试报告


