import uiautomator2 as u2
import time
d = u2.connect_wifi('192.168.2.5')


def openApp() :
    with d.session("com.ss.android.ugc.aweme") as sess:
        loginAccount()
    return

def loginAccount():
    if d(text="我知道了").exists(timeout=2):
        d(text="我知道了").click()
    if d(text="权限请求").exists(timeout=1):
        d(resourceId="com.android.packageinstaller:id/do_not_ask_checkbox").click()
        d(text="始终允许").click()
    if d(text="发现通讯录好友", resourceId="com.ss.android.ugc.aweme:id/title").exists(timeout=1):
        d(text="取消", resourceId="com.ss.android.ugc.aweme:id/rk").click()
    # 请求定位
    if d(text="权限请求").exists(timeout=1):
        d(resourceId="com.android.packageinstaller:id/do_not_ask_checkbox").click()
        d(text="始终允许").click()
    # 视频上滑
    if d(text="滑动查看更多").exists():
        d(scrollable=True).scroll.vert.forward(steps=100)
    time.sleep(1)
    d(resourceId='com.ss.android.ugc.aweme:id/deg').click()
    time.sleep(1)
    # 未登录
    if d(resourceId="com.ss.android.ugc.aweme:id/c6t").exists(timeout=1):
        d(resourceId="com.ss.android.ugc.aweme:id/cid").click()
        d(resourceId="com.ss.android.ugc.aweme:id/c6t").click()
        time.sleep(0.5)
        if d(resourceId="com.ss.android.ugc.aweme:id/c91").exists():
            d(resourceId="com.ss.android.ugc.aweme:id/c91").click()
            d(resourceId="com.ss.android.ugc.aweme:id/ac2").set_text("12")
            d(resourceId="com.ss.android.ugc.aweme:id/ac1").set_text("34")
            d(resourceId="com.ss.android.ugc.aweme:id/ci2").click()
            d(resourceId="com.ss.android.ugc.aweme:id/pr").click()
            time.sleep(0.5)
            # 获取验证码
            # 如果出现输入验证码页面就比较尴尬
            if d(resouceId="com.ss.android.ugc.aweme:id/d81").exists():
                d(resouceId="com.ss.android.ugc.aweme:id/d81").click();
                # 输入验证码
                d(resouceId="com.ss.android.ugc.aweme:id/ach").set_text(2312);

    else:
        uploadVideo();
    return

def uploadVideo():
    # 判断权限
    if d(text="权限请求").exists(timeout=0.2):
        d(text="禁止后不再询问", resourceId="com.android.packageinstaller:id/do_not_ask_checkbox").click()
        d(text="始终允许").click()

    if d(text="权限请求").exists(timeout=0.2):
        d(text="禁止后不再询问", resourceId="com.android.packageinstaller:id/do_not_ask_checkbox").click()
        d(text="始终允许").click()
    # 存储
    if d(text="权限请求").exists(timeout=0.2):
        d(text="禁止后不再询问", resourceId="com.android.packageinstaller:id/do_not_ask_checkbox").click()
        d(text="始终允许").click()

    for i in range(1, 20):
        try:
            print("点击相册：")
            d(resourceId='com.ss.android.ugc.aweme:id/qs').click()
            print("选择视频：")
            d(resourceId="com.ss.android.ugc.aweme:id/bwb").click()
            time.sleep(8)
            # 截取视频
            d(text="下一步",resourceId="com.ss.android.ugc.aweme:id/dtj").click()
            time.sleep(0.5)
            # 修饰视视频
            d(text="下一步",resourceId="com.ss.android.ugc.aweme:id/c23").click()
            time.sleep(0.5)
            print("点击发布")
            # 视频不保存在本地
            atrs = d(resourceId="com.ss.android.ugc.aweme:id/ua").info
            if atrs['checked']:
                d(resourceId="com.ss.android.ugc.aweme:id/ua").click();
            d(description="发布", resourceId="com.ss.android.ugc.aweme:id/ckq").click()
            time.sleep(1)
            # 关闭同步弹窗
            if d(text="同步到今日头条", resourceId="com.ss.android.ugc.aweme:id/cl0").exists(timeout=3):
                ## d(resourceId='com.ss.android.ugc.aweme:id/cl0', text="同步到今日头条").click()
                d(resourceId='com.ss.android.ugc.aweme:id/ckw').click()
            print("发布第" + str(i) + "视频")
            time.sleep(10)
            d(resourceId='com.ss.android.ugc.aweme:id/deg').click()
        except Exception:
            print("发布异常")
    return

if __name__ == '__main__':
    print(d.app_info("com.ss.android.ugc.aweme"))
    openApp()

