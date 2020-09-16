import random, time


def sum_with_for_loop(arr: "list"):
    total = 0
    for i, v in enumerate(arr):
        total += arr[i]
        time.sleep(random.randint(0.0, 1.0))
    return total


def main():
    numbers = [4, 10, 3]
    print(sum_with_for_loop(numbers))
    return


if __name__ == "__main__":
    main()
