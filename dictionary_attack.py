# Mini Dictionary Attack on the password generated by the TOOL
import sys
from tqdm import tqdm
import threading

pass_to_break = str(sys.argv[1].encode("utf-8"))

cracked = False


def function(str1):
    if str1 == pass_to_break:
        print("\n\nPASSWORD CRACKED!!!\n\n")
        exit(0)

def function2():
    #print("FUNCTION2")
    with open("realhuman_phill.txt", 'r', encoding = "latin-1") as f:
        i = 0

        dicti = f.readlines()

    for i in tqdm(range(len(dicti))):
        function(str(dicti[i].strip().encode("utf-8")))

#threading.Thread(target = function2, args = ()).start()
function2()