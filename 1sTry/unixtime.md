# 13位数字表示的时间还原  
解决步骤：  
1. 搜索13位时间，有13位时间戳转换。    
2. 试着在http://shijianchuo.911cha.com/转换了一下，结果正确。  
3. 该页面上有UNIX时间戳字样。下面有不同语言获取时间戳提示：  
> Python时间戳  
> 先import time 然后time.time()    

4. 到命令行试行，生效。  
5. 重新搜索“python批量读取unix时间戳”，进入http://www.jb51.net/article/66167.htm，发现解释了何谓“UNIX时间戳”：  
> Unix timestamp：是从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数，不考虑闰秒。  

怪不得网站上很多时间不对的地方经常显示为“1970年1月1日”，原来是这种归零。  