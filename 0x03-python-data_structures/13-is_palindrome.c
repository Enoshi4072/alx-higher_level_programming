#include "lists.h"
/**
 * rev_list - reverses a linked list
 * @head: Pointer to the beginning of the linked list
 * Return: pointer to the reversed node
 */
listint_t *rev_list(listint_t *head)
{
	listint_t *pn_rev, *c_node, *nx_node;

	c_node = head;
	pn_rev = NULL;

	while (c_node != NULL)
	{
		nx_node = c_node->next; /* To hold the current node */
		c_node->next = pn_rev; /* Make the next of the first pointer to null */
		pn_rev = c_node; /* Move the previous node one step ahead */
		c_node = nx_node; /* move the current node to the nexy step */
	}
	return (pn_rev);
}
/**
 * is_palindrome - Checks if a given list is a palindrom
 * @head: pointer to the beginning of the linked list
 * Return: 1 if the list is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *a_node, *c_node, *b_node, *list_a, *list_b;
	listint_t *pn_rev;

	/* If the list is empty, it is a palindrome */
	if ((*head) == NULL)
		return (1);
	/* If it contains one element, it is a palindrom */
	if ((*head)->next == NULL)
	{
		return (1);
	}
	/* Let us find the center of the list */
	c_node = *head; /* The current node */
	b_node = *head; /* The node after the current node */
	a_node = NULL; /* The node befor the current node*/
	while (b_node != NULL && b_node->next != NULL)
	{
		b_node = b_node->next->next; /* Move to the node ahead */
		a_node = c_node; /* move the node after the current node ahead */
		c_node = c_node->next; /* Move the current node one step ahead */
	}
	list_a = c_node; /*The middle of the node*/
	a_node->next = NULL; /* disconnection btn list_a and list_b */
	pn_rev = rev_list(list_a);
	/* Comparison between the first list and the second list */
	list_b = *head; /* Since the first node is connected to the head*/
	while (list_b != NULL && pn_rev != NULL)
	{
		if (list_b->n != pn_rev->n)
			return (0); /* Not a palindrome */
		list_b = list_b->next; /* Move one step ahead in the first list*/
		pn_rev = pn_rev->next; /* move one step ahead in the 2nd list */
	}
	return (1);
}
