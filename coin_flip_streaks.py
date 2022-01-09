'''
Write a program to find out how often a streak of six heads or a streak
of six tails comes up in a randomly generated list of heads and tails.
'''
import random


streaks = 0
for x in range(10000):
    flips = []
    tCount, hCount = 0, 0
    for i in range(100):

        if random.randint(0, 1) == 1:
            if hCount > 0 or hCount <6:
                hCount = 0
            flips.append("T")
            tCount += 1

            if tCount == 6:
                streaks += 1
                tCount = 0
        else:
            if tCount >0 or tCount <6:
                tCount = 0
            flips.append("H")
            hCount += 1
            if hCount == 6:
                streaks +=1
                hCount = 0

# testFlips = ["T","T","T","T","T","T","H","H","T","H","H","H","H","H","H","H","T","H","H","H","H","H","H"]
# tCombo, hCombo, streaks = 0, 0, 0
# for i in range(len(testFlips)):
#     if testFlips[i] == "T":
#         tCombo += 1
#         if hCombo > 0 or hCombo <6:
#             hCombo = 0
#         if tCombo == 6:
#             streaks += 1
#             tCombo = 0
#
#     else:
#         hCombo += 1
#         if hCombo == 6:
#             streaks += 1
#             hCombo = 0
#         if tCombo > 0 or tCombo < 6:
#             tCombo = 0


print('Chance of getting a streak is ' ,str((streaks/(10000*100))* 100) + "%")
#print((streaks/len(testFlips))*100)
print('%s streaks' % (streaks))
