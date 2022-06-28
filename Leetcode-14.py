if __name__ == '__main__':
    strs = list(map(str,input().split()))
    print(strs)
    for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if len(strs[i])>len(strs[j]):
                    strs[i],strs[j] = strs[j],strs[i]
    s = len(strs[0])
    s1 = 0
    ss = ''
    son1 = 0
    mantiq = True
    for i in range(s):
        son1 = 0
        for j in range(1,len(strs)):
          if strs[0][s1] == strs[j][s1]:
              son1+=1 
          else:
              mantiq = False
              break
        if son1 == len(strs)-1:
            ss += strs[0][s1]
        if not(mantiq):
            break
        s1+=1
    print(ss)