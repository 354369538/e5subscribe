import time

def focus_timer():
    try:
        minutes = int(input("请输入需要专注的分钟数："))
        seconds = minutes * 60
        print(f"专注计时器已开始，将持续 {minutes} 分钟。")
        while seconds > 0:
            print(f"倒计时: {seconds} 秒")
            time.sleep(1)
            seconds -= 1
        print("专注时间结束！")
    except KeyboardInterrupt:
        print("计时被终止。")

focus_timer()
