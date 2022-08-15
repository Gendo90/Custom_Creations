import java.io.*;
import java.util.*;

public class Solution {

    public static int getDeterminant(int[][] arr) {
        if(arr.length == 2) {
            return arr[0][0]*arr[1][1] - arr[1][0]*arr[0][1];
        }

        int result = 0;

        for (int a = 0; a < arr.length; a++) {
            int currVal = arr[0][a];

            int[][] nextMinorMatrix = new int[arr.length-1][arr.length-1];

            int rowSubtraction = 1;
            int colSubtraction = 0;

            for (int i = 0; i < arr.length; i++) {
                // skip the first row to get the minor matrix
                if (i == 0) {
                    continue;
                }

                for (int j = 0; j < arr.length; j++) {
                    // skip this column to get the minor matrix
                    if (a == j) {
                        continue;
                    }

                    if(a > j) {
                        colSubtraction = 0;
                    } else {
                        colSubtraction = 1;
                    }

                    nextMinorMatrix[i-rowSubtraction][j-colSubtraction] = arr[i][j];
                }
            }

            int subResult = currVal*getDeterminant(nextMinorMatrix);

            // add a sign flip here for odd values of a
            if(a % 2 == 1) {
                subResult *= -1;
            }
            result += subResult;
        }

        return result;
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        int[][] inputMatrix = {{3, 0, 0, -2, 4}, {0, 2, 0, 0, 0}, {0, -1, 0, 5, -3},
        {-1, 0, 1, 0, 6}, {0, -1, 0, 3, 2}};

        int[][] testMatrix = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};

        int[][] testMatrix2 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

        int determinant = Solution.getDeterminant(inputMatrix);

        System.out.println(determinant);
    }
}
