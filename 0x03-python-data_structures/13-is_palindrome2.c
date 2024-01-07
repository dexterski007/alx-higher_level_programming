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
	size_t len = 0, halflen = 0, i = 0;
	listint_t *current = *head, *prev = NULL, *nextp;
	listint_t *first_half = NULL, *second_half = NULL;

	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	halflen = len / 2;
	current = *head;
	for (i = 0; i < halflen; i++)
	{
		nextp = current->next;
		current->next = prev;
		prev = current;
		current = nextp;
	}
	*head = prev;
	first_half = *head;
	second_half = current;
	for (i = 0; i < halflen; i++)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
