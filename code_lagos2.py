##conditional class for 'IF' and 'ELSE'
##temp = 30
##if temp >30:
##    print("temp is normal")
##else:
##    print("temt is false")
##x = int(input('enter x scores'))
##y = int(input('enter y scores'))
##ans = x + y
##if ans > 50:
##    print('you score =',ans,'you pass!')
##else:
##    print('you score =',ans,'you fail!')
def tellStory():
    userPicks = dict()
    addPick('animal', userPicks)
    addPick('food', userPicks)
    addPick('city', userPicks) 
    story = storyFormat.format(**userPicks) 
    print(story)
