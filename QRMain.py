#TODO FIX QR CODES WITH LINKS:
#Need to add a way to sanitize the slashes from the exported name

import qrcode
import PySimpleGUI as sg
import os


#Set QR Code path and blank img variable
path = "QRCodes"
img = ""

#Check if QRCodes folder exists, if not, it will be created
isExist = os.path.exists(path)
if not isExist:
    os.makedirs("QRCodes")
    print("QR Code folder created")

#GUI Layout
layout = [
    [sg.Text("Current export folder:"), sg.Text(path,key="-FOLDERPATH-"),sg.FolderBrowse("Change",key="-NEWFOLDER-")],
    [sg.Text("Enter Serial Number:")],
    [sg.Input("",do_not_clear=False)],
    [sg.Button('Generate QR Code', size=(30,4))],
    [sg.Button('Exit', size=(30,4))],
    [sg.Image(filename=img,expand_x=True,expand_y=True,key="-IMAGE-")],
    [sg.Text("Current QR Code:"), sg.Text("",key="-OUTPUT-")]
]

window = sg.Window('QR Code Generator', layout,element_justification='c')

#Event Handler, if Generate QR Code is clicked, take the user input and create a QR Code. Then refresh the img and input variables. Also checks for if folder is not the default
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Change':
        window["-FOLDERPATH-"].update(path)
        window.refresh()
    if event == 'Generate QR Code':
        path = values["-NEWFOLDER-"]
        if path == "":
            path = "QRCodes"
        current = values
        custName = current[0]
        USER_INP = str(custName)
        def qrCodeGenerator(inputtext):
            cleanInput = inputtext.replace('/','')
            img = qrcode.make(inputtext)
            img.save(path + "\\"+ str(cleanInput) + ".png")
            imgPath = path + "\\" + cleanInput + ".png"
            window['-OUTPUT-'].update(inputtext)
            window['-IMAGE-'].update(imgPath)
            window.refresh()
            print("QR Code created:" + inputtext)
            print("QR Code has been saved to folder: " + path)
        qrCodeGenerator(USER_INP)