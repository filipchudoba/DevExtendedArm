import PySimpleGUI as sg    
import sys  

#Layout
layout = [[sg.Text('Insert path to the scenery folder ChudobaDesign_LKPR:')],      
                 [sg.InputText()],        
                 [sg.Submit(), sg.Cancel()]]   

window = sg.Window('Line Generator', layout)    

event, values = window.read()

#Kdyz klikne na Cancel, tak se to vypne
if event is "Cancel":
    sys.exit()

window.close()

sceneryPath = values[0]