import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            guess = int(input(f"\n请输入你的猜测（第{attempts + 1}/{max_attempts}次）："))
        except ValueError:
            # 避免非整数的内容，如作弊等
            print("请输入有效的整数！")
            continue

        attempts += 1

        if guess < secret_number:
            print("太小")
        elif guess > secret_number:
            print("太大。")
        else:
            print(f"\n你猜对了，用了{attempts}次猜中")
            return

    print(f"\n正确答案是{secret_number}。")

if __name__ == "__main__":
    guessing_game()    