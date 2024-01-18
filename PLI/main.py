# pls use CMD:"py main.py"
from program2 import P2
from  calculator import calculate
from decode import d
import subprocess
import os
# 獲取當前腳本的目錄
script_directory = os.path.dirname(os.path.realpath(__file__))
# 更改根目錄為當前這層目錄
os.chdir(script_directory)

Secret=["NjU1ICogMzI4ICsgKDMzMyAtICg4NjgpICsgKDEpIC8gKDU1NikpIC8gMzE4IC0gNTU1IC0gKDc5OSAvICg5NjUpKSAvIDE1MCAvIDk2ICogNTIyICogNDU4",'VGFpd2FuU29jaWFsQ3JlZGl0VVAh']
if __name__=="__main__":
    print("你好!歡迎打開計算小精靈365，看起來你需要一點整數四則運算，建議你使用CMD執行main.py效果更好!\n")
    index=calculate(d(Secret[0]))
    P2ret=P2()
    script_path = "dist/program1.exe"
    script_argument=d(Secret[1])
    while True:
        try:
            alg=input('請輸入四則運算式:').replace('/','//')#確保沒有小數點運算
            print(calculate(alg))
            script_argument2=str(calculate(alg))
            subprocess.run([script_path,script_argument,script_argument2])
        except:
            break



# auth:Each^_~