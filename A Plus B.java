//Tudor is sitting in math class, on his laptop. Clearly, he is not paying attention in this situation. However, he gets called on by his math teacher to do some problems. Since his math teacher did not expect much from Tudor, he only needs to do some simple addition problems. However, simple for you and I may not be simple for Tudor , so please help him!

//Input Specification
//The first line will contain an integer N (1≤N≤100000), the number of addition problems Tudor needs to do. The next N lines will each contain two space-separated integers whose absolute value is less than 1000000000, the two integers Tudor needs to add.

//Output Specification
//Output N lines of one integer each, the solutions to the addition problems in order.


import java.util.Scanner;
import java.util.Arrays;

public class Main {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
    int num = myObj.nextInt();
    // Create an array with room for 100 integers
    int[] array = new int[num];
    myObj.nextLine();

    // Fill it with numbers using a for-loop
    for (int i = 0; i < num; i++) {
      String str = myObj.nextLine();
      String[] parts = str.split(" ");
      array[i] = Integer.parseInt(parts[0]) + Integer.parseInt(parts[1]);
    }

    for (int i = 0; i < num; i++) {
      System.out.println(array[i]);
    }


  }
}