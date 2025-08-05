package Java.CodeBreaker;

import java.awt.*;
import javax.swing.*;

public class GridPanel extends JPanel {
    ButtonPanel btn1 = new ButtonPanel();
    ButtonPanel btn2 = new ButtonPanel();
    ButtonPanel btn3 = new ButtonPanel();
    ButtonPanel btn4 = new ButtonPanel();
    ButtonPanel btn5 = new ButtonPanel();
    ButtonPanel btn6 = new ButtonPanel();
    ButtonPanel btn7 = new ButtonPanel();
    ButtonPanel btn8 = new ButtonPanel();
    ButtonPanel btn9 = new ButtonPanel();
    ButtonPanel[][] btnArray = { { btn1, btn2, btn3 }, { btn4, btn5, btn6 }, { btn7, btn8, btn9 } };

    GridPanel() {
        this.setLayout(new GridLayout(3, 3));
        for (int i = 0; i < btnArray.length; i++) {
            for (int j = 0; j < btnArray.length; j++) {
                this.add(btnArray[i][j]);
            }
        }

    }

    public int getValue(int i, int j) {
        return btnArray[i][j].value;
    }

    public int[][] getInputGrid() {
        int[][] inputGrid = { { 0, 0, 0 }, { 0, 0, 0 }, { 0, 0, 0 } };
        for (int i = 0; i < inputGrid.length; i++) {
            for (int j = 0; j < inputGrid.length; j++) {
                inputGrid[i][j] = this.getValue(i, j);
            }
        }
        return inputGrid;
    }

}
