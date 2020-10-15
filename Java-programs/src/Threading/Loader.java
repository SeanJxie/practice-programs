package Threading;

// Creates a new thread.
public class Loader extends Thread {
    private int threadPriority;

    Loader(int threadPriority) {
        this.threadPriority = threadPriority;
    }

    public void run() {
        setPriority(this.threadPriority); // Setting the thread priority.
        System.out.println("Thread loaded with priority " + threadPriority);
    }
}
