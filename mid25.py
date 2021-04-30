while(1):
    s = input("檢測的字串(end結束):")
    if s == "end":
        print("檢測結束")
        break
    w = input("檢測的單一字元:")
    print("字元%s出現次數為:%d" %(w,s.count(w)))