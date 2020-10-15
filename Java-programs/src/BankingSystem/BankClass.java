package BankingSystem;

import java.util.HashMap;
import java.util.ArrayList;

/*

Playing with classes. Here's a nice little banking system with simple encryption.

*/

public class BankClass implements BankClassInterface {
    private int encryptionShift = 2;
    HashMap<ArrayList<String>, Double> accounts = new HashMap<ArrayList<String>, Double>();

    // We can encrypt a password and put the encryption somewhere without worrying about
    // our password being cracked. When we check a password, we simply encrypt it with the same algorithm.
    // If our saved encryption matches our current one, the passwords match.

    public String encrypt(String password, int shift) {
        StringBuilder encryptedString = new StringBuilder();
        for (char c : password.toCharArray()) {
            encryptedString.append((char) ((int) (c) + shift));
        }

        return encryptedString.toString();
    }

    public void addAccount(String accountID, String password) throws IllegalArgumentException {
        ArrayList<String> account = new ArrayList<String>(2);
        account.add(accountID);
        account.add(encrypt(password, encryptionShift));

        if (accounts.containsKey(account)) {
            throw new IllegalArgumentException("An account with this ID already exits.");
        } else {
            accounts.put(account, (double) 0); // Initial balance is $0;
        }
    }

    public void showAccount(String accountID, String password) throws IllegalArgumentException {
        ArrayList<String> account = new ArrayList<String>(2);
        account.add(accountID);
        account.add(encrypt(password, encryptionShift));

        if (!accounts.containsKey(account)) {
            throw new IllegalArgumentException("Account does not exist.");
        }

        System.out.println("ACCOUNT ID: " + account.get(0) + "\nENCRYPTION: " + account.get(1) + "\nBALANCE: " + accounts.get(account));
    }

    public void deleteAccount(String accountID, String password) throws IllegalArgumentException {
        ArrayList<String> account = new ArrayList<String>(2);
        account.add(accountID);
        account.add(encrypt(password, encryptionShift));

        if (!accounts.containsKey(account)) {
            throw new IllegalArgumentException("Account does not exist.");
        } else {
            accounts.remove(account);
        }
    }

    public void deposit(String accountID, String password, double amount) throws IllegalArgumentException {
        ArrayList<String> account = new ArrayList<String>(2);
        account.add(accountID);
        account.add(encrypt(password, encryptionShift));

        if (!accounts.containsKey(account)) {
            throw new IllegalArgumentException("Account does not exist.");
        } else {
            double newBalance = accounts.get(account) + amount;
            accounts.replace(account, newBalance);
        }
    }

    public void withdraw(String accountID, String password, double amount) throws IllegalArgumentException {
        ArrayList<String> account = new ArrayList<String>(2);
        account.add(accountID);
        account.add(encrypt(password, encryptionShift));

        double newBalance = accounts.get(account) - amount;

        if (!accounts.containsKey(account)) {
            throw new IllegalArgumentException("Account does not exist.");
        }

        if (newBalance < 0) {
            throw new IllegalArgumentException("Insufficient funds.");
        } else {
            accounts.replace(account, newBalance);
        }
    }
}
