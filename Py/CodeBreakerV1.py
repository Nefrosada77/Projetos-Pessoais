import random  
import PySimpleGUI as sg
'''-----------------------------------------------------------'''
#CRIAÇÃO DA MATRIX DOS NUMEROS QUE SERÃO SELECIONADOS
NUM = []
for a in range(1,10):
    NUM.append(a)

#CRIAÇÃO DA GRID
GRID = [[""for x in range(3)]for y in range(3)]

#IMPLEMENTANDO OS NUMEROS NA GRID
for y in range(len(GRID)):
    for x in range(len(GRID[0])):
        NUM_SELECT = random.randrange(len(NUM))
        GRID[y][x] = NUM[NUM_SELECT]
        NUM.pop(NUM_SELECT)
    
for linha in GRID:
    print(linha)
'''-----------------------------------------------------------'''
#JOGO
LAYOUTGAME = [[sg.Button(button_text=1) for x in range(3)]for y in range(3)]
window = sg.Window('Code Breaker V.1',LAYOUTGAME)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
        break
    if event != 'CONFIRM':
        match int(event):
            case 1:
                but = int(LAYOUTGAME[0][0].get_text())
                if but != 9:
                    LAYOUTGAME[0][0].update(but+1)
                else:
                    LAYOUTGAME[0][0].update(1)
            case 10:
                but = int(LAYOUTGAME[0][1].get_text())
                if but != 9:
                    LAYOUTGAME[0][1].update(but+1)
                else:
                    LAYOUTGAME[0][1].update(1)
            case 11:
                but = int(LAYOUTGAME[0][2].get_text())
                if but != 9:
                    LAYOUTGAME[0][2].update(but+1)
                else:
                    LAYOUTGAME[0][2].update(1)
            case 12:
                but = int(LAYOUTGAME[1][0].get_text())
                if but != 9:
                    LAYOUTGAME[1][0].update(but+1)
                else:
                    LAYOUTGAME[1][0].update(1)
            case 13:
                but = int(LAYOUTGAME[1][1].get_text())
                if but != 9:
                    LAYOUTGAME[1][1].update(but+1)
                else:
                    LAYOUTGAME[1][1].update(1)
            case 14:
                but = int(LAYOUTGAME[1][2].get_text())
                if but != 9:
                    LAYOUTGAME[1][2].update(but+1)
                else:
                    LAYOUTGAME[1][2].update(1)
            case 15:
                but = int(LAYOUTGAME[2][0].get_text())
                if but != 9:
                    LAYOUTGAME[2][0].update(but+1)
                else:
                    LAYOUTGAME[2][0].update(1)
            case 16:
                but = int(LAYOUTGAME[2][1].get_text())
                if but != 9:
                    LAYOUTGAME[2][1].update(but+1)
                else:
                    LAYOUTGAME[2][1].update(1)
            case 17:
                but = int(LAYOUTGAME[2][2].get_text())
                if but != 9:
                    LAYOUTGAME[2][2].update(but+1)
                else:
                    LAYOUTGAME[2][2].update(1)