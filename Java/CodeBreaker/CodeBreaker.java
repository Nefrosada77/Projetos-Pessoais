package Java.CodeBreaker;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class CodeBreaker extends JFrame implements ActionListener {
        int turn = 0;
        JButton exit = new JButton("EXIT");
        JButton confirm = new JButton("CONFIRM");
        JLabel icon = new JLabel();
        GridPanel codebreakGrid = new GridPanel();

        CodeBreaker() {
                Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();

                final int screen_Width = dim.width;
                final int screen_Height = dim.height;

                this.setUndecorated(true);
                this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
                this.setVisible(true);
                this.setLayout(null);
                this.setContentPane(
                                new JLabel(new ImageIcon("Java/CodeBreaker/Textures/JudgementCyan.png")));

                JPanel windowWest = new JPanel();
                windowWest.setLayout(new GridBagLayout());
                windowWest.setBackground(new Color(0, 0, 0, 0));

                JPanel windowEast = new JPanel();
                windowEast.setLayout(new GridBagLayout());
                windowEast.setBackground(new Color(0, 0, 0, 0));

                JPanel windowNorth = new JPanel();
                windowNorth.setLayout(new BorderLayout());
                windowNorth.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
                windowNorth.setBackground(new Color(0, 0, 0, 50));

                JPanel codebreakerPanel = new JPanel();
                codebreakerPanel.setLayout(null);
                codebreakerPanel.setBackground(Color.BLACK);

                JPanel greenHPanel = new JPanel();
                greenHPanel.setBackground(Color.green);
                greenHPanel.setLayout(new GridLayout(3, 1));

                JPanel greenVPanel = new JPanel();
                greenVPanel.setBackground(Color.green);
                greenVPanel.setLayout(new GridLayout(1, 3));

                JPanel yellowHPanel = new JPanel();
                yellowHPanel.setBackground(Color.YELLOW);
                yellowHPanel.setLayout(new GridLayout(3, 1));

                JPanel yellowVPanel = new JPanel();
                yellowVPanel.setBackground(Color.yellow);
                yellowVPanel.setLayout(new GridLayout(1, 3));

                JLabel HBLabel = new JLabel();
                // HBLabel.setIcon(new ImageIcon("HBIMAGE"));

                LastPlaysPanel HistoryPanel = new LastPlaysPanel();

                for (int i = 1; i < 13; i++) {
                        JLabel newLabel = new JLabel("0");
                        newLabel.setHorizontalAlignment(JLabel.CENTER);
                        newLabel.setVerticalAlignment(JLabel.CENTER);
                        if (i <= 3) {
                                greenHPanel.add(newLabel);
                        }
                        if (i > 3 && i <= 6) {
                                greenVPanel.add(newLabel);
                        }
                        if (i > 6 && i <= 9) {
                                yellowHPanel.add(newLabel);
                        }
                        if (i > 9) {
                                yellowVPanel.add(newLabel);
                        }
                }

                exit.addActionListener(this);
                confirm.addActionListener(this);
                exit.setPreferredSize(new Dimension(100, 100));
                confirm.setPreferredSize(new Dimension(100, 100));
                icon.setHorizontalAlignment(JLabel.CENTER);
                icon.setOpaque(true);
                icon.setBackground(new Color(0, 0, 0, 100));
                icon.setIcon(new ImageIcon("Java/CodeBreaker/Textures/MAKETHECODE.png"));
                icon.setPreferredSize(new Dimension(icon.getIcon().getIconWidth(), icon.getIcon().getIconHeight()));

                windowNorth.add(exit, BorderLayout.WEST);
                windowNorth.add(icon, BorderLayout.CENTER);
                windowNorth.add(confirm, BorderLayout.EAST);

                windowEast.add(codebreakerPanel);
                codebreakerPanel.add(codebreakGrid);
                codebreakerPanel.add(greenHPanel);
                codebreakerPanel.add(greenVPanel);
                codebreakerPanel.add(yellowHPanel);
                codebreakerPanel.add(yellowVPanel);
                codebreakerPanel.add(HBLabel);

                windowWest.add(HistoryPanel);

                this.add(windowEast);
                this.add(windowWest);
                this.add(windowNorth);

                windowNorth.setBounds(0, 0, screen_Width, screen_Height / 8);
                windowEast.setBounds(((screen_Width * 4) / 7), screen_Height / 8,
                                ((screen_Width * 3) / 7), screen_Height - windowNorth.getHeight());
                windowWest.setBounds(0, screen_Height / 8,
                                (screen_Width * 4) / 7, screen_Height - windowNorth.getHeight());
                codebreakerPanel.setPreferredSize(new Dimension(500, 500));
                codebreakGrid.setBounds(0, 0, 390, 390);
                greenHPanel.setBounds(390, 0, 55, 390);
                greenVPanel.setBounds(0, 390, 390, 55);
                yellowHPanel.setBounds(445, 0, 55, 390);
                yellowVPanel.setBounds(0, 445, 390, 55);
                HBLabel.setBounds(390, 390, 110, 110);
                this.pack();
                this.setExtendedState(JFrame.MAXIMIZED_BOTH);
        }

        @Override
        public void actionPerformed(ActionEvent e) {
                if (e.getSource() == exit) {
                        this.dispose();
                }
                if (e.getSource() == confirm) {
                        turn += 1;
                        codebreakGrid.getInputGrid();

                        /*
                         * DEBUG CHECK VALUES
                         * for (int i = 0; i < inputGrid.length; i++) {
                         * for (int j = 0; j < inputGrid[i].length; j++) {
                         * if (i != 3 && i != 4 && j != 3 && j != 4) {
                         * System.out.print(inputGrid[i][j] + " ");
                         * }
                         * }
                         * System.out.println();
                         * }
                         */
                }
        }

        public static void main(String[] args) {
                new CodeBreaker();
        }
}
