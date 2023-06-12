#include "lists.h"

/**
 * reverse_listint - reverse a singly linked  list
 * @hwad: pointer to a node of list to reverse
 * Return: reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to new head
 * Return: 1 if linked list is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *first_half = NULL, *second_half = NULL;

	if (*head != NULL || (*head)->next != NULL)
	{
		return (1);
	}

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	/* reverse the second half of the list */
       	second_half = reverse_listint(&slow);
	first_half = *head;
	
	/* compare first half and reversed second half of the lis */
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			return (0); /* list is not palindrome */
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
