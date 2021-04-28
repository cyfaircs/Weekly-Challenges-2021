package myproject;

import java.util.Arrays;
import java.util.Scanner;


public class testing {

	public static void main(String[] args) throws java.lang.NumberFormatException{
		Scanner keyboard = new Scanner(System.in);
		String input = keyboard.nextLine();
		
		String[] numArray = input.split(",");
		double[] numbers = new double[numArray.length];
		
		for(int i = 0; i < numArray.length; i++) {
			numArray[i] = numArray[i].trim();
			numbers[i] = Double.parseDouble(numArray[i]);
		}
		
		sortArray(numbers);
		System.out.print(Arrays.toString(numbers));
	}
	
	public static void sortArray(double[] nums) {
		for(int i = 0; i < nums.length; i++) {
			for(int j = 0; j < nums.length - i - 1; j++) {
				if(nums[j] > nums[j+1]) {
					double temp = nums[j];
					nums[j] = nums[j+1];
					nums[j+1] = temp;
				}
			}
		}
	
	}


}
