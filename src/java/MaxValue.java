/**
 * Copyright (C) 2016 Canux CHENG.
 * All right reserved.
 * Name: MaxValue.java
 */

//package java;

/**
 * Get the max value or min value of a array.
 * @author Canux CHENG canuxcheng@gmail.com
 * @version V1.0.0.0
 * @since Tue 13 Sep 2016 09:53:30 AM EDT
 */
public class MaxValue
{
    public static void main(String[] args)
    {
        int[] array = {99, 17, -9, 68, 56};
        System.out.println(getMax(array));
        System.out.println(getMin(array));
    }

    /**
     * Get the max value from array.
     * @param array.
     * @return max
     */
    public static int getMax(int[] array)
     {
         int max = array[0];
         for (int i = 1; i < array.length; i++)
         {
             if (array[i] > max)
             {
                 max = array[i];
             }
         }
         return max;
     }

    /**
     * Get the min value from array.
     * @param array
     * @return min
     */
    public static int getMin(int[] array)
    {
        int min = array[0];
        for (int i = 1; i < array.length; i++)
        {
            if (array[i] < min)
            {
                min = array[i];
            }
        }
        return min;
    }
}
