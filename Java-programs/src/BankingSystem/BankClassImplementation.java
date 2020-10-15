package BankingSystem;

/*
A simple banking system.
 */

public class BankClassImplementation {
    public static void main(String[] args) {
        BankClass bankingSystem = new BankClass();

        bankingSystem.addAccount("Sean", "password");

        bankingSystem.deposit("Sean", "password", 10);

        System.out.println(bankingSystem.accounts);

        bankingSystem.showAccount("Sean", "password");

        bankingSystem.withdraw("Sean", "password", 5);

        bankingSystem.showAccount("Sean", "password");

        bankingSystem.deleteAccount("Sean", "password");



    }
}
