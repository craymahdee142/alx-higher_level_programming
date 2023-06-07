#include "lists.h"
/**
 *insert_node - function that insert into singly node
 *@head: pointer of head to node
 *@number: num to insert
 *Return: pointer to node if success, else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if(node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	/*adjust the node until correct position is found*/
	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}
	new->next = node->next;
	node-> = new;
	return (new);
}
