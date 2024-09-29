import java.io.*;
import java.util.*;
class PrintUniqueSubstrings {
    
    public static void main(String... args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Input the string: ");
        String str = s.next();
        printUniqueSubstrings(str);
    }

    private static void printUniqueSubstrings(String str) {
        Set<String> set = new HashSet<>();

        for(int i=0; i<str.length(); i++) {
            StringBuilder sb = new StringBuilder();
            for(int j=i; j<str.length(); j++) {
                sb.append(str.charAt(j));
                set.add(sb.toString());
            }
        }

        System.err.println(set);
    }
}