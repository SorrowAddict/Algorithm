M = int(input())
day = int(input())
if M == 2:
     if day < 18:
          print('Before')
     elif day > 18:
          print('After')
     else:
          print('Special')
elif M < 2:
     print('Before')
elif M > 2:
     print('After')