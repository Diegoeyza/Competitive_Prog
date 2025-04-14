from sys import stdin
import io
import math
from itertools import combinations
stdin = io.StringIO("""500
42
18468
6335
26501
19170
15725
11479
29359
26963
24465
5706
28146
23282
16828
9962
492
2996
11943
4828
5437
32392
14605
3903
154
293
12383
17422
18717
19719
19896
5448
21727
14772
11539
1870
19913
25668
26300
17036
9895
28704
23812
31323
30334
17674
4665
15142
7712
28254
6869
25548
27645
32663
32758
20038
12860
8724
9742
27530
779
12317
3036
22191
1843
289
30107
9041
8943
19265
22649
27447
23806
15891
6730
24371
15351
15007
31102
24394
3549
19630
12624
24085
19955
18757
11841
4967
7377
13932
26309
16945
32440
24627
11324
5538
21539
16119
2083
22930
16542
4834
31116
4640
29659
22705
9931
13978
2307
31674
22387
5022
28746
26925
19073
6271
5830
26778
15574
5098
16513
23987
13291
9162
18637
22356
24768
23656
15575
4032
12053
27351
1151
16942
21725
13967
3431
31108
30192
18008
11338
15458
12288
27754
10384
14946
8910
32210
9759
24222
18589
6423
24947
27507
13031
16414
29169
901
32592
18763
1656
17411
6360
27625
20538
21549
6484
27596
4042
3603
24351
10292
30837
9375
11021
4597
24022
27349
23200
19669
24485
8282
4735
54
2000
26419
27939
6901
3789
18128
468
3729
14894
24649
22484
17808
2422
14311
6618
22814
9515
14310
7617
18936
17452
20601
5250
16520
31557
22799
30304
6225
11009
5845
32610
14990
32703
3196
20486
3094
14344
30524
1588
29315
9504
7449
25201
13459
6619
20581
19797
14799
15282
19590
20799
28010
27158
20473
23623
18539
12293
6039
24180
18191
29658
7959
6192
19816
22889
19157
11512
16203
2635
24273
20056
20329
22647
26363
4887
18876
28434
29870
20143
23845
1417
21882
31999
10323
18652
10022
5700
3558
28477
27893
24390
5076
10713
2601
2511
21004
26870
17862
14689
13402
9790
15256
16424
5003
10586
24183
10286
27089
31427
28618
23758
9833
30933
4170
2155
25722
17190
19977
31330
2369
28693
21426
10556
3435
16550
7442
9513
30146
18061
21719
3754
16140
12424
16280
25997
16688
12530
22550
17438
19867
12950
194
23196
3298
20417
28287
16106
24489
16283
12456
25735
18115
11702
31317
20672
5787
12264
4314
24356
31186
20054
913
10809
1833
20946
4314
27757
28322
19559
23647
27983
482
4145
23197
20223
7130
2162
5536
20451
11174
10467
12045
21660
26293
26440
17254
20025
26155
29511
4746
20650
13187
8314
4475
28023
2169
14019
18788
9906
17959
7392
10203
3626
26478
4415
9315
25825
29335
25875
24373
20160
11834
28071
7488
28298
7519
8178
17774
32271
1764
2669
17193
13986
3103
8481
29214
7628
4803
4100
30528
2626
1544
1925
11024
29973
13062
14182
31004
27433
17506
27594
22726
13032
8493
143
17223
31287
13065
7901
19188
8361
22414
30975
14271
29171
236
30834
19712
25761
18897
4668
7286
12551
141
13695
2696
21625
28020
2126
26577
21695
22659
26303
17372
22467
4679
22594
23852
25485
1019
28465
21120
23153
2801
18088
31061
1927
9011
4758
32171
20316
9577
30228
12044
22759
7165
5110
7883
17087
29566
3488
29578
14475
2626
25628
5630
31929
25424
28521
6903
14963
124
24597
3738
13262
10196
32526

""")

def construct_seq(limit,memo=False):
    seq=[[],[]]
    if memo:
        pass
    else:
        i=0
        while (len("".join(seq[0]))<limit):
            s=""
            if i==0:
                s="1"
                seq[0].append(s)
                seq[1]="1"
            else:
                s=seq[0][i-1]+str(int(seq[1])+1)
                seq[0].append(s)
                seq[1]=str(int(seq[1])+1)
            i+=1
    return seq
    

    


cases = int(stdin.readline().strip())
for i in range (cases):
    case=int(stdin.readline().strip())
    conc="".join(construct_seq(case)[0])
    #print("".join(construct_seq(case-1)[0]))
    print(conc[case-1])
    

    