'''
观察者模式

外部与一个子系统的通信必须通过一个统一的外观对象进行，为子系统中的一组接口提供一个一致的界面，
外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
外观模式又称为门面模式，它是一种对象结构型模式。


外观模式包含如下角色： Facade: 外观角色 SubSystem:子系统角色
假设有一组火警报警系统，由三个子元件构成：一个警报器，一个喷水器，一个自动拨打电话的装置。
'''

#当火警发生时，先警报器响起警报，喷水器开始喷水，最后开始拨打火警电话
class AlarmSensor(object):
    def run(self):
        print("Alarm Ring...")


class WaterSprinker(object):
    def run(self):
        print("Spray Water...") 


class EmergencyDialer(object):
    def run(self):
        print("Dial 119...")


class EmergencyFacade(object):
    """
    外观类中封装了对子系统的操作
    """
    def __init__(self):
        self.alarm_sensor=AlarmSensor()
        self.water_sprinker=WaterSprinker()
        self.emergency_dialer=EmergencyDialer()
        
    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()



#业务代码 (第一种虽然也完成了业务需求，但是明显的是客户的负担较重，客户端与子系统的耦合度太大。)
if __name__=="__main__":
    print("#######1")
    alarm_sensor=AlarmSensor()
    water_sprinker=WaterSprinker()  
    emergency_dialer=EmergencyDialer()
    alarm_sensor.run()
    water_sprinker.run()
    emergency_dialer.run()
    print("#######2")
    emergency = EmergencyFacade()
    emergency.runAll()