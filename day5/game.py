import random

# 컴퓨터가 무작위로 3자리 숫자를 생성
answer = str(random.randint(100, 999))

# 게임 횟수 카운트
count = 0

while True:
    # 사용자가 3자리 숫자를 입력
    guess = input("Enter a 3-digit number: ")

    # 사용자 입력이 3자리 숫자인지 확인
    if guess.isdigit() and len(guess) == 3:
        # 스트라이크, 볼, 아웃 카운트
        strike_count = 0
        ball_count = 0
        out_count = 0

        # 사용자 입력과 컴퓨터 생성 숫자를 비교
        for i in range(3):
            if guess[i] == answer[i]:
                strike_count += 1
            elif guess[i] in answer:
                ball_count += 1
            else:
                out_count += 1

        # 결과 출력
        print(
            "Strike: {}, Ball: {}, Out: {}".format(strike_count, ball_count, out_count)
        )
        count += 1

        # 정답을 맞추면 게임 종료
        if strike_count == 3:
            print("Congratulations! You won the game in {} tries!".format(count))
            break
    else:
        print("Invalid input. Please enter a 3-digit number.")
