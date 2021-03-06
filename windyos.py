import numpy as np
def inputs():#takes inputs
    for i in range(pr_num):
        print()
        j=str(i+1)
        proc.append('P'+j)
        arr = int(input(f"Arrival Time for process P{i+1} ->"))
        if arr>=0:
            bur = int(input(f"Burst Time for process P{i+1} ->"))
            if bur>=0:
                arr_tim.append(arr)
                bur_tim.append(bur)
            else:
                print("INVALID INPUT")
        else:
            print("INVALID INPUT")
        
def initt():#given table
    print("Given values are ->\n")
    print()
    print("\t\t\t\t\tPROCESS\t\t\t\t\tARRIVAL TIME\t\t\tBURST TIME")
    for i in range(pr_num):
        print()
        print("\t\t\t\t\t ",proc[i],"\t\t\t\t\t  ",arr_tim[i],"\t\t\t\t ",bur_tim[i])

def exe():
    burr=0
    k=0
    for i in range(pr_num):
        burr = burr+bur_tim[i]
        min = bur_tim[i]
        k+=1
        for j in range(k,pr_num):
            if burr>=arr_tim[i] and bur_tim[i]<min :
                bur_tim[j],bur_tim[k] = bur_tim[k],bur_tim[j]
                arr_tim[j],arr_tim[k] = arr_tim[k],arr_tim[j]
                proc[j],proc[k] = proc[k],proc[j]

def waitndturn():#wait and turn around time
    val=0
    tem=0
    tuar_final=0
    wait_fin=0
    for i in range(1,pr_num):
        val += bur_tim[i-1]
        wait_tim[i] = val - arr_tim[i]
        wait_fin += wait_tim[i]
    wait_avg = wait_fin/pr_num
    for i in range(pr_num):
        tem += bur_tim[i]
        tuar_tim.append(tem - arr_tim[i])
        tuar_final += tuar_tim[i]
    tuar_avg = tuar_final/pr_num
    print("\nDetailed View of Table ->")
    print("PROCESS\t\t\t\t\tARRIVAL TIME\t\t\tBURST TIME\t\t\t\tWAITING TIME\t\t\t\tTURN AROUND TIME")
    for i in range(pr_num):
        print()
        print(proc[i],"\t\t\t\t\t  ",arr_tim[i],"\t\t\t\t ",bur_tim[i],"\t\t\t\t\t",wait_tim[i],"\t\t\t\t\t  ",tuar_tim[i])

def priority():
    print("\nPriorities are give by :-\n")
    for i in range(1,pr_num):
        cmpl_tim[i] = cmpl_tim[i-1] + bur_tim[i]
    for j in range(pr_num):
        x= 1+wait_tim[j]/cmpl_tim[j]
        prioritie.append(x)
        print(f"P{j+1} -> %.3f"%x)

def result():#final table
    print("\n\nPROCESS\t\t\t\t\tARRIVAL TIME\t\t\tBURST TIME\t\t\t\tWAITING TIME\t\t\t\tTURN AROUND TIME")
    for i in range(pr_num):
        print()
        print(proc[i],"\t\t\t\t\t  ",arr_tim[i],"\t\t\t\t ",bur_tim[i],"\t\t\t\t\t",wait_tim[i],"\t\t\t\t\t  ",tuar_tim[i])


if __name__=="__main__":
    print("\t\t\t\t\t\t\t\t\tWELCOME TO VINITHA SCHEDULING\n\n")
    input("-----press enter to continue-----\n")
    pr_num = int(input("Give number of processes ->"))
    if pr_num == 0:
        print("No Processes")
    elif pr_num>0:
        proc=[]
        arr_tim=[]
        bur_tim=[]
        tuar_tim=[]
        prioritie=[]
        wait_tim=np.zeros(pr_num,dtype=int)
        cmpl_tim=np.zeros(pr_num,dtype=int)
        inputs()
        initt()
        exe()
        waitndturn()
        cmpl_tim[0]=bur_tim[0]
        #priority = 1 + waiting time / estimated run time
        priority()
        result()
    else:
        print("INVALID INPUT")
    print("\n\n")
    print("\t\t\t\t\t\t\t\t\t\tTHANK YOU ")
    input()
