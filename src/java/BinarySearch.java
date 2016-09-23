/**
 * Copyright (C) 2016 Canux CHENG.
 * All right reserved.
 * Name: BinarySearch.java
 */

//package jva;

/**
 * Binary search
 * @author Canux CHENG canuxcheng@gmail.com
 * @version V1.0.0.0
 * @since Sat 17 Sep 2016 07:12:01 AM EDT
 */
public class BinarySearch
{
    public static void main(String[] args)
    {
        int[] array = {32, 19, -2, 48, 90};
        System.out.println(binarySearch(array, 0));
        System.out.println(binarySearch(array, -2));
    }

    /**
     * binary search for one value.
     * @param array.
     * @param key
     * @return mid
     */
    public static int binarySearch(int[] array, int key)
    {
        int min = 0;
        int max = array.length - 1;

        while (min <= max)
        {
            int mid = (min + max)>>1;

            if (key > array[mid])
            {
                min = mid + 1;
            }
            else if (key < array[mid])
            {
                max = mid - 1;
            }
            else
                return mid;
        }
        return -1;
    }
}
