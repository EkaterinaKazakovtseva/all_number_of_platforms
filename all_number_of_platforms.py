# Номер успешной посылки на Контесте ID 115014078
def all_number_of_platforms(weights, limit):
    weights.sort()
    number_of_platforms = 0
    left_index = 0
    right_index = len(weights)-1
    while left_index <= right_index:
        number_of_platforms += 1
        if weights[left_index] + weights[right_index] <= limit:
            left_index += 1
        right_index -= 1
    return number_of_platforms

weights = list(map(int, input().split()))
limit = int(input())

if __name__ == '__main__':
    print(all_number_of_platforms(weights, limit))