import java.util.Scanner;

public class Triangle2 {
	public static void main(String[] args) {
		
		// Scanner sc = new Scanner(System.in);
		// System.out.print("Size: ");
		// int size = sc.nextInt();

        int size = 5;
		
		for (int row = 0; row <= size; row++) {
			printSpace(size,row);
			printStars(row);
			System.out.println();
		}
			
	}
	static void printSpace(int size, int row) {
		for (int column = size; column > row; column--) {
			System.out.print(' ');
		}
	}
	
	static void printStars(int row) {
		
		for (int k = 0; k <= 2 * row; k++) {
			System.out.print('*');
		}
	}
}