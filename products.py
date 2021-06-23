import os #operating system作業系統
#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf_8_sig') as f:
        for line in f:
            if '商品,價格' in line:
                continue         
            name, price = line.strip().split(',')
            products.append([name, price])
    return products
#使用者輸入
def user_input(products):
    while True:
        name = input('輸入商品名稱:')
        if name == 'q':
            break
        price = input('輸入商品價格:')
        products.append([name,price])
    return products    
#印出
def print_porducts(products):
    for p in products:
        print(p[0], '的價格是', p[1])
#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf_8_sig') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')




def main():
    products = []
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('水唷!找到了!')
        products = read_file(filename)
    else:
        print('裝肖偉喔?找不到啊!')
    products = user_input(products)
    print_porducts(products)
    write_file('products.csv', products)

if __name__ == '__main__':
    main()