#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check the code for
 *
 * @head: head
 *
 * Return: 0 or 1.
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	return (aux_palind(head, *head));
}


/**
 * aux_palind - check the code for
 *
 * @head: head
 *
 * @end: end list
 */

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return(1);
	}
	return (0);
}