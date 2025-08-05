package Java.CodeBreaker;

import java.awt.*;
import javax.swing.*;

public class LastPlaysPanel extends JPanel {

    JPanel GridPanel = new JPanel();

    LastPlaysPanel() {
        this.setLayout(new GridBagLayout());
        this.setBackground(Color.gray);
        this.add(GridPanel);
        GridPanel.setLayout(new GridLayout(2, 4, 10, 10));
        GridPanel.setBackground(Color.BLACK);
        GridPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        for (int i = 0; i < 8; i++) {
            LastPlay newPlay = new LastPlay();
            GridPanel.add(newPlay);
        }
        this.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        this.setPreferredSize(getPreferredSize());

    }
}
