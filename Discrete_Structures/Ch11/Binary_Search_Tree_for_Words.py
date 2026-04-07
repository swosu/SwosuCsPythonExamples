# ------------------------------------------------------------
# Binary Search Tree for Words
# ------------------------------------------------------------
# This program builds a binary search tree (BST) using words.
# It uses alphabetical order to decide where each word goes.
#
# WHY THIS IS USEFUL:
# A BST can make searching more efficient than scanning a list
# from start to finish, especially when the tree is fairly balanced.
#
# BASIC IDEA:
# - If a new word comes before the current word alphabetically,
#   go LEFT.
# - If a new word comes after the current word alphabetically,
#   go RIGHT.
# - Keep doing that until you find an empty spot.
#
# In this example, we first use the exercise words:
# mathematics, physics, geography, zoology, meteorology,
# geology, psychology, chemistry
#
# Then we add many more words so the tree becomes larger.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Define one node of the tree
# ------------------------------------------------------------
class Node:
    def __init__(self, word):
        # The value stored in this node
        self.word = word

        # Pointers to the left and right child nodes
        self.left = None
        self.right = None


# ------------------------------------------------------------
# Step 2: Define the Binary Search Tree class
# ------------------------------------------------------------
class BinarySearchTree:
    def __init__(self):
        # At the beginning, the tree has no root
        self.root = None

    # --------------------------------------------------------
    # Insert a word into the tree
    # --------------------------------------------------------
    def insert(self, word):
        # If the tree is empty, this word becomes the root
        if self.root is None:
            self.root = Node(word)
        else:
            # Otherwise, find the correct place for the word
            self._insert_recursive(self.root, word)

    def _insert_recursive(self, current_node, word):
        # Compare alphabetically
        if word < current_node.word:
            # The new word belongs on the LEFT side
            if current_node.left is None:
                current_node.left = Node(word)
            else:
                self._insert_recursive(current_node.left, word)

        elif word > current_node.word:
            # The new word belongs on the RIGHT side
            if current_node.right is None:
                current_node.right = Node(word)
            else:
                self._insert_recursive(current_node.right, word)

        else:
            # If the word is equal, we skip it to avoid duplicates
            # You could change this behavior if you want duplicates allowed
            pass

    # --------------------------------------------------------
    # Search for a word in the tree
    # Returns True if found, False if not found
    # --------------------------------------------------------
    def search(self, word):
        return self._search_recursive(self.root, word)

    def _search_recursive(self, current_node, word):
        # If we hit an empty branch, the word is not in the tree
        if current_node is None:
            return False

        # If we found the word, return True
        if word == current_node.word:
            return True

        # If the word comes before the current node, search left
        if word < current_node.word:
            return self._search_recursive(current_node.left, word)

        # Otherwise search right
        return self._search_recursive(current_node.right, word)

    # --------------------------------------------------------
    # In-order traversal:
    # Left -> Root -> Right
    #
    # This is special because in a BST it prints the words in
    # sorted alphabetical order.
    # --------------------------------------------------------
    def inorder(self):
        words = []
        self._inorder_recursive(self.root, words)
        return words

    def _inorder_recursive(self, current_node, words):
        if current_node is not None:
            self._inorder_recursive(current_node.left, words)
            words.append(current_node.word)
            self._inorder_recursive(current_node.right, words)

    # --------------------------------------------------------
    # Pretty print the tree sideways
    #
    # This is not the only way to draw a tree, but it gives a
    # nice visual shape in the console.
    # --------------------------------------------------------
    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, current_node, level):
        if current_node is not None:
            # First print the right subtree higher on the page
            self._print_tree_recursive(current_node.right, level + 1)

            # Print the current node with indentation
            print("    " * level + "-> " + current_node.word)

            # Then print the left subtree lower on the page
            self._print_tree_recursive(current_node.left, level + 1)


# ------------------------------------------------------------
# Step 3: Build the tree with the exercise words
# ------------------------------------------------------------
exercise_words = [
    "mathematics",
    "physics",
    "geography",
    "zoology",
    "meteorology",
    "geology",
    "psychology",
    "chemistry"
]

# ------------------------------------------------------------
# Step 4: Add many more words to make the tree bigger
# ------------------------------------------------------------
extra_words = [
    "algebra", "biology", "botany", "calculus", "computation",
    "data", "ecology", "economics", "engineering", "ethics",
    "geometry", "grammar", "history", "language", "literature",
    "logic", "music", "philosophy", "poetry", "programming",
    "science", "statistics", "trigonometry", "writing", "astronomy",
    "anatomy", "architecture", "art", "coding", "design",
    "education", "finance", "geophysics", "journalism", "law",
    "medicine", "nursing", "robotics", "sociology", "theology"
]

# Combine both lists into one large list
all_words = exercise_words + extra_words


# ------------------------------------------------------------
# Step 5: Create the tree and insert all words
# ------------------------------------------------------------
bst = BinarySearchTree()

for word in all_words:
    bst.insert(word)


# ------------------------------------------------------------
# Step 6: Show the tree structure
# ------------------------------------------------------------
print("\nBINARY SEARCH TREE (sideways):\n")
bst.print_tree()


# ------------------------------------------------------------
# Step 7: Show the words in alphabetical order
# ------------------------------------------------------------
print("\nWORDS IN ALPHABETICAL ORDER:\n")
print(bst.inorder())


# ------------------------------------------------------------
# Step 8: Test searching for a few words
# ------------------------------------------------------------
test_words = ["chemistry", "psychology", "robotics", "dance"]

print("\nSEARCH RESULTS:\n")
for word in test_words:
    if bst.search(word):
        print(f"{word}: found")
    else:
        print(f"{word}: not found")