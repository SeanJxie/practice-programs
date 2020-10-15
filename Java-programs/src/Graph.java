package FunctionGrapher;

/*
A simple graphing program.
- Change the method functionToGraph() to a desired function and run.
 */

import java.awt.*;
import javax.swing.*;

public class Graph extends Canvas {
    private static int windowWidth = 800, windowHeight = 800;

    public static void main(String[] args) {
        Graph graph = new Graph();
        JFrame f = new JFrame();

        f.add(graph);
        f.setSize(windowWidth, windowHeight);
        f.setVisible(true);

        f.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }

    // Override paint method.
    public void paint(Graphics g) {
        // Axis
        Graphics2D g2 = (Graphics2D) g;
        g2.translate(windowWidth / 2, windowWidth / 2); // We move the (0, 0) to the center of the window.
        g2.rotate(-3.1415 / 2); // In radians. we rotate everything by -90 degrees.

        g2.draw(new java.awt.geom.Line2D.Double(
                        0, (double) windowHeight / 2, 0, (double) -windowHeight / 2
                )
        );

        g2.draw(new java.awt.geom.Line2D.Double(
                        (double) -windowWidth / 2, 0, (double) windowWidth / 2, 0
                )
        );

        double y1, x2 = (double) -windowWidth / 2, y2 = functionToGraph(x2); // Initial coordinates.

        double graphAccuracy = 0.02; // Gap between each point.
        double zoomScale = 40; // Scale factor.

        for (double x = (double) -windowWidth / 2; x < (double) windowWidth / 2; x += graphAccuracy) {
            y1 = functionToGraph(x);

            // The x and y axes are swapped. We swap the coordinates here to get the correct graph.
            g2.draw(new java.awt.geom.Line2D.Double(y1 * zoomScale, x * zoomScale, y2 * zoomScale, x2 * zoomScale));

            x2 = x;
            y2 = y1;
        }
    }

    // THE FUNCTION TO GRAPH.
    public double functionToGraph(double x) {
        return Math.sin(x);
    }
}
