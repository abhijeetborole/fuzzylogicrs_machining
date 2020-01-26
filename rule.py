file1 = open("D:\DocumentsInt\\rules.txt","w+")
for h in ['soft','hard']:
    for s in ['slow','medium','fast']:
        for w in ['narrow','medium','wide']:
            for f in ['small','medium','large']:
                for a in ['less','medium','high']:
                    print('Enter Data for '+h+' hardness, '+s+' speed, '+w+' width, '+f+' feed, '+a+' amr')
                    v = input("Enter VB:")
                    rule1 = "rule = ctrl.Rule(hardness['"+h+"'] & speed['"+s+"']&width['"+w+"']&feed['"+f+"']&amr['"+a+"'],vb['"+v+"'])"
                    file1.write(rule1+"\n")
                    fc = input("Enter avgstatcutforce:")
                    rule2 = "rule = ctrl.Rule(hardness['"+h+"'] & speed['"+s+"']&width['"+w+"']&feed['"+f+"']&amr['"+a+"'],avgstatcutforce['"+fc+"'])"
                    file1.write(rule2+"\n")
                    df = input("Enter avgdynfeedforce:")
                    rule3 = "rule = ctrl.Rule(hardness['"+h+"'] & speed['"+s+"']&width['"+w+"']&feed['"+f+"']&amr['"+a+"'],avgstatcutforce['"+df+"'])"
                    file1.write(rule3+"\n")
                    sce = input("Enter sceenergy:")
                    rule4 = "rule = ctrl.Rule(hardness['"+h+"'] & speed['"+s+"']&width['"+w+"']&feed['"+f+"']&amr['"+a+"'],scenergy['"+sce+"'])"
                    file1.write(rule4+"\n")

file1.close()