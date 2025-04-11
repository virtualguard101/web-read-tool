#!/usr/bin/env python3

import pyautogui
import time
import logging

def get_runtime():
    '''获取运行时长'''
    run_time = int(input("How long do you want the script work:"))
    start_time = time.time()
    return [run_time, start_time]


def main(start_time, run_time):
    '''功能主体'''
    # 预留网页开启时间
    print("You have 10s to open the lesson website\n")
    time.sleep(10)
    # time.sleep(3)

    # 更新运行时间
    while (time.time() - start_time < run_time):
        time.sleep(5)

        pyautogui.scroll(-2)
        time.sleep(5)
        pyautogui.scroll(1)

    pyautogui.scroll(500)

def runtime_record():
    '''记录运行时间'''
    logging.basicConfig(
        filename = 'runtime.log',
        level = logging.INFO,
        format = '%(asctime)s - %(levelname)s - %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S'
    )

    # 获取运行时长与时间戳
    runtime_res = get_runtime()
    work_time, work_end = runtime_res[0], runtime_res[1]
 
    start_time = time.time()
    logging.info("Start working")

    # 运行功能主体
    main(work_end, work_time)

    end_time = time.time()
    logging.info("End of this time")

    runtime = end_time - start_time
    logging.info(f"Runtime of this time: {(runtime-10)/60:.2f} min")


if __name__ == "__main__":
    runtime_record()
