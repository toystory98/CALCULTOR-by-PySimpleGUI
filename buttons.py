import PySimpleGUI as sg

# set button
buttons = [[sg.Text('Enter Your Equasion')],    
          [sg.Input(size=(27, 15), font=('Cordia New', 30), do_not_clear=True, justification='right', key='input')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('+')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('*')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('Del'), sg.ReadFormButton('/')],
          [sg.ReadFormButton('('),sg.ReadFormButton(')'),sg.ReadFormButton('='),sg.ReadFormButton('Clear')],
          [sg.Text('', size=(15, 1), font=('Cordia New', 30), text_color='white', key='out')],
          ]
#set button size
form = sg.FlexForm('Keypad', default_button_element_size=(6, 2), font=('Cordia New', 30), auto_size_buttons=False, grab_anywhere=False)
form.Layout(buttons)