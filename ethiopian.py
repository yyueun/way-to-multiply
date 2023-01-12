def hello():
    print("Good luck!")

if __name__=='__main__':
    hello()
def multiply_two(division_num:int, multiply_num):
  multiply_list = [multiply_num]
  while division_num!=1:
    multiply_list.append(multiply_num*2)
    division_num=division_num//2
    multiply_num=multiply_num*2

  return multiply_list

def division_two(division_num:int):
  division_list = [division_num]
  while division_num!=1:
    division_list.append(division_num//2)
    division_num=division_num//2

  return division_list

def ethiopian(division_list, multiply_list):
  result = 0
  for i in range(len(division_list)) :
    if division_list[i] %2 == 0:
      result = result
    else:
      result += multiply_list[i]
  
  return result

num_list = input("숫자 두개를 입력해주세요. 숫자하나를 입력하고 스페이스바를 한번 누른 뒤 다른 숫자를 입력하세요: ")
division_num = int(num_list.split()[0])
multiply_num = int(num_list.split()[1])

result = ethiopian(division_two(division_num), multiply_two(division_num, multiply_num))

print(result)
