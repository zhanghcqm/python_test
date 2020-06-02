
import random,string
s=string.digits + string.ascii_letters
v=random.sample(s,4)
str_data=''.join(v)
print("随机4位验证码是%s" % str_data)



from time import strftime, localtime
import datetime,time
# 打印当前时间

def gen_now_time():
    """
    获取当前时间，精确到天
    :return:
    """
    now_time = strftime("%Y-%m-%d", localtime())
    return now_time

def get_report_time():
    """
    获取报表查询起始时间（当天）
    :return:
    """
    today = datetime.date.today()
    t = today.strftime('%Y/%m/%d')
    return t



def teardown_hook_sleep_N_secs(response, n_secs):
    """
    请求完毕，沉睡时间
    :param response:
    :param n_secs:
    :return:
    """
    if response.status_code == 200:
        time.sleep(3)
    else:

        time.sleep(n_secs)


def time_stamp():
    """
    后获取当前13位时间戳(毫秒)
    :return:
    """
    t=time.time()
    time_stamp=int(round(t*1000))
    return time_stamp

print(time_stamp())