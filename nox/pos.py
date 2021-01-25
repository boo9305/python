
btn_pos = {}

btn_pos['wait'] = (0,0)

btn_pos['follow'] = (665, 347)  # 따라가기
btn_pos['auto'] = (920, 348)  # 자동공격
btn_pos['exit-normal'] = (928, 58) # 기본 종료 버튼

btn_pos['title-no'] = (419, 356) # 타이틀로가기 취소


btn_pos['ski1'] = (737, 412) # 왼쪽 상단
btn_pos['ski2'] = (794, 410)
btn_pos['ski3'] = (860, 412)
btn_pos['ski4'] = (919, 412)
btn_pos['ski5'] = (670, 471)
btn_pos['ski6'] = (742, 469)
btn_pos['ski7'] = (798, 467)
btn_pos['ski8'] = (671, 528) #7 비영사천문
btn_pos['ski9'] = (740, 529) #8 노랑비서
btn_pos['ski10'] = (794, 532) # change

btn_pos['dogam'] = (22, 330)
btn_pos['expr'] = (19, 287) 

btn_pos['map'] = (879, 104) # 지도
btn_pos['map-exit'] = (927, 59) # 지도 끄기
btn_pos['map-btn1'] = (587, 116) # 세계전도
btn_pos['map-btn2'] = (664, 118)  # 2번째 
btn_pos['map-sm'] = (40, 227)  # 제일 작게 

btn_pos['map-g-weapon'] = (190, 336) 
btn_pos['map-g-doin'] = (237, 460) # 국내성 - 도인

btn_pos['map-b-doin'] = (314, 456) # 부여 - 도인
btn_pos['map-b-weapon'] = (96, 378) # 부여 - 대장간

btn_pos['map1'] = (679, 310) # 지도 1번
btn_pos['map2'] = (680, 365)  
btn_pos['map3'] = (692, 440) 
btn_pos['map4'] = (697, 509) # 지도 4번


btn_pos['map1-move'] = (863, 305) # 지도 1번 바로 이동
btn_pos['map2-move'] = (863, 371) 
btn_pos['map3-move'] = (859, 440) 
btn_pos['map4-move'] = (864, 508) 

btn_pos['map1-walk'] = (912, 299) 
btn_pos['map2-walk'] = (920, 372) 
btn_pos['map3-walk'] = (910, 432) 
btn_pos['map4-walk'] = (913, 504) 


btn_pos['map-move-yes'] = (536, 357) # 지도 바로이동 허락
btn_pos['map-move-no'] = (417, 355) # 지도 바로이동 취소

btn_pos['doin-npc'] = (484, 171) # 도인의집 npc 클릭
btn_pos['doin-npc-btn1'] = (482, 308) # 대화 1번
btn_pos['doin-npc-btn2'] = (478, 360) # 대화 2번

btn_pos['doin-npc-sinsu1'] = (257, 185) # 현무
btn_pos['doin-npc-sinsu2'] = (392, 316) # 청룡
btn_pos['doin-npc-sinsu3'] = (238, 463) # 주작
btn_pos['doin-npc-sinsu4'] = (103, 308) # 백호
btn_pos['doin-npc-sinsu-hp'] = (865, 378) # hp 클릭
btn_pos['doin-npc-sinsu-mp'] = (860, 511) 

btn_pos['dungeon'] = (848, 189) # 던전
btn_pos['ground'] = (140,216) # 사냥터
btn_pos['ground1-1'] = (56, 116) # 사냥터1
btn_pos['ground1-2'] = (53, 168) # 사냥터2
btn_pos['ground1-3'] = (57, 229) 
btn_pos['ground1-4'] = (59, 272) 
btn_pos['ground1-5'] = (59, 334) 
btn_pos['ground1-6'] = (64, 386) 
btn_pos['ground1-7'] = (58, 432) 
btn_pos['ground1-8'] = (55, 482) 
btn_pos['ground1-9'] = (62, 538) 
btn_pos['ground2-1'] = (254, 134) 
btn_pos['ground2-2'] = (237, 209) 
btn_pos['ground2-3'] = (255, 272) 
btn_pos['ground2-4'] = (244, 335) 
btn_pos['ground2-5'] = (249, 400) 
btn_pos['ground2-6'] = (247, 474) 
btn_pos['ground2-7'] = (243, 535)

btn_pos['ground-map'] = (825, 208) 



btn_pos['menu1'] = (607, 75)  # 메뉴 왼쪽 상단
btn_pos['menu2'] = (644, 73)
btn_pos['menu3'] = (684, 74) 
btn_pos['menu4'] = (724, 73) 
btn_pos['menu5'] = (763, 73) 
btn_pos['menu6'] = (800, 73) 
btn_pos['menu7'] = (606, 113) 
btn_pos['menu8'] = (648, 113) 
btn_pos['menu9'] = (687, 113) 
btn_pos['menu10'] = (727, 114) 
btn_pos['menu11'] = (766, 112) 
btn_pos['menu12'] = (805, 111)

btn_pos['chat'] = (465, 482) 
btn_pos['chat1'] = (791, 242) 
btn_pos['chat2'] = (778, 282) 
btn_pos['chat3'] = (778, 322) 
btn_pos['chat4'] = (783, 365) 
btn_pos['chat5'] = (775, 404) 
btn_pos['chat6'] = (779, 446) 
btn_pos['chat7'] = (777, 484) 
btn_pos['chat8'] = (775, 529) 
btn_pos['chat9'] = (779, 565) 

btn_pos['dogam1'] = (792, 244) 

action = {}


action['recovery'] = [
    {'delay' : 1 , 'btn' : 'chat'},
    {'delay' : 1 , 'btn' : 'chat2'},
    {'delay' : 1 , 'btn' : 'chat'},
    {'delay' : 1 , 'btn' : 'chat3'},
]

action['home'] = [
    {'delay' : 3 , 'btn' : 'ski5'},
    {'delay' : 10 , 'btn' : 'wait'}
]

action['move_weapon'] = [
        # 대장간으로!
    {'delay' : 3 , 'btn' : 'map'},
    {'delay' : 3 , 'btn' : 'map-btn2'},
    {'delay' : 3 , 'btn' : 'map-sm'},
    {'delay' : 3 , 'btn' : 'map-b-weapon'},
    {'delay' : 3 , 'btn' : 'map2-walk'},
    {'delay' : 70 , 'btn' : 'wait'},
    {'delay' : 3 , 'btn' : 'chat'},
    {'delay' : 3 , 'btn' : 'chat6'},
]

action['move_doin'] = [
    {'delay' : 3 , 'btn' : 'map'},
    {'delay' : 3 , 'btn' : 'map-btn2'},
    {'delay' : 3 , 'btn' : 'map-sm'},
    {'delay' : 3 , 'btn' : 'map-b-doin'},
    {'delay' : 3 , 'btn' : 'map2-walk'},
    {'delay' : 60 , 'btn' : 'wait'},
]

action['move_hunt'] = [
    {'delay' : 3 , 'btn' : 'menu6'},
    {'delay' : 3 , 'btn' : 'dungeon'},
    {'delay' : 3 , 'btn' : 'ground'},
    {'delay' : 3 , 'btn' : 'ground1-9'},
    {'delay' : 3 , 'btn' : 'ground2-2'},
    {'delay' : 3 , 'btn' : 'ground-map'},
    {'delay' : 3 , 'btn' : 'map2-move'},
    {'delay' : 3 , 'btn' : 'map-move-yes'},
    {'delay' : 10 , 'btn' : 'wait'},
    {'delay' : 3 , 'btn' : 'auto'},
    {'delay' : 3 , 'btn' : 'follow'},
]

l = []
l.append({'delay' : 3 , 'btn' : 'doin-npc'})
l.append({'delay' : 3 , 'btn' : 'doin-npc-btn1'})
l.append({'delay' : 3 , 'btn' : 'doin-npc-sinsu1'})
for i in range(1,15): l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-hp'})
for i in range(1,15): l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-mp'})
l.append({'delay' : 3 , 'btn' : 'exit-normal'})    
action['sell_expr1'] = l

l = []
l.append({'delay' : 3 , 'btn' : 'doin-npc'})
l.append({'delay' : 3 , 'btn' : 'doin-npc-btn1'})
l.append({'delay' : 3 , 'btn' : 'doin-npc-sinsu1'})
for i in range(1,25): l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-mp'})
for i in range(1,5): l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-hp'})
l.append({'delay' : 3 , 'btn' : 'exit-normal'})    
action['sell_expr2'] = l

l = []
l.append({'delay' : 3 , 'btn' : 'doin-npc'})
l.append({'delay' : 3 , 'btn' : 'doin-npc-btn1'})
l.append({'delay' : 3 , 'btn' : 'doin-npc-sinsu1'})
for i in range(1,20): l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-hp'})
for i in range(1,10): l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-mp'})
l.append({'delay' : 3 , 'btn' : 'exit-normal'})    
action['sell_expr3'] = l

l = []
l.append({'delay' : 3 , 'btn' : 'doin-npc'})
l.append({'delay' : 3 , 'btn' : 'doin-npc-btn1'})
l.append({'delay' : 3 , 'btn' : 'doin-npc-sinsu1'})
for i in range(1,25): l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-hp'})
for i in range(1,5): l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-mp'})
l.append({'delay' : 3 , 'btn' : 'exit-normal'})    
action['sell_expr4'] = l


def hunt() :
    l = []
    l.append({'delay' : 3 , 'btn' : 'ski5'})

    # 대장간으로!
    l.append({'delay' : 10 , 'btn' : 'wait'})
    l.append({'delay' : 3 , 'btn' : 'map'})
    l.append({'delay' : 3 , 'btn' : 'map-btn2'})
    l.append({'delay' : 3 , 'btn' : 'map-sm'})
    l.append({'delay' : 3 , 'btn' : 'map-b-weapon'})
    l.append({'delay' : 3 , 'btn' : 'map2-walk'})

    # 걸어가는중...
    l.append({'delay' : 25 , 'btn' : 'wait'})
    l.append({'delay' : 3 , 'btn' : 'chat'})
    l.append({'delay' : 3 , 'btn' : 'chat6'})

    # 도인의 집으로!
    l.append({'delay' : 3 , 'btn' : 'map'})
    l.append({'delay' : 3 , 'btn' : 'map-btn2'})
    l.append({'delay' : 3 , 'btn' : 'map-sm'})
    l.append({'delay' : 3 , 'btn' : 'map-b-doin'})
    l.append({'delay' : 3 , 'btn' : 'map2-walk'})

    l.append({'delay' : 40 , 'btn' : 'wait'})
    l.append({'delay' : 3 , 'btn' : 'doin-npc'})
    l.append({'delay' : 3 , 'btn' : 'doin-npc-btn2'})
    l.append({'delay' : 3 , 'btn' : 'doin-npc-sinsu1'})
    
    # 체력 클릭
    for i in range(1,30):
        l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-hp'})
    for i in range(1,30):
        l.append({'delay' : 0 , 'btn' : 'doin-npc-sinsu-mp'})
    l.append({'delay' : 3 , 'btn' : 'exit-normal'})    

    #사냥터이동
    l.append({'delay' : 3 , 'btn' : 'menu6'})
    l.append({'delay' : 3 , 'btn' : 'dungeon'})
    l.append({'delay' : 3 , 'btn' : 'ground'})
    l.append({'delay' : 3 , 'btn' : 'ground1-9'})
    l.append({'delay' : 3 , 'btn' : 'ground2-2'})
    l.append({'delay' : 3 , 'btn' : 'ground-map'})
    l.append({'delay' : 3 , 'btn' : 'map2-move'})
    l.append({'delay' : 3 , 'btn' : 'map-move-yes'})

    l.append({'delay' : 10 , 'btn' : 'wait'})
    l.append({'delay' : 3 , 'btn' : 'auto'})
    l.append({'delay' : 3 , 'btn' : 'follow'})
    return l;