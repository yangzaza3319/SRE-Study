def add_book(book_title,*authors,**details):
    print(f"书籍标题：{book_title}")
    print("作者：","，".join(authors))
    for key,value in details.items():
        print(f"{key}:{value}")
    print("--------")

add_book("Pythom编程","Alice","Bob",year=2023,publisher="XYZ出版社")
add_book("数据科学入门","Charlie",year=2022,pages=350,genre="教育")
add_book("机器学习概论","David","Ella","Frank",year=2021)

