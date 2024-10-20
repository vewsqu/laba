pages = 100
strings_per_page = 50
symbols_per_string = 25
bytes_per_symbol = 4
total_bytes_per_book = pages * strings_per_page * symbols_per_string * bytes_per_symbol
disk_capacity_mb = 1.44
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024
number_of_books = disk_capacity_bytes // total_bytes_per_book
print("Количество книг, помещающихся на дискету:", int(number_of_books))
