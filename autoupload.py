import uiautomator2 as u2
import time
d = u2.connect_wifi('192.168.1.5')


def openApp() :

    d.session("com.ss.android.ugc.aweme")  # 等待应用前台运行
    d.app_wait("com.ss.android.ugc.aweme", True)

    loginAccount()



    return

def loginAccount():
    if d(text="我知道了").exists(timeout=2):
        d(text="我知道了").click()
    time.sleep(1)
    if d(text="权限请求").exists():
        d(resourceId="com.android.packageinstaller:id/do_not_ask_checkbox").click()
        d(text="始终允许").click()
    time.sleep(1)
    # 请求定位
    if d(text="权限请求").exists():
        d(resourceId="com.android.packageinstaller:id/do_not_ask_checkbox").click()
        d(text="始终允许").click()
    time.sleep(1)
    # 视频上滑
    if d(text="滑动查看更多").exists():
        d(scrollable=True).scroll.vert.forward(steps=100)
    time.sleep(1)
    # 点击我的进行登录判断


    # 其它手机号码登录

    # 密码登陆


    return

def uploadVideo():
    print("点击拍照：")
    d(resourceId='com.ss.android.ugc.aweme:id/deg').click()
    print("点击相册：")
    d(resourceId='com.ss.android.ugc.aweme:id/qs').click()
    print("选择视频：")

    print()
    print("end")
    return

if __name__ == '__main__':
    print(d.app_info("com.ss.android.ugc.aweme"))
    openApp()

