#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to next node
 * Description: singly linked list node structure
 */
typedef struct listsint_s
{
	int n;
	struct listint_s *next;
} listsint_t;

size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);

#endif /* LISTS_H */
