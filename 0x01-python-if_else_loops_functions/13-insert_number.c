#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert a number into sorted linked list
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner_ke;
	listint_t *new;

	runner_ke = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (runner_ke->next != NULL)
	{
		if ((runner_ke->next)->n >= number)
		{
			new->next = runner_ke->next;
			runner_ke->next = new;
			return (new);
		}
		runner_ke = runner_ke->next;
	}

	new->next = NULL;
	runner_ke->next = new;
	return (new);
}

