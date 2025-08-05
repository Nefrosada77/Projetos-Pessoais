package Java.CodeBreaker;

import java.awt.Color;
import java.awt.event.*;
import javax.swing.*;

public class ButtonPanel extends JPanel implements MouseListener {
    int value = 1;
    JLabel BtnIcon = new JLabel(new ImageIcon("Java/CodeBreaker/Textures/1.png"));

    ButtonPanel() {
        BtnIcon.setAlignmentX(JLabel.CENTER_ALIGNMENT);
        BtnIcon.setAlignmentY(JLabel.CENTER_ALIGNMENT);
        BtnIcon.addMouseListener(this);
        BtnIcon.setBounds(0, 0, BtnIcon.getIcon().getIconWidth(), BtnIcon.getIcon().getIconHeight());
        this.setLayout(null);
        this.add(BtnIcon);
        this.setBackground(Color.LIGHT_GRAY);
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        if (e.getButton() == MouseEvent.BUTTON1) {
            if (value >= 9) {
                value = 1;
            } else {
                value += 1;
            }
        }
        if (e.getButton() == MouseEvent.BUTTON3) {
            if (value <= 1) {
                value = 9;
            } else {
                value -= 1;
            }
        }
        BtnIcon.setIcon(new ImageIcon("Java/CodeBreaker/Textures/" + Integer.toString(value) + ".png"));
    }

    public void mouseEntered(MouseEvent e) {

    }

    public void mouseExited(MouseEvent e) {

    }

    public void mousePressed(MouseEvent e) {

    }

    public void mouseReleased(MouseEvent e) {

    }
}
