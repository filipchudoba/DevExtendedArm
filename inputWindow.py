import PySimpleGUI as sg    
import sys
from os.path import exists

file_exists = exists("lkprpath.txt") 

if file_exists == False:
    #Layout
    layout = [[sg.Text('Insert path to the scenery folder ChudobaDesign_LKPR:'), sg.FolderBrowse()],
                 [sg.Submit(), sg.Cancel()]]   

    window = sg.Window('Line Generator', layout)    

    event, button = window.read()

    #Kdyz klikne na Cancel, tak se to vypne
    if event == "Cancel" or event == sg.WIN_CLOSED:
        sys.exit()

    window.close()

    sceneryPath  = button['Browse']

    sceneryPath = sceneryPath.replace("/", "\\\\")

    with open("lkprpath.txt", 'x') as f:
        f.write(sceneryPath)
else:
    with open("lkprpath.txt", 'r') as f:
        sceneryPath = (f.readlines())[0]