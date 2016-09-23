/**
 * Copyright (C) 2016 Canux CHENG.
 * All right reserved.
 * Name: SelectionSort.java
 */

//package java;

/**
 * Selection sort for array.
 * @author Canux CHENG canuxcheng@gmail.com
 * @version V1.0.0.0
 * @since Tue 13 Sep 2016 10:06:41 AM EDT
 */
public class SelectionSort
{
    public static void main(String[] args)
    {
        int[] array = {11, 99, 29, -7, 75, 26};

        printArray(array);
        selectionSort(array);
        printArray(array);

        printArray(array);
        selectionSortDesc(array);
        printArray(array);
    }

    public static void printArray(int[] array)
    {
        for (int i = 0; i < array.length; i++)
        {
            if (i != array.length - 1)
                System.out.print(array[i] + ", ");
            else
                System.out.println(array[i]);
        }
    }

    /**
     * From min to max.
     * @param array.
     * @return array.
     */
    public static int[] selectionSort(int[] array)
    {
        for (int i = 0; i < array.length - 1; i++)
        {
            for (int j = i+1; j < array.length; j++)
            {
                if (array[i] > array[j])
                {
                    int temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
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
    public static int[] selectionSortDesc(int[] array)
    {
        for (int i = 0; i < array.length - 1; i++)
        {
            for (int j = i + 1; j < array.length; j++)
            {
                if (array[i] < array[j])
                {
                    int temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
        }
        return array;
    }
}
