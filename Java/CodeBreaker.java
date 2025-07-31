package Java;

import java.awt.*;
import javax.swing.*;

public class CodeBreaker {
    public static void main(String[] args) {

        Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();

        final int screen_Width = dim.width;
        final int screen_Height = dim.height;

        JFrame window = new JFrame();
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setUndecorated(true);
        window.setLayout(new BorderLayout());
        window.setVisible(true);

        JPanel historyPanel = new JPanel();
        historyPanel.setBackground(Color.LIGHT_GRAY);
        historyPanel.setPreferredSize(new Dimension(500, 0));

        JPanel mainPanel = new JPanel();
        mainPanel.setBackground(Color.darkGray);
        mainPanel.setPreferredSize(new Dimension(600, 400));
        mainPanel.setLayout(new GridBagLayout());

        JPanel gridPanel = new JPanel();
        gridPanel.setBackground(Color.gray);
        gridPanel.setLayout(new GridLayout(3, 3, 10, 10));
        gridPanel.setPreferredSize(new Dimension(400, 400));
        gridPanel.setAlignmentY(JComponent.CENTER_ALIGNMENT);

        for (int i = 0; i < 9; i++) {
            gridPanel.add(new JButton(Integer.toString(i)));
        }

        window.add(historyPanel, BorderLayout.WEST);
        window.add(mainPanel, BorderLayout.CENTER);
        mainPanel.add(gridPanel);
        window.setSize(screen_Width, screen_Height);
        window.setExtendedState(JFrame.MAXIMIZED_BOTH);
        window.setMinimumSize(new Dimension(window.getWidth(), window.getHeight()));
    }
}