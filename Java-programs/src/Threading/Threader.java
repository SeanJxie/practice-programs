package Threading;

public class Threader {
    public static void main(String[] args) {
        Loader object1 = new Loader(1);
        object1.start(); // Since Loader is a subclass of Thread (Java.lang), we use Thread's start() method.

        Loader object2 = new Loader(2); // Another thread with different priority.
        object2.start();

    }
}
