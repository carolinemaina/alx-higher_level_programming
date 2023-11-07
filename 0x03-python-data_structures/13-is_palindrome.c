#include "lists.h"

/**
*is_palindrome - check if list is palindrome
*@head: head node
*Return: 1 if it is palindrome otherwise 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *new_h = *head;
	listint_t *a = NULL, *b = NULL;

	if (*head == NULL || new_h->next == NULL)
		return (1);
	while (new_h != NULL)
	{
		node_add(&a, new_h->n);
		new_h = new_h->next;
	}
	b = a;
	while (*head != NULL)
	{
		if ((*head)->n != b->n)
		{
			free_listint(a);
			return (0);
		}
		*head = (*head)->next;
		b = b->next;
	}
	free_listint(a);
	return (1);
}

/**
*node_add - add new node at beginning of a list
*@head: head node
*@n: int to add in list
*Return: address of new element otherwise NULL
*/
listint_t *node_add(listint_t **head, const int n)
{
	listint_t *a;

	a = malloc(sizeof(listint_t));
	if (a == NULL)
		return (NULL);
	a->n = n;
	a->next = *head;
	*head = a;
	return (a);
}
