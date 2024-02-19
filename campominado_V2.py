import PySimpleGUI as sg
import random

sg.set_options(scaling=2)

class Jogo:

    def Menu_inicial(self) -> None:
        layoutMenu = [
        [sg.Text('Campo Minado',font=('Arial',100,'bold'),text_color='Grey')],
        [sg.Text('Tamanho da Grade: '), sg.InputText()],
        [sg.Text('Numero de Bombas: '), sg.InputText()],
        [sg.Button('Continue...')],
        [sg.Button('Sair')]
        ]   
        window = sg.Window('Menu_Campo_minado',layoutMenu,resizable=True,element_justification='Center')
        while True:
            event,values = window.read()
            if event == 'Sair':
                window.close()
                break
            if event == 'Continue...':  
                self.tamanho = int(values[0])
                self.nbombas = int(values[1])       
                if ((self.tamanho > 0 and self.tamanho <= 10) and (self.nbombas > (self.tamanho**2)/5 and self.nbombas <= (self.tamanho**2)/2)):
                    self.Blocos = (self.tamanho**2) - self.nbombas
                    self.layout = [
                    [sg.Button(button_text=f'{a}{b}',size=(4,2),button_color="Grey on Grey") for b in range(self.tamanho)]for a in range(self.tamanho)
                    ]
                    self.Bombas()
                    window.close()
                    self.jogo()
            else:  
                window.close()
                self.jogo()

    def Bombas(self):
        num = 0
        while num != self.nbombas:
            linha = [f'{l}' for l in range(self.tamanho)]
            coluna = [f'{c}' for c in range(self.tamanho)]
            lin = int(random.choice(linha))
            col = int(random.choice(coluna))
            if self.layout[lin][col].get_text() != "*":
                self.layout[lin][col] = sg.Button(button_text='*',size=(4,2),button_color="Grey on Grey")
                num +=1
            else:
                pass
        
    def Cavar(self,y,x):
        contador = 0
        if self.layout[y][x].get_text() != f'{y}{x}':
            pass
        else:
            for l in range(y-1,y+2):
                    for c in range(x-1,x+2):
                        if (((l >= self.tamanho) or (l < 0)) or ((c >= self.tamanho) or (c < 0))):
                            pass                    
                        elif self.layout[l][c].get_text() == '*':
                            contador += 1
                        else:
                            pass
            match contador:
                case 0:
                    self.Blocos -= 1
                    self.window[f'{y}{x}'].update(text=f'{contador}',disabled_button_color=('LightGrey',None),disabled=True)     
                    for l in range(y-1,y+2):
                                for c in range(x-1,x+2):
                                    if (((l >= self.tamanho) or (l < 0)) or ((c >= self.tamanho) or (c < 0))):
                                        pass
                                    else:
                                        self.Cavar(l,c)                    
                case 1:
                    self.Blocos -= 1
                    self.window[f'{y}{x}'].update(text=f'{contador}',disabled_button_color=('LightBlue',None),disabled=True)
                case 2:
                    self.window[f'{y}{x}'].update(text=f'{contador}',disabled_button_color=('Green',None),disabled=True)
                    self.Blocos -= 1    
                case 3:
                    self.window[f'{y}{x}'].update(text=f'{contador}',disabled_button_color=('Red',None),disabled=True)
                    self.Blocos -= 1    
                case 4:
                    self.window[f'{y}{x}'].update(text=f'{contador}',disabled_button_color=('DarkBlue',None),disabled=True)
                    self.Blocos -= 1     
                case 5:
                    self.window[f'{y}{x}'].update(text=f'{contador}',disabled_button_color=('DarkRed',None),disabled=True)
                    self.Blocos -= 1    
                case 6:
                    self.window[f'{y}{x}'].update(text=f'{contador}',disabled_button_color=('Cyan',None),disabled=True)
                    self.Blocos -= 1    
                case 7:
                    self.window[f'{y}{x}'].update(text=f'{contador}',disabled_button_color=('Black',None),disabled=True)
                    self.Blocos -= 1   
                case 8:
                    self.window[f'{y}{x}'].update(text=f'{contador}',disabled_button_color=('White',None),disabled=True)
                    self.Blocos -= 1

        
    def jogo(self):
        self.window = sg.Window('Campo Minado',self.layout,resizable=True,element_justification="Center",background_color="LightGrey")
        while True:  
            if self.Blocos == 0:
                self.window.close()  
                self.GameWinScreen() 
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                self.window.close()
            if event[0] == '*': 
                self.window.close()
                self.GameOverScreen()       
            else:
                y = int(event[0])
                x = int(event[1]) 
                self.Cavar(y,x)                    
          
    def GameOverScreen(self):
        layoutGameOver = [[sg.Text("GAME OVER",text_color='Red',justification='Center',font=('Arial',100,'bold'),background_color='Grey')],
                          [sg.Button('Tentar Novamente...',size=(50,3))],
                          [sg.Button('Sair',size = (50,3))],
                          ]
        GameOverWindow = sg.Window('GameOver Screen',layoutGameOver,element_justification='Center',resizable=True,background_color='Grey')
        while True:
            event, values = GameOverWindow.read()
            if event == sg.WIN_CLOSED:
                GameOverWindow.close()
                break
            if event == 'Tentar Novamente...':
                GameOverWindow.close()
                self.Menu_inicial()
            else:
                GameOverWindow.close()
                break
    
    def GameWinScreen(self):
        layoutGameWin = [[sg.Text("GAME WIN",text_color='Green',justification='Center',font=('Arial',100,'bold'),background_color='Grey')],
                          [sg.Button('Tentar Novamente...',size=(50,3))],
                          [sg.Button('Sair',size = (50,3))],
                          ]
        GameWinWindow = sg.Window('GameOver Screen',layoutGameWin,element_justification='Center',resizable=True,background_color='Grey')
        while True:
            event, values = GameWinWindow.read()
            if event == sg.WIN_CLOSED:
                GameWinWindow.close()
            if event == 'Tentar Novamente...':
                GameWinWindow.close()
                self.Menu_inicial()
            else:
                GameWinWindow.close()
                break

start = Jogo()
start.Menu_inicial()
