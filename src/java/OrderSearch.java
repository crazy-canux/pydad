/**
 * Copyright (C) 2016 Canux CHENG.
 * All right reserved.
 * Name: OrderSearch.java
 */

//package java;

/**
 * Order Search.
 * @author Canux CHENG canuxcheng@gmail.com
 * @version V1.0.0.0
 * @since Sat 17 Sep 2016 07:17:33 AM EDT
 */
public class OrderSearch
{
    public static void main(String[] args)
    {
        int[] array = {29, -1, 37, 87, 34};
        System.out.println(orderSearch(array, 0));
        System.out.println(orderSearch(array, 37));
    }

    /**
     * order/liner search for one value, return the index.
     * @param array
     * @param key
     * @return i
     */
    public static int orderSearch(int[] array, int key)
    {
        for (int i = 0; i < array.length; i++)
        {
            if (array[i] == key)
            {
                return i;
            }
        }
        return -1;
    }
}

