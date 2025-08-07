package Java;

import java.awt.*;
import java.awt.geom.Path2D;
import javax.swing.*;

public class test extends JPanel {
    private static final int PREF_W = 600;
    private static final int PREF_H = PREF_W;
    private static final Color COLOR_1 = Color.blue;
    private static final Color COLOR_2 = Color.red;
    private static final Paint GRADIENT_PAINT = new GradientPaint(0, 0, COLOR_1, 20, 20, COLOR_2, true);
    private Path2D myPath = new Path2D.Double();

    public test() {
        double firstX = (PREF_W / 2.0) * (1 - 1 / Math.sqrt(3));
        double firstY = 3.0 * PREF_H / 4.0;

        myPath.moveTo(firstX, firstY);
        myPath.lineTo(PREF_W - firstX, firstY);
        myPath.lineTo(PREF_W / 2.0, PREF_H / 4.0);
        myPath.closePath();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;

        // to smooth out the jaggies
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);
        g2.setPaint(GRADIENT_PAINT); // just for fun!
        g2.fill(myPath); // fill my triangle
    }

    @Override
    public Dimension getPreferredSize() {
        if (isPreferredSizeSet()) {
            return super.getPreferredSize();
        }
        return new Dimension(PREF_W, PREF_H);
    }

    private static void createAndShowGui() {
        test mainPanel = new test();

        JFrame frame = new JFrame("Path2DExample");
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.getContentPane().add(mainPanel);
        frame.pack();
        frame.setLocationByPlatform(true);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGui();
            }
        });
    }
}
