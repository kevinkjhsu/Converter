import PySimpleGUI as sg
import time
import convert as ct

# GUI elements list
clock = sg.Text("", key="CLOCK")
label_text = sg.Text("Select unit to convert.", key="LABEL")
converts = sg.Spin(["Select", "Length", "Weight", "Area"], enable_events=True, key="CONVERTS", size=10)
result_label1 = sg.Text("Unit1", enable_events=True,  key="RESULT_LABEL1")
result1 = sg.Input(tooltip="Enter a number to convert", enable_events=True, key="RESULT1")
col1 = [[result_label1], [result1]]
result_label2 = sg.Text("Unit2", key="RESULT_LABEL2")
result2 = sg.Input(tooltip="Enter a number to convert", enable_events=True, key="RESULT2")
col2 = [[result_label2], [result2]]
exit_button = sg.Button("Exit", key="EXIT")
clear_button = sg.Button("Clear", key="CLEAR")
sg.theme("BrightColors")
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
            if value["CONVERTS"] == "Select":
                window["RESULT_LABEL1"].update("Unit1")
                window["RESULT_LABEL2"].update("Unit2")
                window["RESULT1"].update("")
                window["RESULT2"].update("")
            elif value["CONVERTS"] == "Length":
                window["RESULT_LABEL1"].update("Meter")
                window["RESULT_LABEL2"].update("Feet")
                window["RESULT1"].update("")
                window["RESULT2"].update("")
            elif value["CONVERTS"] == "Weight":
                window["RESULT_LABEL1"].update("Kg")
                window["RESULT_LABEL2"].update("Lb")
                window["RESULT1"].update("")
                window["RESULT2"].update("")
            elif value["CONVERTS"] == "Area":
                window["RESULT_LABEL1"].update("Square meter")
                window["RESULT_LABEL2"].update("Square feet")
                window["RESULT1"].update("")
                window["RESULT2"].update("")
        case "RESULT1":
            result = value["RESULT1"]
            if result:
                try:
                    if value["CONVERTS"] == "SELECT":
                        sg.popup("Please select a unit to convert.")
                        window["RESULT1"].update("")
                    if value["CONVERTS"] == "Length":
                        length = value["RESULT1"]
                        window["RESULT2"].update(ct.m_ft(length))
                    elif value["CONVERTS"] == "Weight":
                        weight = value["RESULT1"]
                        window["RESULT2"].update(ct.kg_lb(weight))
                    elif value["CONVERTS"] == "Area":
                        area = value["RESULT1"]
                        window["RESULT2"].update(ct.sqm_sqft(area))
                except ValueError:
                    sg.popup("Please enter numeric value.")
                    window["RESULT1"].update("")
                    window["RESULT2"].update("")
            else:
                window["RESULT2"].update("")
        case "RESULT2":
            result = value["RESULT2"]
            if result:
                try:
                    if value["CONVERTS"] == "SELECT":
                        sg.popup("Please select a unit to convert.")
                        window["RESULT1"].update("")
                    if value["CONVERTS"] == "Length":
                        length = value["RESULT2"]
                        window["RESULT1"].update(ct.ft_m(length))
                    elif value["CONVERTS"] == "Weight":
                        weight = value["RESULT2"]
                        window["RESULT1"].update(ct.lb_kg(weight))
                    elif value["CONVERTS"] == "Area":
                        area = value["RESULT2"]
                        window["RESULT1"].update(ct.sqft_sqm(area))
                except ValueError:
                    sg.popup("Please enter numeric value.")
                    window["RESULT1"].update("")
                    window["RESULT2"].update("")
            else:
                window["RESULT1"].update("")
        case "CLEAR":
            window["CONVERTS"].update("Select")
            window["RESULT_LABEL1"].update("Unit1")
            window["RESULT_LABEL2"].update("Unit2")
            window["RESULT1"].update("")
            window["RESULT2"].update("")
        case sg.WIN_CLOSED:
            break
        case "EXIT":
            break
