package BankingSystem;

public interface BankClassInterface {
    void addAccount(String accountID, String password) throws IllegalArgumentException;

    void showAccount(String accountID, String password) throws IllegalArgumentException;

    void deleteAccount(String accountID, String password) throws IllegalArgumentException;

    void withdraw(String accountID, String password, double amount) throws IllegalArgumentException;

    void deposit(String accountID, String password, double amount) throws IllegalArgumentException;

    String encrypt(String password, int shift);
}
