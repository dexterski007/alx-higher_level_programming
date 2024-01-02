#include "lists.h"

/**
 * insert_node - insert node at index
 *
 * @head: node pointer
 * @number: num
 *
 * Return: data of node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *curr = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL || head == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (number == 0)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (curr)
	{
		if (!curr->next || new_node->n < curr->next->n)
		{
			new_node->next = curr->next;
			curr->next = new_node;
			return (curr);
		}
		curr = curr->next;
	}

	return (NULL);
}
