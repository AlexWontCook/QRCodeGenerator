import qrcode
import qrcode.image.svg
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
    [sg.Text("Enter text:")],
    [sg.Input("",do_not_clear=False)],
    [sg.Button('Generate QR Code', size=(30,4))],
    [sg.Button('Exit', size=(30,4))],
    [sg.Image(filename=img,expand_x=True,expand_y=True,key="-IMAGE-")],
    [sg.Text("Current QR Code:"), sg.Text("",key="-OUTPUT-")],
    [sg.Radio("PNG","gen", key="-PNG-",default=True),sg.Radio("SVG","gen",key="-SVG-")]
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
            if values['-PNG-'] == True:
                img = qrcode.make(inputtext)
                cleanInput = inputtext.replace('/','')
                cleanInput2 = cleanInput.replace(':','')
                img.save(path + "\\"+ str(cleanInput2) + ".png")
                imgPath = path + "\\" + cleanInput2 + ".png"
                window['-IMAGE-'].update(imgPath)
                sg.popup_ok("File exported successfully to " + path,auto_close_duration=3,title="Success!")
            elif values['-SVG-'] == True:
                factory = qrcode.image.svg.SvgImage
                img = qrcode.make(inputtext,image_factory=factory)
                cleanInput = inputtext.replace('/','')
                cleanInput2 = cleanInput.replace(':','')
                img.save(path + "\\" + str(cleanInput2) + ".svg")
                sg.popup_ok("File exported successfully to " + path,auto_close_duration=3,title="Success!")
            window['-OUTPUT-'].update(inputtext)
            window.refresh()
            print("QR Code created:" + inputtext)
            print("QR Code has been saved to folder: " + path)
        qrCodeGenerator(USER_INP)