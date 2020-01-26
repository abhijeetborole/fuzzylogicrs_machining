file1 = open("D:\DocumentsInt\\rules.txt","w+")
for h in ['soft','hard']:
    for s in ['slow','medium','fast']:
        for w in ['narrow','medium','wide']:
            for f in ['small','medium','large']:
                for a in ['less','medium','high']:
                    print('Enter Data for '+h+' hardness, '+s+' speed, '+w+' width, '+f+' feed, '+a+' amr')
                    v = input("Enter VB:")
                    rule1 = "rule = ctrl.Rule(hardness['"+h+"'] & speed['"+s+"']&width['"+w+"']&feed['"+f+"']&amr['"+a+"'],vb['"+v+"'])"
                    print(rule1)
                    file1.write(rule1)
                    file1.close()
