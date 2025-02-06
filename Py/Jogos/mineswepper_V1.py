import os
import random
class Colors:

    reset = '\033[0m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

class Campo:

    def __init__(self,tam,qnt_bombas) -> None:
        self.tam = tam
        self.qnt_bombas = qnt_bombas
        self.criarCampo() 

    def criarCampo(self):
        self.minas = [[False for c in range(self.tam)]for l in range(self.tam)]
        self.camp = [['-' for c in range(self.tam)]for l in range(self.tam)]
        bomb_col = 0
        pnm = []
        snm = []
        for pn in range(self.tam):
            pnm.append(pn)
        for sn in range(self.tam):
            snm.append(sn)
        while bomb_col < self.qnt_bombas:
            linha = random.choice(pnm)
            coluna = random.choice(snm)
            if self.minas[linha][coluna] == True:
                pass
            else:
                self.minas[linha][coluna] = True
                bomb_col += 1
    
    def PrintarCampo(self):
        for l in range(len(self.camp)):
            if l == 0:
                for back in range(4):
                    print(end=" ")
                for refcoluna in range(self.tam):
                    print(refcoluna,end=" ")
                print()
                for back in range(4):
                    print(end=" ")
                for refcoluna in range(self.tam):
                    print("|",end=" ")                             
            print("")
            for c in range(len(self.camp)):
                if c == 0:
                    print(f"{l}- ",end="")
                if self.camp[l][c] == 1:
                    print(Colors.fg.lightblue,self.camp[l][c],end="")
                elif self.camp[l][c] == 2:
                    print(Colors.fg.lightgreen,self.camp[l][c],end="")
                elif self.camp[l][c] == 3:
                    print(Colors.fg.lightred,self.camp[l][c],end="")
                elif self.camp[l][c] == 4:
                    print(Colors.fg.blue,self.camp[l][c],end="")
                elif self.camp[l][c] == 5:
                    print(Colors.fg.red,self.camp[l][c],end="")
                elif self.camp[l][c] == 6:
                    print(Colors.fg.cyan,self.camp[l][c],end="")
                elif self.camp[l][c] == 7:
                    print(Colors.fg.black,self.camp[l][c],end="")
                else:
                    print(Colors.fg.darkgrey,self.camp[l][c],end="")
            print(Colors.reset,end="")  
        print()  
        
    def CavarPainel(self,x,y):
        contador = 0 

        if self.minas[x][y] == True:
            self.camp[x][y] = '*'
            self.PrintarCampo()
            return True

        else:
            if self.camp[x][y] != '-':
                        pass
            else:
                for l in range(x-1,x+2):
                    for c in range(y-1,y+2):
                        if (((l >= self.tam) or (l < 0)) or ((c >= self.tam) or (c < 0))):
                            pass
                        elif self.minas[l][c] == True:
                            contador += 1
                        else:
                            pass 
                self.camp[x][y] = contador
                if contador == 0:
                    self.camp[x][y] = 0            
                    for l in range(x-1,x+2):
                        for c in range(y-1,y+2):
                            if (((l >= self.tam) or (l < 0)) or ((c >= self.tam) or (c < 0))):
                                pass
                            else:
                                self.CavarPainel(l,c)

    def ChecarGrade(self):
        contador = 0
        for l in range(self.tam):
            for c in range(self.tam):
                if self.camp[l][c] != '-' and self.minas[l][c] == False:
                    contador += 1
                else:
                    pass
        if contador == ((self.tam**2 - self.qnt_bombas)):
            return True
  
id = False
while id == False:
    tamanho = int(input("Digite o tamanho de campo desejado: "))
    bombas = int(input("Digite a quantidade de bombas desejadas: "))
    if (tamanho**2) <= bombas or bombas < (tamanho**2/5):
        pass
    else:
        id = True
        Campominado = Campo(tamanho,bombas)
        GameOver = False
        GameWin = False

while GameOver != True:
    os.system('cls' if os.name == 'nt' else 'clear')
    Campominado.PrintarCampo()
    x = int(input("Digite linha: "))
    y = int(input("Digite coluna: "))
    if (x >= tamanho or x < 0) or (y >= tamanho or y < 0):
        pass
    else:
        GameOver = Campominado.CavarPainel(x,y)
        GameWin = Campominado.ChecarGrade()
        if GameWin == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            Campominado.PrintarCampo()
            print(Colors.fg.green,"Game Win")
            print(Colors.reset)
            break
        if GameOver == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            Campominado.PrintarCampo()
            print(Colors.fg.red,"Game Over")
            print(Colors.reset)
