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
            print(f"\n恭喜你猜对了，正确答案就是{secret_number}，你用了{attempts}次就猜中了！")
            return

    print(f"\n游戏结束！正确答案是{secret_number}。")

if __name__ == "__main__":
    guessing_game()    