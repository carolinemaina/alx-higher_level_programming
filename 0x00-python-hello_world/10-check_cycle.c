#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle
 * @list: A pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *n1, *n2;

	if (list == NULL || list->next == NULL)
	{
		return 0;
	}

	n1 = list;
	n2 = list->next;

	while (n2 != NULL && n2->next != NULL)
	{
		if (n1 == n2)
		{
			return 1;
		}
		n1 = n1->next;
		n2 = n2->next->next;
	}

	return 0;
}
