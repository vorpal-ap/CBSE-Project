'''
Push, Pop, and Peep operations in stack
'''



BooksStack = []

def push_book(BooksStack, new_book):
    BooksStack.append(new_book)


def pop_book(BooksStack):
    if not BooksStack:
        return "Underflow"
    return BooksStack.pop()


def peep(BooksStack):
    if not BooksStack:
        return "None"
    return BooksStack[-1]


push_book(BooksStack, ['Book1', 'Author1', 2020])
push_book(BooksStack, ['Book2', 'Author2', 2019])
push_book(BooksStack, ['Book3', 'Author3', 2018])

print(BooksStack)
print(pop_book(BooksStack))
print(peep(BooksStack))
