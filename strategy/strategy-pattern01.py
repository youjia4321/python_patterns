'''
现通知客户取快递的方式有两种：电话通知，邮件通知  _type
应如何设计该系统的客户通知部分
'''
class MsgSender(object):
    _type = ''  # 发送信息的方式，用来保存电话号码和邮箱地址
    info = ''  # 保存给客户发送的信息
 
    def send(self):
        pass
 
 
class PhoneSender(MsgSender):
    def send(self):
        print('给{}打电话说：{}'.format(self._type, self.info))
 
 
class Emailsender(MsgSender):
    def send(self):
        print('给{}发送邮件的内容：{}'.format(self._type, self.info))
 
 
class Customer(object):
    name = '' 
    phone = ''
    email = ''
    send_way = None
 
    # 设置发送方式
    def set_send_way(self, send_way):
        self.send_way = send_way
 
    # 发送内容
    def send_msg(self):
        self.send_way.send()
 
 
if __name__ == '__main__':
    customer = Customer()
    customer.name = 'dck'
    customer.phone = '13982199112'
    customer.email = 'youjia4321@qq.com'

    # 1.打电话告诉
    phone_sender = PhoneSender()
    phone_sender.info = '快来啊，您的快递到了，速来...'
    phone_sender._type = customer.phone
    customer.set_send_way(phone_sender)
    customer.send_msg()  

    # 2.发电子邮件：
    email_sender = Emailsender()
    email_sender._type = customer.email
    email_sender.info = '快来啊，您的快递到了，速来...'
    customer.set_send_way(email_sender)
    customer.send_msg() 