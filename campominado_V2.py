import PySimpleGUI as sg
tamanho = 6  
layout = [[sg.Button(f'{a}{b}',size=(4,2),button_color="LightGrey",disabled_button_color=("DarkGrey","Grey")) for b in range(tamanho)]for a in range(tamanho)]
window = sg.Window('Campo Minado',layout,resizable=True,element_justification="Center")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    window[f'{event}'].update(disabled=True)
    
window.close()

