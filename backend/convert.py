from PyQt5 import uic

def convert_uic(txt):
    with open(txt, "w",encoding="utf-8")as fout:
        uic.compileUi(txt,fout)


        


