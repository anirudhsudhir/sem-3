#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int key;
  char val;
  struct Node *left;
  struct Node *right;
} Node;

Node *insert(Node *root, int key, int val);
int search(Node *root, int key);
void delete(Node **root, int key);
void preorderTraversal(Node *root);

Node *newNode(int key, int val);

int main() {
  Node *root = insert(NULL, 10, 'a');
  root = insert(root, 6, 'b');
  root = insert(root, 4, 'b');
  root = insert(root, 7, 'b');
  root = insert(root, 2, 'b');
  preorderTraversal(root);
  return 0;
}

Node *newNode(int key, int val) {
  Node *node = (Node *)malloc(sizeof(Node));
  node->key = key;
  node->val = val;
  node->left = NULL;
  node->right = NULL;

  return node;
}
Node *insert(Node *root, int key, int val) {
  if (root == NULL) {
    return newNode(key, val);
  }

  if (key < root->key) {
    root->left = insert(root->left, key, val);
  } else if (key > root->key) {
    root->right = insert(root->right, key, val);
  }

  return root;
}

void preorderTraversal(Node *root) {
  if (root == NULL) {
    return;
  }
  preorderTraversal(root->left);
  preorderTraversal(root->right);
  printf("%d - %c, ", root->key, root->val);
}
