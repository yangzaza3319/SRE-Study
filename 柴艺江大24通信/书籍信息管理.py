def add_book(book_title,*authors,**details):
    '''添加书籍信息并打印'''
    print(f"书籍标题{book_title}")
    print('作者：','、'.join(authors))#authors是一个元组，使用join方法将元组中的元素连接成字符串
    for i,j in details.items():
        print(i,j)
    print('-------录入完成--------')
add_book("《虚构集》",'博尔赫斯',year=1944,centre='现实与虚构的统一')
add_book('《阿莱夫》','博尔赫斯',year=1949,imortance='《永生与遗忘》')