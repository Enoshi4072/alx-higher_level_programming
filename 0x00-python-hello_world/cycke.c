#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - check for a douly linkd list
 * @list: the head of the list to check
 * Return: 1 if there is a cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	/* check if the head is empty or consist of one node */
	listint_t *first = list; /* Beginning of the list */
	listint_t *after_first = list->next; /* Step ahead of the first */

	if (list == NULL || list->next == NULL)
		/* No cycle, return 0 */
		return (0);
	/* Check if the pointers meet each other or they reach the end of the list */
	while (first != after_first)
	{
		if (after_first == NULL || after_first->next == NULL)
		{
			return (0); /* No cycle */
		}
		/*Move the first step forward*/
		first = first->next;
		/* Move the after_first one step forward also */
		after_first = after_first->next->next;
	}
	/* If exit, the pointers have meet */
	return (1);
}
