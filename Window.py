from tensorflow.keras.models import load_model
import numpy as np
import tkinter as tk
import csv
import pandas as pd


model = load_model('diabetes_model.ann')


def button_trigger():

    textbox_1 = float(in1.get("1.0", 'end-1c').rstrip().lstrip())
    textbox_2 = float(in2.get("1.0", 'end-1c').rstrip().lstrip())
    textbox_3 = float(in3.get("1.0", 'end-1c').rstrip().lstrip())
    textbox_4 = float(in4.get("1.0", 'end-1c').rstrip().lstrip())
    textbox_5 = float(in5.get("1.0", 'end-1c').rstrip().lstrip())
    textbox_6 = float(in6.get("1.0", 'end-1c').rstrip().lstrip())
    textbox_7 = float(in7.get("1.0", 'end-1c').rstrip().lstrip())
    textbox_8 = float(in8.get("1.0", 'end-1c').rstrip().lstrip())
      # 開啟輸出的 CSV 檔案
    with open('input.csv', 'w', newline='') as csvfile:
      # 建立 CSV 檔寫入器
      writer = csv.writer(csvfile)

      # 寫入一列資料
      writer.writerow(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
                       'DiabetesPedigreeFunction', 'Age'])
      writer.writerow([textbox_1/17, textbox_2/199, textbox_3/122, textbox_4/99, textbox_5/846, textbox_6/67.1, (textbox_7-0.078)/2.342, textbox_8/60])
      # 記得清空
    predict = pd.read_csv("./input.csv")

    predict_x = model.predict(predict.iloc[[0]], verbose=1)

    classes_x = np.argmax(predict_x, axis=1)
    print(predict_x, classes_x)
    result_label_2["text"] = "根據您提供的數據，您確診糖尿病的機率為" + str(100 * predict_x[0, 1]) + "%"
    if predict_x[0, 1] <=0.4:
        result_label_3["text"] = "您暫時沒有確診糖尿病的風險！"
    elif 0.4 < predict_x[0, 1] <= 0.5:
        result_label_3["text"] = "此資料集可能無法給您精準的診斷！請就醫以獲得更專業的諮詢"
    else:
        result_label_3["text"] = "您可能罹患糖尿病！請盡速就醫進行深入檢查！"


# 建立視窗
win = tk.Tk()
win.title("糖尿病自主檢測系統")
win.geometry("640x720")
# 左邊的兩行文字
# '懷孕'、'葡萄糖'、'血壓'、'皮膚厚度'、'胰島素'、'BMI'、'糖尿病函數', '年齡'
in1_label = tk.Label(win, text="您育有幾胎", font=("Arial", 12))
in1_label.grid(row=0, column=0, padx=10, pady=20, sticky='w')
in2_label = tk.Label(win, text="血液中葡萄糖濃度為", font=("Arial", 12))
in2_label.grid(row=1, column=0, padx=10, pady=20, sticky='w')
in3_label = tk.Label(win, text="血壓為", font=("Arial", 12))
in3_label.grid(row=2, column=0, padx=10, pady=20, sticky='w')
in4_label = tk.Label(win, text="皮膚厚度為", font=("Arial", 12))
in4_label.grid(row=3, column=0, padx=10, pady=20, sticky='w')
in5_label = tk.Label(win, text="胰島素濃度為", font=("Arial", 12))
in5_label.grid(row=4, column=0, padx=10, pady=20, sticky='w')
in6_label = tk.Label(win, text="BMI為", font=("Arial", 12))
in6_label.grid(row=5, column=0, padx=10, pady=20, sticky='w')
in7_label = tk.Label(win, text="糖尿病函數為", font=("Arial", 12))
in7_label.grid(row=6, column=0, padx=10, pady=20, sticky='w')
in8_label = tk.Label(win, text="您的年齡是", font=("Arial", 12))
in8_label.grid(row=7, column=0, padx=10, pady=20, sticky='w')
# 右邊的對話框
in1 = tk.Text(win, width=20, height=2)
in1.grid(row=0, column=1)
in2 = tk.Text(win, width=20, height=2)
in2.grid(row=1, column=1)
in3 = tk.Text(win, width=20, height=2)
in3.grid(row=2, column=1)
in4 = tk.Text(win, width=20, height=2)
in4.grid(row=3, column=1)
in5 = tk.Text(win, width=20, height=2)
in5.grid(row=4, column=1)
in6 = tk.Text(win, width=20, height=2)
in6.grid(row=5, column=1)
in7 = tk.Text(win, width=20, height=2)
in7.grid(row=6, column=1)
in8 = tk.Text(win, width=20, height=2)
in8.grid(row=7, column=1)

# 按鈕及按鈕觸發行為
button = tk.Button(win, text="查看確診機率", font=('Arial', 12), width=60, height=3, command=button_trigger)
button.grid(row=9, column=0, columnspan=2, padx=10)
# 預留label供修改


result_label_1 = tk.Label(win, text="此資料集正確率為 76.6233742237091 %", font=("Arial", 12))
result_label_1.grid(row=10, column=0, padx=30, sticky='w', columnspan=2)
result_label_2 = tk.Label(win, text="", font=("Arial", 12))
result_label_2.grid(row=11, column=0, padx=30, sticky='w', columnspan=2)
result_label_3 = tk.Label(win, text="", font=("Arial", 12))
result_label_3.grid(row=12, column=0, padx=30, sticky='w', columnspan=2)


win.mainloop()
