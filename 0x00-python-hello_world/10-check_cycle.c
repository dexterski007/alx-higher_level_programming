#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - check cycle
 *
 * @list: list
 *
 * Return: 1 or 0
*/

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list == NULL)
		return (0);

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
		{
			first = list;
			while (second != first)
			{
				first = first->next;
				second = second->next;
			}
			return (1);
		}
	}
	return (0);
}

