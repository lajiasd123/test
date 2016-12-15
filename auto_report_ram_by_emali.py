# -*- coding:UTF-8 -*-
import smtplib,psutil,time

#TODO 定时任务模块
while True:
    time.sleep(1800) #半个小时发送一次
    # TODO 内存获取模块
    listpid = psutil.pids()
    totalnum = 0
    totalmemery = 0
    for n in listpid:
        process_name = psutil.Process(n).name()
        process_pencent = psutil.Process(n).memory_percent()
        totalnum += 1
        totalmemery += psutil.Process(n).memory_percent()

    # TODO 邮件发送模块
    from email.mime.text import MIMEText

    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = 'xxx'
    # 密码
    mail_pass = 'xxxx'
    # 邮件发送方邮箱地址
    sender = 'xxx@163.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['xxx@xx.com']

    # 设置email信息
    # 邮件内容设置
    message = MIMEText(str(totalmemery), 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = '服务器内存使用率'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误



