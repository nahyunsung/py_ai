#숫자 판독하기 앱

import tkinter as tk
import tkinter.filedialog as fd

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        print("파일경로: ", fpath)

#앱 창 만들기
root = tk.Tk()
root.geometry("400x400")

#버튼, 레이블 생성하기
btn = tk.Button(root, text="파일 열기", command = openFile)
imageLabel = tk.Label()

#버튼ㅡ 레이블 화면에 출력하기
btn.pack()
imageLabel.pack()

tk.mainloop()