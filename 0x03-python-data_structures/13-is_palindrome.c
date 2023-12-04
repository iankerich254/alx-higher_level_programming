#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - reverses a singly-linked listint_t list
 * @head: pointer to starting node of list to reverse
 * Return: pointer to head of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly-linked is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not a palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp_ke, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp_ke = *head;
	while (tmp_ke)
	{
		size++;
		tmp_ke = tmp_ke->next;
	}

	tmp_ke = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp_ke = tmp_ke->next;

	if ((size % 2) == 0 && tmp_ke->n != tmp_ke->next->n)
		return (0);

	tmp_ke = tmp_ke->next->next;
	rev = reverse_listint(&tmp_ke);
	mid = rev;

	tmp_ke = *head;
	while (rev)
	{
		if (tmp_ke->n != rev->n)
			return (0);
		tmp_ke = tmp_ke->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}

