import PySimpleGUI as sg
from buttons import *    
sg.Popup('Welcome to my CALCULATOR')


equasion = ''   
while True:
    button, values = form.Read()  
    if button is None:  
        break
    if button is 'Clear':  
        equasion = ''
    elif button is 'Del':  
        equasion = equasion[:-1]
    elif button in '1234567890+-*/.()':
        equasion = values['input']  
        equasion += button  
    elif button is '=':
        if equasion == '' :    # if enter = while not have input
            pass    # no effect to window
        elif '/0' in equasion:    # if number divide by 0 
            equasion = 'Syntax Error'    # display show Syntax Error
        elif equasion[0] in '*/':    # if equasion start by * or /
            equasion = 'Syntax Error'    # display show Syntax Error
        elif equasion[-1] in '+-*/':    # if equasion end by + or - or * or /
            equasion = 'Syntax Error'    # display show Syntax Error
        elif '++' in equasion:     # if in equasion have + stuck together (ex.++)
            equasion = 'Syntax Error'   # display show Syntax Error
        elif '--' in equasion:      # if in equasion have - stuck together (ex.--)
            equasion = 'Syntax Error'   # display show Syntax Error
        elif '//' in equasion:      # if in equasion have / stuck together (ex.//)
            equasion = 'Syntax Error'   # display show Syntax Error
        else :
            equasion = values['input']
            equasion = eval(equasion)   # summary equasion
    if len(str(equasion)) >= 27 : 
        equasion = equasion[:-1] 

    form.FindElement('out').Update(equasion)  
    form.FindElement('input').Update(equasion)  
