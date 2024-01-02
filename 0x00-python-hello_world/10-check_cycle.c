#include "lists.h"

/**
 * check_cycle - checks if singly-linked list has a cycle
 * @list: singly-linked list
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);
		turtle = turtle->next;
		hare = hare->next->next;
	}
	return (0);
}
