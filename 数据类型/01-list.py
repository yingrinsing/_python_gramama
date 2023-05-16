#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017-9-26

@author: yingrinsing
@github: git@github.com:yingrinsing/python_grammar.git
@copyright: Apache License, Version 2.0
"""


import laok
from pprint import pprint
#===============================================================================
# 
#===============================================================================
#<type 'list'>
#builtin-method---->
    #append [<type 'builtin_function_or_method'>] [L.append(object) -- append object to end]
    #count [<type 'builtin_function_or_method'>] [L.count(value) -> integer -- return number of occurrences of value]
    #extend [<type 'builtin_function_or_method'>] [L.extend(iterable) -- extend list by appending elements from the iterable]
    #index [<type 'builtin_function_or_method'>] [L.index(value, [start, [stop]]) -> integer -- return first index of value.  Raises ValueError if the value is not present.]
    #insert [<type 'builtin_function_or_method'>] [L.insert(index, object) -- insert object before index]
    #pop [<type 'builtin_function_or_method'>] [L.pop([index]) -> item -- remove and return item at index (default last).  Raises IndexError if list is empty or index is out of range.]
    #remove [<type 'builtin_function_or_method'>] [L.remove(value) -- remove first occurrence of value.  Raises ValueError if the value is not present.]
    #reverse [<type 'builtin_function_or_method'>] [L.reverse() -- reverse *IN PLACE*]
    #sort [<type 'builtin_function_or_method'>] [L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;  cmp(x, y) -> -1, 0, 1]
def interaction():
    list1 = [1,2,4,6,8]
    list2 = [1,2,3,5,7]
    interaction1 = list(set(list1).intersection(set(list2)))
    print 'interaction1:'
    print interaction1
    interaction2 = [x for x in list1 if x in list2]
    print 'interaction2:'
    print interaction2
    
    
def union():
    list1 = [1,2,4,6,8]
    list2 = [1,2,3,5,7]
    union1 = list(set(list1).union(set(list2)))
    print 'union1:'
    print union1
    #union2 = list2.extend([v for v in list1])
    list1.extend(list2)
    print 'union2:'
    print list(set(list1))


def difference():
    list1 = [1,2,4,6,8]
    list2 = [1,2,3,5,7]
    #list1和list2均不同的元素
    d1 = list(set(list1) ^ set(list2))
    print 'difference1:'
    print d1  
    #list1有list2没有
    d2 = list(set(list1).difference(set(list2))) 
    print 'difference2:'
    print d2   
    d3 = [v for v in list1 if v not in list2]
    print 'difference3:'
    print d3  


def multi_same_string():
    num_list = [1 for i in range(5)]
    print num_list    


def sort1():
    list1 = [1,2,7,6,8]
    list1.sort()
    print list1


if __name__ == '__main__':
    #laok.lktest_run()#catch_except = True
    #interaction()
    #union()
    #difference()
    #multi_same_string()
    #sort1()
    lit1 = []
    try:
        print lit1[0]
    except IndexError:
        print 'error'
    a = ["5xn3ibtmgysxzb4", "5xaiave6dcfiakm", "5xf6q2bzu6mxeqc", "5x568imkc4nsws6", "5xbjd37gprseia4", "5xewbb6iqdvzymy", "5xh9ag2umn5bgvi", "5xcsdkkgyp2hq9y", "5xhfbct6ekv4rq2", "5xjeqgvz87wcnpc", "5xe4k34uhqfrc82", "5x7qxfat8a4xpk4", "5xdfadzkdsu3ezm", "5x9hmk6fty235dc", "5x58dbnm99ee2a4", "5xartyh3ddsi3uc", "5xvgb4knaymq5hy", "5x6nxr4dgennaei", "5xsbni3a7advbje", "5xd7ztn35zh26wk", "5xchsmxxfvf7ajw", "5xri2a9v2wmuk2y", "5xbf49p8wy869ew", "5xdef4fabiyugfi", "5xcb5yb72bi989e", "5xer8k8vwiznrwk", "5xjxsa9x95pkt72", "5xu8h37p27j67xi", "5xwrcfckhcz6rqa", "5xmdtsnyvgdw6d9", "5xhan6erq55urea", "5x6ifz4hezz46vy", "5xwpbynk9jnmeua", "5xeaeza4fbcrrp9", "5xj9ybxct72zg84", "5x6b3bf9csha99k", "5xtgkp7sziehjx4", "5xqa29hgr2a88zy", "5xu5g2z2vh96iss", "5xqvgtzsnvyyew4", "5xw9yv5sr2xws2g", "5xeae292ehir3ky", "5xsj7q2bdagu7n4", "5xxq8wu2b3abkna", "5xhqsybz9zwdsxa", "5xzrj9nckdph9k4", "5xinbgdj9cyzjbk", "5xgwcrqiv8rqzt6", "5xfce99qhz8kfwq", "5xrkwj52iiyzxq9", "5xwqjtk4ka6phi6", "5xjynnsuz8bu7ym", "5xt27gckt62rvz2", "5xt3y8sswb4q8yw", "5xew3etn63nh8cy", "5xgrngkeiuyymzy", "5xz9am75umdgkaq", "5xz5fhuhkryr5qg", "5xrfccctcftiaxe", "5x7vctc22b8hnrk", "5xb6umn5m9cp8ru", "5xkr79xk99jnk52", "5xvp55cpwsfyjhs", "5xqxruu9jue9qqc", "5xdd99qn2xcdpng", "5xmk6gzcqpv3nci", "5x8tf2n6m47rkgs", "5xcafbcn2yfn8m9", "5x9km28rkm8rzbk", "5xacb224am73hfe", "5xx3vcetekka3am", "5xm2wf9ietmyhxg", "5xhf68qwuggvh86", "5xavwrwajau9q4c", "5x26wbthzbrc7ya", "5xrbrts3g5edmum", "5xz7iajtzttdz69", "5xa3xzxz4geamt2", "5x7q5etzvjvijma", "5x5xkmuut6ym5gm", "5xkacp955mk6j4k", "5xr4z327nru3s4m", "5xpzasvexttmugc", "5xigamf6e9zmhwe", "5x27gk2fsdmwux9", "5x6a2tugkw9zim9", "5xr2iqy53mxb33e", "5xf7hukr77uqkam", "5x6zk2xmzub4kca", "5xkt56cipmkw4ic", "5xjs4ju62fguf2e", "5x3mwtzm2qh54g6", "5x7z27qq4p5tdbe", "5xwmcr66xp6vria", "5x99ac3k5ptsrwm", "5x3n5wscdrw2mhm", "5xts72ghgzpkja2", "5xdatnd4eehp6e9", "5xwfkiqq4g2tb3e", "5xdrvvqespzrja4", "5xmvxm3xk98g6qk", "5xfga3rjajr33gk", "5xgfwty7eci67sw", "5x3xii6983eh7nm", "5xqwpanrubxdw4q", "5x2gghmnyjmedbe", "5xixngta4que3fg", "5xznxzn3bxbiijq", "5x8vf2rtjihenyc", "5xvag92hpn2du3k", "5xbhpet4gcw3fgi", "5x344iryvskten6", "5xdab2xftd682am", "5xbry5kh4pyh3jg", "5xiza7sqptzfkxw", "5x2j4axghx8ufj9", "5xc3aizxuj23c59", "5xbuybc9jasbn72", "5x5er83m42nyzpw", "5xkqwpmcze65zmw", "5xcqmwimw5hmk7s", "5xzgvm76y6pavum", "5xssrd77nsnhfqu", "5xhg8zdy6niivvu", "5xs9zyxy67mknhc", "5xtxdme8swwrnfm", "5x8pz369c6re6a2", "5xgtk5tj3p5vs32", "5xzd69sfu3v6g6c", "5xg3bydkywvfubq", "5xku5ppnirgp3n9", "5xqqrajanwsz3n4", "5x5sc7cxnmemgua", "5xr6j24tia8tpzs", "5xhigqdssdst386", "5xgvgavjb3mb23c", "5xvjegdqeyb4zji", "5xizpvtdhyenfmu", "5xdkaqkr8zuj2gy", "5xqpq5f4eur92fe", "5xs4sj78c55gzsw", "5xg88rj462exe7y", "5xzaws6q5hbb96w", "5xn3vbjm9ic5c7w", "5xrwz3cucjuuarq", "5xii3t2iq6hjcx2", "5xzmk5ifqt4t7je", "5xe8sikf3jgrdzw", "5xppnqz545szpza", "5x8izmfq73et822", "5xeijvr8377xevg", "5xm58ugk32cm5gi", "5xvpkxhwawf8bwk", "5xp2pvy82bp28g6", "5x8422ax9sxt72u", "5xr7z8cgtstcpqi", "5xeu6rca54d4ibs", "5x6ymef5kvq5i7e", "5xv5qistx9vtxvq", "5xmm69y785qi3we", "5x6596ju7hmurfm", "5xa24jwx4wkqfuk", "5x5zp8p2pq5sdka", "5x6ivgfgkuqec8m", "5x842ku6mu8fd5e", "5xyabhgchcg6agg", "5x9brbcenm7u8ss", "5xijabd9id94hmm", "5xp9n6d8qgdkbd2", "5xe4iv2xapdupbc", "5x3jnir84y2dws4", "5xn3cq2w4k3224u", "5xfgv4hf3swix3e", "5xnwvs9w63quf5a", "5xswh52n9tcair6", "5xt2g8am6epdcqc", "5xxvhggbyxk7p26", "5xw5abi6saxvyec", "5x3xc99nvvxy9x9", "5xzf434ukxmr7bk", "5xjyb3zr7i9z8aq", "5x5sety35cirk6q", "5x4gugkpzfhess9", "5xpv6ynwhkreghs", "5xdsrja68p2nma2", "5x63jawtkystjpm", "5x9cqntutmesz56", "5xwwfvj4rk43m9g", "5x7w66fndd5b4n2", "5xxzgrz9t4husdc", "5x46yu36jehvizu", "5xbfxnf8su67wg2", "5xue675kg7xmb2k", "5xi4c2is67ezreu", "5xikta38h2dfwk4", "5xefg7jzz5au874", "5xauhnsp77knrw9", "5xrn42f4sndxabe", "5xbqe9f6fdbi9ek", "5x32bqtuumkdgdy", "5x6a5h2s5xybe8s", "5xyzctvbxu8a7n6", "5x7ziuxwjb3wh9i", "5xxiqpk56t4hxca", "5xg56cbpkthdvns", "5xs8p4cwq4xgsbg", "5x5bipaw8ytqt46"]
    print(len(a))
    b = ["5xn3ibtmgysxzb4", "5xaiave6dcfiakm", "5xf6q2bzu6mxeqc", "5x568imkc4nsws6", "5xbjd37gprseia4",
         "5xewbb6iqdvzymy", "5xh9ag2umn5bgvi", "5xcsdkkgyp2hq9y", "5xhfbct6ekv4rq2", "5xjeqgvz87wcnpc",
         "5xe4k34uhqfrc82", "5x7qxfat8a4xpk4", "5xdfadzkdsu3ezm", "5x9hmk6fty235dc", "5x58dbnm99ee2a4",
         "5xartyh3ddsi3uc", "5xvgb4knaymq5hy", "5x6nxr4dgennaei", "5xsbni3a7advbje", "5xd7ztn35zh26wk",
         "5xchsmxxfvf7ajw", "5xri2a9v2wmuk2y", "5xbf49p8wy869ew", "5xdef4fabiyugfi", "5xcb5yb72bi989e",
         "5xer8k8vwiznrwk", "5xjxsa9x95pkt72", "5xu8h37p27j67xi", "5xwrcfckhcz6rqa", "5xmdtsnyvgdw6d9",
         "5xhan6erq55urea", "5x6ifz4hezz46vy", "5xwpbynk9jnmeua", "5xeaeza4fbcrrp9", "5xj9ybxct72zg84",
         "5x6b3bf9csha99k", "5xtgkp7sziehjx4", "5xqa29hgr2a88zy", "5xu5g2z2vh96iss", "5xqvgtzsnvyyew4",
         "5xw9yv5sr2xws2g", "5xeae292ehir3ky", "5xsj7q2bdagu7n4", "5xxq8wu2b3abkna", "5xhqsybz9zwdsxa",
         "5xzrj9nckdph9k4", "5xinbgdj9cyzjbk", "5xgwcrqiv8rqzt6", "5xfce99qhz8kfwq", "5xrkwj52iiyzxq9",
         "5xwqjtk4ka6phi6", "5xjynnsuz8bu7ym", "5xt27gckt62rvz2", "5xt3y8sswb4q8yw", "5xew3etn63nh8cy",
         "5xgrngkeiuyymzy", "5xz9am75umdgkaq", "5xz5fhuhkryr5qg", "5xrfccctcftiaxe", "5x7vctc22b8hnrk",
         "5xb6umn5m9cp8ru", "5xkr79xk99jnk52", "5xvp55cpwsfyjhs", "5xqxruu9jue9qqc", "5xdd99qn2xcdpng",
         "5xmk6gzcqpv3nci", "5x8tf2n6m47rkgs", "5xcafbcn2yfn8m9", "5x9km28rkm8rzbk", "5xacb224am73hfe",
         "5xx3vcetekka3am", "5xm2wf9ietmyhxg", "5xhf68qwuggvh86", "5xavwrwajau9q4c", "5x26wbthzbrc7ya",
         "5xrbrts3g5edmum", "5xz7iajtzttdz69", "5xa3xzxz4geamt2", "5x7q5etzvjvijma", "5x5xkmuut6ym5gm",
         "5xkacp955mk6j4k", "5xr4z327nru3s4m", "5xpzasvexttmugc", "5xigamf6e9zmhwe", "5x27gk2fsdmwux9",
         "5x6a2tugkw9zim9", "5xr2iqy53mxb33e", "5xf7hukr77uqkam", "5x6zk2xmzub4kca", "5xkt56cipmkw4ic",
         "5xjs4ju62fguf2e", "5x3mwtzm2qh54g6", "5x7z27qq4p5tdbe", "5xwmcr66xp6vria", "5x99ac3k5ptsrwm",
         "5x3n5wscdrw2mhm", "5xts72ghgzpkja2", "5xdatnd4eehp6e9", "5xwfkiqq4g2tb3e", "5xdrvvqespzrja4",
         "5xmvxm3xk98g6qk", "5xfga3rjajr33gk", "5xgfwty7eci67sw", "5x3xii6983eh7nm", "5xqwpanrubxdw4q",
         "5x2gghmnyjmedbe", "5xixngta4que3fg", "5xznxzn3bxbiijq", "5x8vf2rtjihenyc", "5xvag92hpn2du3k",
         "5xbhpet4gcw3fgi", "5x344iryvskten6", "5xdab2xftd682am", "5xbry5kh4pyh3jg", "5xiza7sqptzfkxw",
         "5x2j4axghx8ufj9", "5xc3aizxuj23c59", "5xbuybc9jasbn72", "5x5er83m42nyzpw", "5xkqwpmcze65zmw",
         "5xcqmwimw5hmk7s", "5xzgvm76y6pavum", "5xssrd77nsnhfqu", "5xhg8zdy6niivvu", "5xs9zyxy67mknhc",
         "5xtxdme8swwrnfm", "5x8pz369c6re6a2", "5xgtk5tj3p5vs32", "5xzd69sfu3v6g6c", "5xg3bydkywvfubq",
         "5xku5ppnirgp3n9", "5xqqrajanwsz3n4", "5x5sc7cxnmemgua", "5xr6j24tia8tpzs", "5xhigqdssdst386",
         "5xgvgavjb3mb23c", "5xvjegdqeyb4zji", "5xizpvtdhyenfmu", "5xdkaqkr8zuj2gy", "5xqpq5f4eur92fe",
         "5xs4sj78c55gzsw", "5xg88rj462exe7y", "5xzaws6q5hbb96w", "5xn3vbjm9ic5c7w", "5xrwz3cucjuuarq",
         "5xii3t2iq6hjcx2", "5xzmk5ifqt4t7je", "5xe8sikf3jgrdzw", "5xppnqz545szpza", "5x8izmfq73et822",
         "5xeijvr8377xevg", "5xm58ugk32cm5gi", "5xvpkxhwawf8bwk", "5xp2pvy82bp28g6", "5x8422ax9sxt72u",
         "5xr7z8cgtstcpqi", "5xeu6rca54d4ibs", "5x6ymef5kvq5i7e", "5xv5qistx9vtxvq", "5xmm69y785qi3we",
         "5x6596ju7hmurfm", "5xa24jwx4wkqfuk", "5x5zp8p2pq5sdka", "5x6ivgfgkuqec8m", "5x842ku6mu8fd5e",
         "5xyabhgchcg6agg", "5x9brbcenm7u8ss", "5xijabd9id94hmm", "5xp9n6d8qgdkbd2", "5xe4iv2xapdupbc",
         "5x3jnir84y2dws4", "5xn3cq2w4k3224u", "5xfgv4hf3swix3e", "5xnwvs9w63quf5a", "5xswh52n9tcair6",
         "5xt2g8am6epdcqc", "5xxvhggbyxk7p26", "5xw5abi6saxvyec", "5x3xc99nvvxy9x9", "5xzf434ukxmr7bk",
         "5xjyb3zr7i9z8aq", "5x5sety35cirk6q", "5x4gugkpzfhess9", "5xpv6ynwhkreghs", "5xdsrja68p2nma2",
         "5x63jawtkystjpm", "5x9cqntutmesz56", "5xwwfvj4rk43m9g", "5x7w66fndd5b4n2", "5xxzgrz9t4husdc",
         "5x46yu36jehvizu", "5xbfxnf8su67wg2", "5xue675kg7xmb2k", "5xi4c2is67ezreu", "5xikta38h2dfwk4",
         "5xefg7jzz5au874", "5xauhnsp77knrw9", "5xrn42f4sndxabe", "5xbqe9f6fdbi9ek", "5x32bqtuumkdgdy",
         "5x6a5h2s5xybe8s", "5xyzctvbxu8a7n6", "5x7ziuxwjb3wh9i", "5xxiqpk56t4hxca", "5xg56cbpkthdvns"]
    # b = ["5x2vdsk4948wumw", "5x2wsje65y2vnww", "5xevbbyak9ivsrg", "5x64h8gfqprrd8i", "5xjuz94yiz573im", "5xuht72nc7cx2ng", "5xzgddsqgm3si5i", "5x9kfybzhksh79s", "5xuaubbvumawhy6", "5x5zxn8kwnq6vha", "5xs9jp39bmjj96s", "5x8hk7d24id6xha", "5xrzb2yrtsquvcg", "5xy6xv3m87jw4jk", "5x25x9j5bjezx5c", "5xwv62cy8pz3qnq", "5x6rsurkudv7ur2", "5x567atsnqub559", "5xv59s23anhyxzg", "5xrbgc4ypenidj6", "5xwbqraipciuipi", "5x97ig4juhtubyw", "5xhszp4gdwaesny", "5xcvcef2y5vasim", "5xxsmczf9bgthke", "5xma96su25ivqkk", "5xims68ytkwi5em", "5xe4ygfak8pd2xw", "5xutsh3getp6pb9", "5xazuz24rn4xpdq", "5xavpfsnukzpif9", "5x5hgrkes62x45g", "5xwuu8rkggmgsfy", "5xx8gcee2cauxn6", "5xxtjhhzk5xcbta", "5xaxkx4kkgbmp2c", "5x9vu2dcssbavv2", "5xz3i9ipyyb778g", "5x9ws8h4a2ue3a6", "5xa7kiqamav5sgi", "5xmrd5yqymfw6rc", "5xz62g5gpbe8qks", "5xu4ukwmiqn3srm", "5xqsfc6e6rzmrhy", "5xzzs7ttszzxyfa", "5x5ix6k3hvckq32", "5xca8dhucmh8mnk", "5xn8y7g2smnhs2i", "5x32h3kqxvh6cc9", "5xxxb6gy3km9fpg", "5xh5w542av5gcd4", "5xicgis4tpweieu", "5xcyyv23fittzec", "5xtztc9kvc5i73e", "5xqb257p6ap9xbq", "5xedxx8298wgs3u", "5xpivbzq6srfbki", "5xwdmcfwkc3yagu", "5xhvj3segrtgyhm", "5x3qgik5dv7tsdi", "5xn9trx2aprpwvk", "5x9uzrnqjqt82gg", "5xr68atbcwtxnju", "5xixvj6d5bnc429", "5xzfs9sircrdmb2", "5xhf8ugfbka77ia", "5xusu9gtxdjpyfc", "5xbcs46kbgvzhys", "5x9pqgwrj4jm55w", "5xiz3n44m3eipdc", "5xdz2ug7fgtmhw2", "5x5tbykjk9f7upy", "5x5p6xdfwkecuti", "5xrj6qh5rn2r5e6", "5xsben56ryinqfc", "5x8ie87r72qufdw", "5x5wxmqrnj94yjc", "5xhee43m9hg6kee", "5xsj25x8zxzzxcy", "5xbfx4qxjy5npvs", "5xqgjaqvitthi7a", "5xqin3iitq29tk2", "5xvja6hb7mrcmxk", "5x64gyqjnz3p6pu", "5xa7m87xnim5uqe", "5x4m7fvex9br72g", "5xx9epqqjrqmhfa", "5x8incrcdi3y4da", "5x9vrg6fn45piym", "5xf7muyrmpmx67c", "5x54qnmie7i2pti", "5x4stxgxf2scp56", "5x29a7ekpybf2cy", "5xzsfq23mje5uyg", "5xvwywjbgbgcuzs", "5xrehkx5xfuyaje", "5xhnqpkv6j42rs6", "5xuw5h2jirq5edm", "5xd3smiww47xj32", "5xm6cqjnc9vad6k", "5xj4thms7x5aafm", "5xqair6azd7m6ik", "5x345cb7ed7ndmw", "5xz9i4exj7ggy74", "5x7awbu3rkxdg9e", "5xdtweawp7jtaky", "5xt7pvp9uqpjuju", "5x4nq347y5vhike", "5xigqix638y2s6a", "5xbkht582bim3d4", "5xr643ujxutzx8g", "5xcasuvtqsv7rqu", "5xnve2pe7d3maqs", "5xzm8b7vq9s6n66", "5xuxfeq6jibmsri", "5xti3e2xaugjais", "5xa4sgcpa8hdf3g", "5xhzfyra5fzvgdk", "5xsxmyakzk4f3qi", "5xdcva9wtr2vzfs", "5xxp8kd4rjeyrys", "5xe8kug3w3rs25q", "5x47bzawfxg7uxk", "5x859tig9xkwznk", "5xb4tgakvvn3en9", "5xkiihi3fgsrkja", "5xrqerrjjnihbfq", "5xti2tqxe55batg", "5xqdfeesuajhfbw", "5xvhdbsn78aw4sg", "5xgbhci2g66d2ia", "5xq3g2cuge4eezw", "5xf3t63inn5cc54", "5xqxwj3muc9b4yg", "5x7siqye3aqxzjg", "5xpny9qdyvahzv9", "5x3f2ye8d8sb5va", "5xquf28n8hzdfvy", "5xcwm4uevuvikuy", "5xjxbev222m6rzi", "5xwimdsnw6jdtci", "5xpszu4kcih7brw", "5xmkmm7mz2uyrds", "5xima3gdikny6m9", "5xfj52nepv76saq", "5xhwp2kf8j856he", "5xpszskbsbyur2m", "5xs3jeuufv9fyi6", "5x7avehnpmjs2uq", "5xbxnk4ts8z4q49", "5xzfipvk6y3gidk", "5xgdjzugnrfw2bi", "5x295bucsszw652", "5xskjiii9a6igc6", "5xrw3zi27yx3bzi", "5xqu6ejfma2qbwq", "5xuawhpqfj5wjk6", "5x2twejnk3ye3e6", "5xubtvj2p8k742g", "5xzvi729wirzshm", "5xu8xcypmc5huqu", "5x7m659c8dadh9y", "5x3kasqp2ahhcp6", "5x7ma8wdggqcy5m", "5xka7qy8y8pv4em", "5xe2isqwvyctmgc", "5xtj7yzgdxpcnje", "5xunzmtet6w9vjy", "5xcdir9ad5ep4m6", "5xyk7wijbyvxyps", "5xv27655buh958w", "5xihud39retduc9", "5xh5pxkku959nh4", "5xvps6m5gu45afk", "5x2hnzhyihbfwhg", "5x39jj2mpxtpwfi", "5xbjeaucgjfny6i", "5xypnh5edqwt44s", "5x2m8rmmw5zkxfm", "5xcug97h5mhtx6i", "5x6awbzir92ckam", "5xibfqgxiq9nj92", "5xrxx39rk6f5rja", "5xyee8b3k4bp4hc", "5xkssc2698es99u", "5xshqp2h8jn93rw", "5xp929qwiyws5jq", "5x9j8qrjfg352pu", "5xtvdvzfwaw8y6y", "5xygzsgrixr5x84", "5x7gke2mpu8xwdm", "5xjfu8dkivvfzxy", "5x9qmjgj4pachk4", "5xqsvq5usv2aibq", "5xcbns9bfjcjgs2", "5xubma5bgjh6jti", "5xe78xtfcxjbruk", "5x7ybr686h7n3fq", "5xpbbsbtgb5q5v4", "5xpjxx9j8axwqps", "5xqxn6v7xpars5i", "5xxx2gbwjcwdk2e", "5xxv5de286g5k4a", "5xdnzavnutxpkws", "5xjbgdqumjzr9ii", "5xp8bemwf9kbun2", "5xw3tsb5kjeixsq", "5xe322ksakg4fe6", "5xp5yyw8ca5jpha", "5xkd3ez9vwasna6", "5x5tpbci5g25ijw", "5x3pdavzbtubqpg", "5xg5vfbfrfj248y", "5xf6wkm4m4hbfee", "5xukcadq8z8735q", "5xdettcbxkxhhpg", "5xy5quuycfdsayy", "5xj4zstpr99mvz6", "5xtaqmbahp2u322", "5xg2mhvsrggggms", "5xu6ctaa75i2wzu", "5x8sp8h5p9b594y", "5xh6rnrh77jpa5w", "5xw59egmsumc48y", "5x4nfqpeanddu72", "5xaf7trsye4k5xu", "5x2acbzy9ppj7j9", "5x966mny874sgf2", "5xx5n6h7xepsqx9", "5x635g2w8fw38em", "5xuwb9z3uhjness", "5xm68r49yaj7pta", "5xm4yq7bczsvyvi"]
    b = ["5xn3ibtmgysxzb4", "5xaiave6dcfiakm", "5xf6q2bzu6mxeqc", "5x568imkc4nsws6", "5xbjd37gprseia4",
         "5xewbb6iqdvzymy", "5xh9ag2umn5bgvi", "5xcsdkkgyp2hq9y", "5xhfbct6ekv4rq2", "5xjeqgvz87wcnpc",
         "5xe4k34uhqfrc82", "5x7qxfat8a4xpk4", "5xdfadzkdsu3ezm", "5x9hmk6fty235dc", "5x58dbnm99ee2a4",
         "5xartyh3ddsi3uc", "5xvgb4knaymq5hy", "5x6nxr4dgennaei", "5xsbni3a7advbje", "5xd7ztn35zh26wk",
         "5xchsmxxfvf7ajw", "5xri2a9v2wmuk2y", "5xbf49p8wy869ew", "5xdef4fabiyugfi", "5xcb5yb72bi989e",
         "5xer8k8vwiznrwk", "5xjxsa9x95pkt72", "5xu8h37p27j67xi", "5xwrcfckhcz6rqa", "5xmdtsnyvgdw6d9",
         "5xhan6erq55urea", "5x6ifz4hezz46vy", "5xwpbynk9jnmeua", "5xeaeza4fbcrrp9", "5xj9ybxct72zg84",
         "5x6b3bf9csha99k", "5xtgkp7sziehjx4", "5xqa29hgr2a88zy", "5xu5g2z2vh96iss", "5xqvgtzsnvyyew4",
         "5xw9yv5sr2xws2g", "5xeae292ehir3ky", "5xsj7q2bdagu7n4", "5xxq8wu2b3abkna", "5xhqsybz9zwdsxa",
         "5xzrj9nckdph9k4", "5xinbgdj9cyzjbk", "5xgwcrqiv8rqzt6", "5xfce99qhz8kfwq", "5xrkwj52iiyzxq9",
         "5xwqjtk4ka6phi6", "5xjynnsuz8bu7ym", "5xt27gckt62rvz2", "5xt3y8sswb4q8yw", "5xew3etn63nh8cy",
         "5xgrngkeiuyymzy", "5xz9am75umdgkaq", "5xz5fhuhkryr5qg", "5xrfccctcftiaxe", "5x7vctc22b8hnrk",
         "5xb6umn5m9cp8ru", "5xkr79xk99jnk52", "5xvp55cpwsfyjhs", "5xqxruu9jue9qqc", "5xdd99qn2xcdpng",
         "5xmk6gzcqpv3nci", "5x8tf2n6m47rkgs", "5xcafbcn2yfn8m9", "5x9km28rkm8rzbk", "5xacb224am73hfe",
         "5xx3vcetekka3am", "5xm2wf9ietmyhxg", "5xhf68qwuggvh86", "5xavwrwajau9q4c", "5x26wbthzbrc7ya",
         "5xrbrts3g5edmum", "5xz7iajtzttdz69", "5xa3xzxz4geamt2", "5x7q5etzvjvijma", "5x5xkmuut6ym5gm",
         "5xkacp955mk6j4k", "5xr4z327nru3s4m", "5xpzasvexttmugc", "5xigamf6e9zmhwe", "5x27gk2fsdmwux9",
         "5x6a2tugkw9zim9", "5xr2iqy53mxb33e", "5xf7hukr77uqkam", "5x6zk2xmzub4kca", "5xkt56cipmkw4ic",
         "5xjs4ju62fguf2e", "5x3mwtzm2qh54g6", "5x7z27qq4p5tdbe", "5xwmcr66xp6vria", "5x99ac3k5ptsrwm",
         "5x3n5wscdrw2mhm", "5xts72ghgzpkja2", "5xdatnd4eehp6e9", "5xwfkiqq4g2tb3e", "5xdrvvqespzrja4",
         "5xmvxm3xk98g6qk", "5xfga3rjajr33gk", "5xgfwty7eci67sw", "5x3xii6983eh7nm", "5xqwpanrubxdw4q",
         "5x2gghmnyjmedbe", "5xixngta4que3fg", "5xznxzn3bxbiijq", "5x8vf2rtjihenyc", "5xvag92hpn2du3k",
         "5xbhpet4gcw3fgi", "5x344iryvskten6", "5xdab2xftd682am", "5xbry5kh4pyh3jg", "5xiza7sqptzfkxw",
         "5x2j4axghx8ufj9", "5xc3aizxuj23c59", "5xbuybc9jasbn72", "5x5er83m42nyzpw", "5xkqwpmcze65zmw",
         "5xcqmwimw5hmk7s", "5xzgvm76y6pavum", "5xssrd77nsnhfqu", "5xhg8zdy6niivvu", "5xs9zyxy67mknhc",
         "5xtxdme8swwrnfm", "5x8pz369c6re6a2", "5xgtk5tj3p5vs32", "5xzd69sfu3v6g6c", "5xg3bydkywvfubq",
         "5xku5ppnirgp3n9", "5xqqrajanwsz3n4", "5x5sc7cxnmemgua", "5xr6j24tia8tpzs", "5xhigqdssdst386",
         "5xgvgavjb3mb23c", "5xvjegdqeyb4zji", "5xizpvtdhyenfmu", "5xdkaqkr8zuj2gy", "5xqpq5f4eur92fe",
         "5xs4sj78c55gzsw", "5xg88rj462exe7y", "5xzaws6q5hbb96w", "5xn3vbjm9ic5c7w", "5xrwz3cucjuuarq",
         "5xii3t2iq6hjcx2", "5xzmk5ifqt4t7je", "5xe8sikf3jgrdzw", "5xppnqz545szpza", "5x8izmfq73et822",
         "5xeijvr8377xevg", "5xm58ugk32cm5gi", "5xvpkxhwawf8bwk", "5xp2pvy82bp28g6", "5x8422ax9sxt72u",
         "5xr7z8cgtstcpqi", "5xeu6rca54d4ibs", "5x6ymef5kvq5i7e", "5xv5qistx9vtxvq", "5xmm69y785qi3we",
         "5x6596ju7hmurfm", "5xa24jwx4wkqfuk", "5x5zp8p2pq5sdka", "5x6ivgfgkuqec8m", "5x842ku6mu8fd5e"]

    print(b)
    print(len(b))
    c = ','.join(b)
    print(c)

    d_list = ["https://ali-album.static.yximgs.com/mediacloud/album/album_image/IzNuDUtWMozFQY2I2U2Y6PnBcNK2IbXhPACXTBnKLPg.jpg?auth_key=1579828281-189659489-0-eb4e1194edfc339677422021148cf87c", "https://ali-album.static.yximgs.com/mediacloud/album/album_image/zXZhhMem8ahMcHPRXLtV_X41_5jkqVXVk13whY0vFyM.jpg?auth_key=1579828281-1030581668-0-5ed017fd61c7f1b7c4a1486b01d3f53f",
 "https://ali-album.static.yximgs.com/mediacloud/album/album_image/S9yDYWpSOUXXoLOpZBFjzyfgpfb7uxbYmGlrbgXlUJo.jpg?auth_key=1579828281-1055431687-0-95cd0eb4d049e57b242b3da8798d8f5c",
 "https://ali-album.static.yximgs.com/mediacloud/album/album_image/Sfo_gXCC37ijH8pILY81EnA61nflhQvLl-Mu_mxBies.jpg?auth_key=1579828281-671812861-0-8ba8f3139c3de38c77cabc607a1ae8c2", "https://tx-album.static.yximgs.com/mediacloud/album/album_image/Ky2Tpuo1hYh22xDyChwYsOpG9JguEN3l06mB6t7bu_o.jpg?sign=7fb5e537f7e3cc5a2603e39017cc59cb&t=1579830081&us=924543277", "https://tx-album.static.yximgs.com/mediacloud/album/album_image/VunnSVjpTUkc_1dETaPKCyqlo_A_i6i5mU7IEaIp2uM.jpg?sign=d7784e4a7f4cb0532b2b4801c864a4cb&t=1579830081&us=974951001",
  "https://ali-album.static.yximgs.com/mediacloud/album/album_image/pjyJ0BUbavCuA91wGJDWuhWs9D7jegWwrA8LWtR6ulU.jpg?auth_key=1579828281-1999020296-0-4885ded0203d85e0698d9c9c9245138b", "https://tx-album.static.yximgs.com/mediacloud/album/album_image/XeP5L3fIEiateEOdhzA67PzjuUguvr3VlvaSrg7f-CU.jpg?sign=0ebafbda4dc24e7e9d53dcfa6e849146&t=1579830081&us=1721090523", "https://ali-album.static.yximgs.com/mediacloud/album/album_image/qQgJiCvruYLuNsmL0Cqv_-HV6jGg7Mcl5hZhq8OXcRc.jpg?auth_key=1579828281-343935020-0-11ee11b7ed23846026a77aafb09ee3f0",
  "https://ali-album.static.yximgs.com/mediacloud/album/album_image/Z18fSFWGsPs_VpZJZJ095WHln1e2oIewDTTWv4_-L1c.jpg?auth_key=1579828281-548234236-0-5a71b2a8a83a914ec93c4eea04f30037", "https://tx-album.static.yximgs.com/mediacloud/album/album_image/kO21iW4lqg05pLcsqgYp3BiVOI_fAtbceLyEY6E9s_w.jpg?sign=5d8cbebd1f18065d6a82afe3ffe1bfce&t=1579830081&us=2138582954", "https://tx-album.static.yximgs.com/mediacloud/album/album_image/9vMkidllp-uaOU2ylfC2r4xmXsSBIls-EK5uglsUkec.jpg?sign=8ee7da5e759a9bf73d0c42a855f1c6c5&t=1579830081&us=793378287",
   "https://tx-album.static.yximgs.com/mediacloud/album/album_image/molVwBN4ClICUbKwyAG65AK77AYeVrYRpkwlEJadx78.jpg?sign=f14906404027e22da234f4919336b841&t=1579830081&us=187276462", "https://ali-album.static.yximgs.com/mediacloud/album/album_image/94Fy2nGKza_QOfFe_PuJ7EvQ3LKW_9UNT4IFM0XKUBE.jpg?auth_key=1579828281-1768800585-0-906c1d3690d2fdb9fc3b5512cbc4c078", "https://ali-album.static.yximgs.com/mediacloud/album/album_image/BlM6uJ0ijpC0-ucQoMS-C60e430M84rUHWs03b8-Xkg.jpg?auth_key=1579828281-1289801336-0-9f0578c5466577af0e1c95402c922a5e", "https://ali-album.static.yximgs.com/mediacloud/album/album_image/r8yNMUj5dqtYVQgGqSB52oc20ImJsrKwJ71tkWCSZqI.jpg?auth_key=1579828281-1549178991-0-0358555158f6d56132a824b6fb05629b", "https://tx-album.static.yximgs.com/mediacloud/album/album_image/GVmZWWlYhOQkDSe_jfZXpkCqfYyPEjTLVD3nEvLJO0Q.jpg?sign=d3e62d8583b1b9375f138913830d1246&t=1579830081&us=1090365439", "https://ali-album.static.yximgs.com/mediacloud/album/album_image/ILtIsuqAFq0yalPx4K1vJ3u2-UygZsbrh7zxQtlld6Q.jpg?auth_key=1579828281-985275546-0-38d969185b831a3bb118ea2f08cc5ee3"]
    for i in d_list:
        print(i)

