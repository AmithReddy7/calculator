class Calculator {
  public static void main(String args[]) {

    if (args.length != 2) {
      System.out.println("Please provide exactly two integer values.");
      return;
    }

    try {
      int n1 = Integer.parseInt(args[0]);
      int n2 = Integer.parseInt(args[1]);

      System.out.println("Addition: " + (n1 + n2));
      System.out.println("Subtraction: " + (n1 - n2));
      System.out.println("Multiplication: " + (n1 * n2));

      if (n2 != 0) {
        System.out.println("Division: " + (n1 / n2));
      } else {
        System.out.println("Division: Cannot divide by zero.");
      }

    } catch (NumberFormatException e) {
      System.out.println("Please enter valid integers.");
    }
  }
}
