#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: A singly-linked list
 * Return: 0 if no cycle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle_k, *hare_k;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle_k = list->next;
	hare_k = list->next->next;

	while (turtle_k && hare_k && hare_k->next)
	{
		if (turtle_k == hare_k)
			return (1);

		turtle_k = turtle_k->next;
		hare_k = hare_k->next->next;
	}
	return (0);
}
