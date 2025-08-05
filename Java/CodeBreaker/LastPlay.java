package Java.CodeBreaker;

import java.awt.*;
import javax.swing.*;

public class LastPlay extends JPanel {

    /*
     * 0 0 0 1 1
     * 0 0 0 1 1
     * 0 0 0 1 1
     * 1 1 1 - -
     * 1 1 1 - -
     */

    LastPlay() {
        this.setBackground(Color.lightGray);
        this.setLayout(new GridBagLayout());
        this.setPreferredSize(new Dimension(35 * 5, 35 * 5));
        this.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        this.setLayout(null);
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                JLabel newLabel = new JLabel("0");
                newLabel.setHorizontalAlignment(JLabel.CENTER);
                newLabel.setVerticalAlignment(JLabel.CENTER);
                newLabel.setName(Integer.toString(i) + Integer.toString(j));
                newLabel.setBounds(j * 35, i * 35, 35, 35);
                newLabel.setOpaque(true);
                this.add(newLabel);
            }
        }
        for (Component jlabel : this.getComponents()) {
            switch (jlabel.getName()) {
                case "03", "13", "23", "30", "31", "32":
                    jlabel.setBackground(Color.green);
                    break;
                case "04", "14", "24", "40", "41", "42":
                    jlabel.setBackground(Color.yellow);
                    break;
                case "33", "34", "43", "44":
                    this.remove(jlabel);
                    break;
                default:
                    jlabel.setBackground(new Color(0, 0, 0, 0));
                    break;
            }
        }

    }

}
