###############################################
#   List and for loop
###############################################
#players = [{'Name':'Jason Alkain','Gender':'Male','Age':27},{'Name':'Shiro Nokami','Gender':'Male','Age':25},{'Name':'Hitomi Takashi','Gender':'Female','Age':21}]
#for player in players:
#    print('~~~~~~~~~~~~~~~')
#    for value in player:
#        print(value+':\n~ '+str(player[value]))
#    print('~~~~~~~~~~~~~~~')

###############################################
#   Lambda Challenge
###############################################


def calc_ms(h=0, m=0, s=0, ms=0): return 'Miliseconds: ' + \
    str((((60*h)*60)*1000)+((m*60)*1000)+(s*1000) + ms)


def calc_mns(yr): return 'Months: ' + str(yr*12)


print(calc_ms())
print(calc_ms(3, 16, 20, 375))
print(calc_mns(2))
yrs = 2
print('{} Years = {}'.format(str(yrs), calc_mns(yrs)))
