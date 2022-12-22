donations = input().split(", ")
beggars_count = int(input())

int_donations =[]
result = [0] * beggars_count

for num in donations:
    int_donations.append(int(num))

for index, element  in enumerate(int_donations):
    result[index % beggars_count] += element

        
print(result)
