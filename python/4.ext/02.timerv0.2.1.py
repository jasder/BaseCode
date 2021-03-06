#!/usr/bin/env python3

import os
import time
from multiprocessing.dummy import Pool


def move_screen():
    """旋转屏幕来提示"""
    os.system("xrandr -o left")  # 左旋转90度
    time.sleep(2)
    os.system("xrandr -o normal")  # 恢复正常


# 大概多少秒（n的整数倍较好）
# def reset(n)
global_how_time = 240
global_time = 0  # 开始播放时间


def play_music():
    """播放音乐来提醒"""
    global global_time, global_how_time
    # os.system("mpv ~/音乐/莫问明天.mp3")
    if global_time > global_how_time:
        global_time = 0  # 防止超出时间
    os.system(f"mpv ~/音乐/莫问明天.mp3 --start={global_time}")


def reset(n=1):
    """友情提醒"""
    os.system("xrandr -o normal")  # 恢复正常
    time.sleep(n)
    global global_time
    global_time += n  # 继续播放
    os.system("pkill mpv")  # 关闭音乐
    print("等待下一次拥抱...")


if __name__ == "__main__":
    pool = Pool()
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(1200)  # 20 分钟
        os.system("notify-send 逆天友情提醒 20分钟过去了")
        pool.apply_async(play_music)
        pool.apply_async(move_screen)
        reset(30)  # 休息30s
