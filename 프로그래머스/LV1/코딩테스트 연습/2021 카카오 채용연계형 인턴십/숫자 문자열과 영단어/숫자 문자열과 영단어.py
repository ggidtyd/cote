numbers = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number_word_dic = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}
def solution(s):
    answer = 0
    for i in range(10):
        s = s.replace(numbers[i], number_word_dic[numbers[i]])
    answer = int(s)
    return answer