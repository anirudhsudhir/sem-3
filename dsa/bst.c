#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int key;
  char val;
  struct Node *left;
  struct Node *right;
} Node;

Node *insert(Node *root, int key, int val);
char search(Node *root, int key);
Node *delete(Node *root, int key);
void inorderTraversal(Node *root);
void preorderTraversal(Node *root);

Node *newNode(int key, int val);

int main() {
  Node *root = insert(NULL, 10, 'a');
  root = insert(root, 6, 'b');
  root = insert(root, 4, 'c');
  root = insert(root, 7, 'd');
  root = insert(root, 2, 'e');
  preorderTraversal(root);
  printf("\nsearch key %d = val %c\n", 4, search(root, 4));
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
  printf("%d - %c, ", root->key, root->val);
  preorderTraversal(root->left);
  preorderTraversal(root->right);
}

char search(Node *root, int key) {
  if (root == NULL) {
    return '!';
  } else if (root->key == key) {
    return root->val;
  } else {
    if (root->key < key) {
      return search(root->right, key);
    } else {
      return search(root->left, key);
    }
  }
}

Node *delete(Node *root, int key) {
  if (root == NULL) {
    return NULL;
  }

  if (root->key > key) {
    delete (root->left, key);
  } else if (root->key < key) {
    delete (root->right, key);
  } else {
  }
}
