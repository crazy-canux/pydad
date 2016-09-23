/**
 * Copyright (C) 2016 Canux CHENG.
 * All right reserved.
 * Name: BubbleSort.java
 */

//package java;

/**
 * Bubble Sort.
 * @author Canux CHENG canuxcheng@gmail.com
 * @version V1.0.0.0
 * @since Fri 16 Sep 2016 01:48:32 AM EDT
 */
public class BubbleSort
{
    public static void main(String[] args)
    {
        int[] array = {74, 27, 96, -1, 0, 35};

        printArray(array);
        bubbleSort(array);
        printArray(array);

        printArray(array);
        bubbleSortDesc(array);
        printArray(array);
    }

    public static void printArray(int[] array)
    {
        for (int i = 0; i < array.length; i++)
        {
            if (i == array.length - 1)
                System.out.println(array[i]);
            else
                System.out.print(array[i] + ",");
        }
    }

    /**
     * From min to max.
     * @param array
     * @return array
     */
    public static int[] bubbleSort(int[] array)
    {
        for (int i = 0; i < array.length - 1; i++)
        {
            for (int j = 0; j < array.length - 1 - i; j++)
            {
                if (array[j] > array[j + 1])
                {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        return array;
    }

    /**
     * From max to min.
     * @param array
     * @return array
     */
    public static int[] bubbleSortDesc(int[] array)
    {
        for (int i = 0; i < array.length - 1; i++)
        {
            for (int j = 0; j < array.length - 1 - i; j++)
            {
                if (array[j] < array[j+1])
                {
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
        return array;
    }
}
