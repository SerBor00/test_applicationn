column_names = ['match_id', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty_one', 
                    'twenty_two', 'twenty_three', 'twenty_four', 'twenty_five', 'twenty_six', 'twenty_seven', 'twenty_eight', 'twenty_nine', 'thirty', 'extra_one', 'extra_two', 'extra_three', 'extra_four', 'extra_five', 'extra_six', 'extra_seven', 'extra_eight', 'extra_nine']

t = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]

t.sort(reverse=True)

for i in t:
    del column_names[i+1]
    
print(*column_names)