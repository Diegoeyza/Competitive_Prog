import math
from sys import stdin
import io

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def get_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i: 
                factors.append(n // i)
    return factors

def min_sum_lcm(n):
    factors = get_factors(n)
    min_sum = [float('inf')]
    memo = {} 

    def backtrack(start, current_set, current_lcm):
        current_sum = sum(current_set)

        if current_sum >= min_sum[0]:
            return

        if current_lcm > n:
            return

        if current_lcm == n:
            min_sum[0] = min(min_sum[0], current_sum)
            return
        memo_key = (start, current_lcm)
        if memo_key in memo and memo[memo_key] <= current_sum:
            return
        memo[memo_key] = current_sum

        for i in range(start, len(factors)):
            next_factor = factors[i]
            new_lcm = lcm(current_lcm, next_factor)
            backtrack(i + 1, current_set + [next_factor], new_lcm)
    backtrack(0, [], 1)

    if min_sum[0] == n:
        min_sum[0] += 1
    if min_sum[0] ==0:
        min_sum[0] =2
    
    return min_sum[0]

# # stdin = io.StringIO("""527737240
# 1646067777
# 1132730035
# 150867131
# 1970613182
# 1178302920
# 153145790
# 158336005
# 1405450792
# 1027604424
# 1132669803
# 1875637929
# 1154956630
# 70921391
# 1022785618
# 1327538778
# 1846304759
# 1498545328
# 541670059
# 1914278404
# 2096658159
# 660987852
# 1980107505
# 1309893938
# 1809152134
# 738890012
# 673867261
# 1201578928
# 959940966
# 1025263350
# 75898294
# 187814113
# 1686594741
# 1901096228
# 292978149
# 341866407
# 1828666873
# 522071391
# 1513660873
# 1143067468
# 1728747767
# 574238667
# 1113123768
# 959766465
# 1387852820
# 218485006
# 2009398970
# 759391696
# 698836443
# 807108477
# 218405492
# 1347786955
# 1213423693
# 865087060
# 2022502072
# 1603860156
# 372012233
# 1975127268
# 1476764092
# 1231294920
# 1506332228
# 1752772207
# 1429907920
# 1860784468
# 1875794174
# 1861054218
# 1669921488
# 524046170
# 892711951
# 1832393264
# 131752942
# 2123177417
# 1655675885
# 1150273529
# 191282764
# 1374348505
# 513326081
# 1630133904
# 1370232841
# 276941248
# 630653686
# 10283523
# 1905076017
# 481650280
# 619957782
# 398850848
# 1201677560
# 1649344668
# 1998387935
# 1440567263
# 762974747
# 1258285452
# 24540314
# 1327038349
# 1609555163
# 1847893449
# 456613389
# 181348439
# 1461180073
# 68255355
# 995211281
# 122534255
# 1203316609
# 610367624
# 98289883
# 997280531
# 1597363631
# 1232287832
# 1604562245
# 1111430626
# 59674614
# 444983220
# 727109008
# 243426499
# 1605567464
# 1373876638
# 92297413
# 1121401050
# 465929461
# 811586740
# 1920947036
# 654539175
# 1450544083
# 326558955
# 881801357
# 1210078769
# 2077965432
# 370437066
# 158317042
# 1750788976
# 95025559
# 1289454595
# 1030642921
# 303077858
# 1941572831
# 1258231048
# 690139725
# 1216180861
# 1928250406
# 472814318
# 1103862780
# 688886108
# 1522456996
# 649271395
# 555334835
# 223578290
# 2029547802
# 1594524722
# 997641257
# 1893280707
# 132654750
# 1632457077
# 710754282
# 864314924
# 1983268832
# 1887552410
# 464064638
# 53138161
# 1041177136
# 1945479370
# 1326014681
# 1291531497
# 453851682
# 493107401
# 931054203
# 619284383
# 348696611
# 2033302394
# 1039460974
# 1136014298
# 767113826
# 2066815101
# 702948728
# 25651914
# 1604222129
# 1375931535
# 932321978
# 1443997030
# 1962955867
# 80950311
# 1126014024
# 1042051930
# 685839533
# 445861335
# 1026262481
# 1589222036
# 1788275876
# 2080560848
# 1880173644
# 872887621
# 328497984
# 1723782573
# 458135369
# 213523280
# 867965961
# 69049896
# 2060354750
# 1730522356
# 2089284055
# 214728599
# 1831771511
# 1034875836
# 1047918570
# 827431311
# 2065768604
# 434137081
# 932101247
# 1814843050
# 1926889272
# 1405569239
# 1627196761
# 624822365
# 821292171
# 402251200
# 1479784903
# 587809327
# 1420498991
# 975744889
# 2027712347
# 1556303364
# 868605399
# 2010844321
# 252606262
# 1616826783
# 448324594
# 1538925679
# 1601922516
# 154372786
# 299904400
# 1623072642
# 1461478528
# 1705699731
# 1637760571
# 1197505471
# 2030609168
# 744941624
# 282316435
# 1081042243
# 232025951
# 1691750285
# 176746892
# 136475051
# 95617414
# 1516171490
# 275310766
# 621685728
# 700972828
# 671623220
# 808675099
# 930368965
# 844459124
# 2018274996
# 1641363202
# 222866004
# 325757821
# 30928751
# 470205162
# 335073530
# 1163819058
# 2033166817
# 925645657
# 575404083
# 149327433
# 2051987499
# 1214291765
# 747620357
# 1720518644
# 1345044407
# 214182181
# 2117434847
# 1688616815
# 713568222
# 691573640
# 697752358
# 1171166427
# 574283310
# 223712029
# 824433397
# 1382845871
# 358591127
# 1909842027
# 288981246
# 112293948
# 233901754
# 1916791161
# 809968858
# 1374359411
# 429966525
# 2126072812
# 1735240740
# 1168782496
# 1072304215
# 421138866
# 63515872
# 1809204691
# 764984702
# 1620259455
# 495060465
# 2115147068
# 368618540
# 0""")

input_value = int(stdin.readline().strip())
case=1
while input_value != 0:
    print(f"Case {case}: {min_sum_lcm(input_value)}")
    case+=1

    input_value = int(stdin.readline().strip())