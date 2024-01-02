#include "lists.h"
/**
 * insert_node - inserts a digit into a sorted
 * singly-linked list
 * @head: pointer to head of linked list
 * @number: digit to insert
 * Return: NULL if fails, pointer if not
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *nnew;

	nnew = malloc(sizeof(listint_t));
	if (nnew == NULL)
		return (NULL);
	nnew->n = number;

	if (node == NULL || node->n >= number)
	{
		nnew->next = node;
		*head = nnew;
		return (nnew);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	nnew->next = node->next;
	node->next = nnew;

	return (nnew);
}
