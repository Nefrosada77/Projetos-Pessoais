package Java;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class CodeBreaker {
    public static void main(String[] args) {
        JFrame window = new JFrame();
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.getContentPane().setBackground(Color.DARK_GRAY);
        window.setLayout(new BorderLayout());
        window.setVisible(true);

        JPanel lastPanel = new JPanel();
        lastPanel.setBackground(Color.LIGHT_GRAY);

        window.add(lastPanel, BorderLayout.WEST);

    }
}