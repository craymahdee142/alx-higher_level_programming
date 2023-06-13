#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 *insert_node - insert a number into sorted node
 *@number: num to insert
 *@head: pointer to a linked list head
 *Return: points to a new node or 0 if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *insert, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	insert = current->next;

	while (current && insert && number > insert->n)
	{
		current = current->next;
		insert = insert->next;
	}

	current->next = new_node;
	new_node->next = insert;
			
	return (new_node);
}
