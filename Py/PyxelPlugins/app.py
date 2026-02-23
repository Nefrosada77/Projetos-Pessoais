import pyxel as py
import panels as GUI

class App:
    WIDTH = GUI.WIDTH
    HEIGHT = GUI.HEIGHT
    hudState : int = 0

    def __init__(self):
        py.init(self.WIDTH,self.HEIGHT,title="Test",quit_key=py.KEY_ESCAPE)
        py.mouse(True)
        py.images[0].load(0,0,"textures/arrow.png")
        py.run(self.update, self.draw)
    
    def update(self):
        GUI.enemies.update()
        match self.hudState:
            case 0:
                if py.btnp(py.KEY_UP):
                    GUI.skillList.UP()
                if py.btnp(py.KEY_DOWN):
                    GUI.skillList.DOWN()
                if py.btnp(py.KEY_SPACE):
                    self.hudState = GUI.skillList.SELECT()
            case 1:
                if py.btnp(py.KEY_LEFT):
                    GUI.enemieSelctor.LEFT()
                if py.btnp(py.KEY_RIGHT):
                    GUI.enemieSelctor.RIGHT()
                if py.btnp(py.KEY_SPACE):
                    self.hudState = GUI.enemieSelctor.SELECT()                    
        
    def draw(self):
        py.cls(0)
        GUI.playerPanel.draw()
        GUI.enemies.draw()
        match self.hudState:
            case 0:
                #GUI.debugPanel.draw()
                GUI.skillList.draw()
            case 1:
                GUI.skillList.draw()
                GUI.enemieSelctor.draw()
    
App()