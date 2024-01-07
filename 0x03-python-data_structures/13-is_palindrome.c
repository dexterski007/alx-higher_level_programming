#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check the code for palind
 *
 * @head: head
 *
 * Return: 0 or 1.
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	return (check_palind(head, *head));
}


/**
 * check_palind - check the code for
 *
 * @head: head
 *
 * @final: final of list
 *
 * Return: 0 or 1
 */

int check_palind(listint_t **head, listint_t *final)
{
	if (final == NULL)
		return (1);
	if (check_palind(head, final->next) && (*head)->n == final->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
