import pyinputplus as pyip
import os

class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_book(self, book):
        new_node = Node(book)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if book < current.book:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search_book(self, book_title):
        current = self.root
        while current is not None:
            if book_title == current.book:
                return True
            elif book_title < current.book:
                current = current.left
            else:
                current = current.right
        return False

    def remove_book(self, book_title):
        def find_min(node):
            current = node
            while current.left is not None:
                current = current.left
            return current

        def remove_node(node, book_title):
            if node is None:
                return node
            if book_title < node.book:
                node.left = remove_node(node.left, book_title)
            elif book_title > node.book:
                node.right = remove_node(node.right, book_title)
            else:
                if node.left is None and node.right is None:
                    node = None
                elif node.left is None:
                    node = node.right
                elif node.right is None:
                    node = node.left
                else:
                    min_node = find_min(node.right)
                    node.book = min_node.book
                    node.right = remove_node(node.right, min_node.book)
            return node

        self.root = remove_node(self.root, book_title)

    def display_tree(self, node, level=0):
        if node is not None:
            self.display_tree(node.right, level + 1)
            print("    " * level + str(node.book))
            self.display_tree(node.left, level + 1)

tree = BinaryTree()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Cari Buku")
    print("4. Tampilkan Tree")
    print("5. Exit")

    choice = pyip.inputInt("Enter your choice: ", min=1, max=5)

    if choice == 1:
        book_title = pyip.inputStr("Masukan Judul Buku: ")
        tree.add_book(book_title)
        print("Buku Ditambahkan!")

    elif choice == 2:
        book_title = pyip.inputStr("Masukan Judul Buku: ")
        tree.remove_book(book_title)
        print("Buku Dihapus!")

    elif choice == 3:
        book_title = pyip.inputStr("Masukan Judul Buku: ")
        if tree.search_book(book_title):
            print("Buku Ditemukan!")
        else:
            print("Buku tidak ditemukan!")

    elif choice == 4:
        print("Binary Tree:")
        tree.display_tree(tree.root)

    elif choice == 5:
        break

    input("Tekan Enter to lanjut...")

print("Program selesai.")