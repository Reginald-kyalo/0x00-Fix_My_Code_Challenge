#include "sort.h"

/**
 * selection_sort - sorts an array of integers in ascending
 *			order using selection sort algorithm
 * @array: array of integers to be sorted
 * @size: size of array
 *
 * Return: void
 */
void selection_sort(int *array, size_t size)
{
	size_t i = 0, j = 0, min = 0;

	int temp = 0;

	if (array == NULL || size == 0)
		return;

	for (i = 0; i < n - 1; i++)
	{
		min = i;

		for (j = i + 1; j < n; j++)
		{
			if (a[j] < a[min])
			{
				min = j;
			}
		}
		if (min != i)
		{
			temp = array[i];
			array[i] = array[min];
			array[min] = temp;
			print_array(array, size);
		}
	}
}

