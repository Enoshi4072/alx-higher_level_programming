#include "lists.h"

/**
 * insert_node - Inserts the node at a given position
 * in a sorted list
 * @head: pointer to the beginning of the node
 * @number: The int to add to the linked list
 * Return: Pointer to the newnode
 */

listint_t *insert_node(listint_t **head, int number)
{
	/* Lets create a new node */
	listint_t *n_node, *c_node;

	n_node = (listint_t *)malloc(sizeof(listint_t));
	/* Check if the n_node is created */
	if (n_node == NULL)
		return (NULL);
	n_node->n = number;
	n_node->next = NULL;
	/* Make the n_node as the head if the list provided is empty */
	if ((*head) == NULL)
	{
		n_node->next = *head;
		*head = n_node;
	}
	/* start with the beginning if the first element is smaller than number */
	if (number < (*head)->n)
	{
		n_node->next = *head;
		*head = n_node;
	}
	/* Find the position to insert the node */
	c_node = *head;
	while (c_node->next != NULL && c_node->next->n < number)
	{
		/* Move to the next node in the list */
		c_node = c_node->next;
	}
	/* Connect the nodes */
	n_node->next = c_node->next;
	c_node->next = n_node;
return (n_node);
}

