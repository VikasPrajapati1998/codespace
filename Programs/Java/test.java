import java.util.*;
public class test{
    public static void main(String[] args){
        System.out.println("Name and Age Printer.");
        Scanner sc = new Scanner(System.in);
        String name;
        System.out.print("Enter Name : ");
        name = sc.nextLine();

        int age;
        System.out.print("Enter Age : ");
        age = sc.nextInt();

        System.out.println("Your name is " + name + "and age is " + age);

        sc.close();
        
    }
}