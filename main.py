import PySimpleGUI as sg
import time

# GUI elements list
clock = sg.Text("", key="CLOCK")
label_text = sg.Text("Select unit to convert.", key="LABEL")
converts = sg.Spin(["Length", "Weight", "Area"], enable_events=True, key="CONVERTS", size=10)
result_label1 = sg.Text("Meter", key="RESULT_LABEL1")
result1 = sg.Input(tooltip="Enter a number to convert", enable_events=True, key="RESULT1")
col1 = [[result_label1], [result1]]
result_label2 = sg.Text("feet", key="RESULT_LABEL2")
result2 = sg.Input(tooltip="Enter a number to convert", enable_events=True, key="RESULT2")
col2 = [[result_label2], [result2]]
exit_button = sg.Button("Exit", key="EXIT")
clear_button = sg.Button("Clear", key="CLEAR")
layout = [
    [clock],
    [label_text, converts],
    [sg.Column(col1), sg.Column(col2)],
    [exit_button, clear_button]
]

window = sg.Window("Universal Unit converter", layout=layout, font=("Helvetica", 15))

while True:
    event, value = window.read(timeout=200)
    clock = time.strftime("%b %d, %Y %H:%M:%S")
    window["CLOCK"].update(clock)

    match event:
        case "CONVERTS":
            print(value)
            print(value["CONVERTS"])
            if value["CONVERTS"] == "Length":
                window["RESULT_LABEL1"].update("Meter")
                window["RESULT_LABEL2"].update("Feet")
            elif value["CONVERTS"] == "Weight":
                window["RESULT_LABEL1"].update("Kg")
                window["RESULT_LABEL2"].update("Lb")
            elif value["CONVERTS"] == "Area":
                window["RESULT_LABEL1"].update("Square meter")
                window["RESULT_LABEL2"].update("Square feet")
        case "CLEAR":
            window["RESULT"].update("")
        case sg.WIN_CLOSED:
            break
        case "EXIT":
            break
