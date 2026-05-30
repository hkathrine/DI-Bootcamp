import math


class Pagination():
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        self.total_number_of_pages = math.ceil(len(self.items) / self.page_size)
    
    def get_visible_items(self):
        start = self.current_idx * int(self.page_size)
        end = start + self.page_size
        return self.items[start:end]
    
    def go_to_page(self, page_num):
        int_page_num = int(page_num)
        if int_page_num > self.total_number_of_pages or int_page_num <= 0:
            raise ValueError(f"Page number {int_page_num} is out of range.")
        
        self.current_idx = int_page_num - 1

        return self
    
    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_number_of_pages - 1
        return self
    
    def next_page(self):
        if self.current_idx < (self.total_number_of_pages - 1):
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx != 0:
            self.current_idx -= 1
        return self
    
    def __str__(self):
        start = self.current_idx * int(self.page_size)
        end = start + self.page_size
        str_current_page = self.items[start:end]

        return "\n".join(str(item) for item in str_current_page)
    

#tests
   
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.get_visible_items())# ['a', 'b', 'c', 'd']

p.next_page()

print(p.get_visible_items())# ['e', 'f', 'g', 'h']

p.last_page()

print(p.get_visible_items())# ['y', 'z']

try:
    p.go_to_page(10) 
except ValueError as e:
    print(f"Error: {e}") # ValueError

p.last_page()

try:
    print(p.current_idx + 1)# Output: ValueError
except ValueError as e:
    print(f"Error: {e}") # ValueError


try:
    p.go_to_page(0)
except ValueError as e:
    print(f"Error: {e}")# Raises ValueError

