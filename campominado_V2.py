import PySimpleGUI as sg
import random
continuar = False
while continuar == False:
tamanho = int(input("Tamanho da Grade: "))  
bombas = int(input("Numero de Bombas: "))
if (bombas > tamanho) or (bombas < tamanho/4):
    pass
else:
    continuar = True
layout = [[sg.Button(button_text=f'{a}{b}',size=(4,2),button_color="LightGrey",disabled_button_color=("DarkGrey","Grey")) for b in range(tamanho)]for a in range(tamanho)]
for num in range(bombas):
    linha = [f'{l}' for l in range(tamanho)]
    coluna = [f'{c}' for c in range(tamanho)]
    lin = int(random.choice(linha))
    col = int(random.choice(coluna))
    if layout[lin][col].get_text() != "*":
        layout[lin][col] = sg.Button(button_text='*',size=(4,2),button_color="LightGrey",disabled_button_color=("DarkGrey","Grey"))
    else:
        num -= 1
    
window = sg.Window('Campo Minado',layout,resizable=True,element_justification="Center")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break   
    if event == '*':
        print("Game Over")
        break
    else:
        cavacao = True   
        y = int(event[0])
        x = int(event[1])
        contador = 0
        for l in range(y-1,y+2):
            for c in range(x-1,x+2):
                if (((l >= tamanho) or (l < 0)) or ((c >= tamanho) or (c < 0))):
                    pass                    
                elif layout[l][c].get_text() == '*':
                    contador += 1
                else:
                    pass
        window[f'{event}'].update(text=f'{contador}',disabled=True)

                            
                




window.close()
