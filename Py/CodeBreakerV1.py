import random  
import PySimpleGUI as sg

sg.SetOptions(auto_size_buttons=False,button_element_size=(6,3),button_color=('DarkRed','Grey'),text_element_background_color='Grey',text_justification='Center')
'''-----------------------------------------------------------'''
#CRIAÇÃO DA MATRIX DOS NUMEROS QUE SERÃO SELECIONADOS
NUM = []
for a in range(1,10):
    NUM.append(a)

#CRIAÇÃO DA GRID
GRID = [[""for x in range(3)]for y in range(3)]
GRIDV = [[""for x in range(3)]for y in range(3)]

#IMPLEMENTANDO OS NUMEROS NA GRID
for y in range(len(GRID)):
    for x in range(len(GRID[0])):
        NUM_SELECT = random.randrange(len(NUM))
        GRID[y][x] = NUM[NUM_SELECT]
        NUM.pop(NUM_SELECT)

for y in range(3):
    for x in range(3):
        GRIDV[y][x] = GRID[((x-2)*(-1))][y]
    
for linha in GRID:
    print(linha)
print()
for linha in GRIDV:
    print(linha)
'''-----------------------------------------------------------'''
#JOGO
LAYOUTGAME = [[sg.Text('Turno: 1',key='Cont')],
            [sg.Button(button_text='1',key=0),sg.Button(button_text=1,key=1),sg.Button(button_text=1,key=2),sg.Text(text='0',text_color='White',background_color='Orange',size=(2,3),key=('H0')),sg.Text(text='0',text_color='White',background_color='Green',size=(2,3),key=('B0'))],
            [sg.Button(button_text='1',key=10),sg.Button(button_text=1,key=11),sg.Button(button_text=1,key=12),sg.Text(text='0',text_color='White',background_color='Orange',size=(2,3),key=('H1')),sg.Text(text='0',text_color='White',background_color='Green',size=(2,3),key=('B1'))],
            [sg.Button(button_text='1',key=20),sg.Button(button_text=1,key=21),sg.Button(button_text=1,key=22),sg.Text(text='0',text_color='White',background_color='Orange',size=(2,3),key=('H2')),sg.Text(text='0',text_color='White',background_color='Green',size=(2,3),key=('B2'))],
            [sg.Text(text='0',text_color='White',background_color='Orange',size=(5,1),key=('H3')),sg.Text(text='0',text_color='White',background_color='Orange',size=(5,1),key=('H4')),sg.Text(text='0',text_color='White',background_color='Orange',size=(5,1),key=('H5'))],
            [sg.Text(text='0',text_color='White',background_color='Green',size=(5,1),key=('B3')),sg.Text(text='0',text_color='White',background_color='Green',size=(5,1),key=('B4')),sg.Text(text='0',text_color='White',background_color='Green',size=(5,1),key=('B5'))],            
            [sg.Button('CONFIRM',size=(16,2),button_color="DarkRed on Grey")]]
window = sg.Window('Code Breaker V.1',LAYOUTGAME,element_justification='center',resizable=True,background_color="DarkGrey",scaling=3,text_justification='center')
turno = 1
Vitoria = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
        break
    
    if event != 'CONFIRM':
                but = int(window[event].get_text())
                if but != 9:
                    window[event].update(but+1)
                else:
                    window[event].update(1)
    else:
        for a in range(0,30,10):
            HitH = 0
            BeH = 0
            if window[a].get_text() in GRID[int(a/10)]:
                if window[a].get_text() == GRID[int(a/10)][0]:
                    HitH += 1
                else:
                    BeH += 1
            if window[a+1].get_text() in GRID[int(a/10)]:
                if window[a+1].get_text() == GRID[int(a/10)][1]:
                    HitH += 1
                else:
                    BeH += 1
            if window[a+2].get_text() in GRID[int(a/10)]:
                if window[a+2].get_text() == GRID[int(a/10)][2]:
                    HitH += 1
                else:
                    BeH += 1
            window[f'H{int(a/10)}'].update(HitH)
            window[f'B{int(a/10)}'].update(BeH)
        for a in range(0,3,1):
            HitV = 0
            BeV = 0
            if window[a].get_text() in GRIDV[a]:
                if window[a].get_text() == GRID[0][a]:
                    HitV += 1
                else:
                    BeV += 1
            if window[a+10].get_text() in GRIDV[a]:
                if window[a+10].get_text() == GRID[1][a]:
                    HitV += 1
                else:
                    BeV += 1
            if window[a+20].get_text() in GRIDV[a]:
                if window[a+20].get_text() == GRID[2][a]:
                    HitV += 1
                else:
                    BeV += 1
            window[f'H{a+3}'].update(HitV)
            window[f'B{a+3}'].update(BeV)
        turno += 1
        window['Cont'].update(f'Turno: {turno}')
        if turno == 8:
            window.close()
            break
