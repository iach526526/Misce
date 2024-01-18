import program1
from program2 import P2
from  calculator import calculate
from decode import d
import subprocess

Secret="NjU1ICogMzI4ICsgKDMzMyAtICg4NjgpICsgKDEpIC8gKDU1NikpIC8gMzE4IC0gNTU1IC0gKDc5OSAvICg5NjUpKSAvIDE1MCAvIDk2ICogNTIyICogNDU4"
if __name__=="__main__":
    index=calculate(d(Secret))
    P2ret=P2()
    while True:
        try:
            alg=input('請輸入四則運算式:').replace('/','//')
            if P2ret[index]==calculate(alg):
                program1.main()
            else:
                print(calculate(alg))
        except:
            break
    # print(eval(x))