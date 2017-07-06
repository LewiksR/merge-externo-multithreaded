# Relatório de cProfile: sortByCEP_Singlethreaded.py

 | ncalls | tottime | percall | cumtime | percall | filename:lineno(function) |
 | --- | --- | --- | --- | --- | --- |
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | \<frozen importlib._bootstrap\>:989(_handle_fromlist)
 | 233 | 0.000 | 0.000 | 0.001 | 0.000 | genericpath.py:27(isfile)
 | 1 | 10.479 | 10.479 | 21.875 | 21.875 | orderByCEP_oldButWorking.py:3(<module>)
 | 215 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method _stat.S_ISREG}
 | 1 | 0.000 | 0.000 | 21.875 | 21.875 | {built-in method builtins.exec}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method builtins.hasattr}
 | 10231775 | 0.846 | 0.000 | 0.846 | 0.000 | {built-in method builtins.len}
 | 75 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method builtins.print}
 | 279 | 0.007 | 0.000 | 0.007 | 0.000 | {built-in method io.open}
 | 138 | 0.169 | 0.001 | 0.169 | 0.001 | {built-in method posix.remove}
 | 74 | 0.027 | 0.000 | 0.027 | 0.000 | {built-in method posix.rename}
 | 233 | 0.001 | 0.000 | 0.001 | 0.000 | {built-in method posix.stat}
 | 5 | 0.000 | 0.000 | 0.000 | 0.000 | {built-in method time.time}
 | 699307 | 0.051 | 0.000 | 0.051 | 0.000 | {method 'append' of 'list' objects}
 | 139 | 0.001 | 0.000 | 0.001 | 0.000 | {method 'close' of '_io.BufferedReader' objects}
 | 139 | 0.002 | 0.000 | 0.002 | 0.000 | {method 'close' of '_io.BufferedWriter' objects}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 | {method 'disable' of '_lsprof.Profiler' objects}
 | 5397228 | 1.395 | 0.000 | 1.395 | 0.000 | {method 'pack' of 'Struct' objects}
 | 6096675 | 2.346 | 0.000 | 2.346 | 0.000 | {method 'read' of '_io.BufferedReader' objects}
 | 70 | 0.245 | 0.003 | 0.245 | 0.003 | {method 'sort' of 'list' objects}
 | 7570681 | 2.460 | 0.000 | 2.460 | 0.000 | {method 'unpack' of 'Struct' objects}
 | 5397228 | 3.844 | 0.000 | 3.844 | 0.000 | {method 'write' of '_io.BufferedWriter' objects}

----

# Relatório de cProfile: sortByCEP_Multithreaded.py

 | ncalls | tottime | percall | cumtime | percall filename:lineno(function) |
 |---|---|---|---|---| 
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:102(release)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:142(\_\_init\_\_)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:146(\_\_enter\_\_)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:153(\_\_exit\_\_)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:159(\_get\_module\_lock)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:173(cb)
 | 8/3 | 0.000 | 0.000 | 0.027 | 0.009 <frozen importlib.\_bootstrap>:197(\_call\_with\_frames\_removed)
 | 121 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:208(\_verbose\_message)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:293(\_\_init\_\_)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:297(\_\_enter\_\_)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:304(\_\_exit\_\_)
 | 28 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:307(<genexpr>)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:35(\_new\_module)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:355(\_\_init\_\_)
 | 13 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:389(cached)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:402(parent)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:410(has\_location)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:493(\_init\_module\_attrs)
 | 7 | 0.000 | 0.000 | 0.014 | 0.002 <frozen importlib.\_bootstrap>:553(module\_from\_spec)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:57(\_\_init\_\_)
 | 7/2 | 0.000 | 0.000 | 0.038 | 0.019 <frozen importlib.\_bootstrap>:641(\_load\_unlocked)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:698(find\_spec)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:77(acquire)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:771(find\_spec)
 | 21 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:834(\_\_enter\_\_)
 | 21 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:838(\_\_exit\_\_)
 | 7 | 0.000 | 0.000 | 0.001 | 0.000 <frozen importlib.\_bootstrap>:861(\_find\_spec)
 | 7/2 | 0.000 | 0.000 | 0.038 | 0.019 <frozen importlib.\_bootstrap>:931(\_find\_and\_load\_unlocked)
 | 7/2 | 0.000 | 0.000 | 0.038 | 0.019 <frozen importlib.\_bootstrap>:958(\_find\_and\_load)
 | 19 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap>:989(\_handle\_fromlist)
 | 29 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:1080(\_path\_importer\_cache)
 | 7 | 0.000 | 0.000 | 0.001 | 0.000 <frozen importlib.\_bootstrap\_external>:1117(\_get\_spec)
 | 7 | 0.000 | 0.000 | 0.001 | 0.000 <frozen importlib.\_bootstrap\_external>:1149(find\_spec)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:1228(\_get\_spec)
 | 22 | 0.000 | 0.000 | 0.001 | 0.000 <frozen importlib.\_bootstrap\_external>:1233(find\_spec)
 | 12 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:263(cache\_from\_source)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:361(\_get\_cached)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:393(\_check\_name\_wrapper)
 | 22 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:41(\_relax\_case)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:430(\_validate\_bytecode\_header)
 | 6 | 0.000 | 0.000 | 0.001 | 0.000 <frozen importlib.\_bootstrap\_external>:485(\_compile\_bytecode)
 | 12 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:52(\_r\_long)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:524(spec\_from\_file\_location)
 | 112 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:57(\_path\_join)
 | 112 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:59(<listcomp>)
 | 12 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:63(\_path\_split)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:669(create\_module)
 | 6/1 | 0.000 | 0.000 | 0.024 | 0.024 <frozen importlib.\_bootstrap\_external>:672(exec\_module)
 | 6 | 0.000 | 0.000 | 0.021 | 0.003 <frozen importlib.\_bootstrap\_external>:743(get\_code)
 | 35 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:75(\_path\_stat)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:800(\_\_init\_\_)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:825(get\_filename)
 | 6 | 0.000 | 0.000 | 0.020 | 0.003 <frozen importlib.\_bootstrap\_external>:830(get\_data)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:840(path\_stats)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:85(\_path\_is\_mode\_type)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:908(\_\_init\_\_)
 | 1 | 0.000 | 0.000 | 0.013 | 0.013 <frozen importlib.\_bootstrap\_external>:919(create\_module)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:927(exec\_module)
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 <frozen importlib.\_bootstrap\_external>:94(\_path\_isfile)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 <string>:1(<module>)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 <string>:5(TokenInfo)
 | 1 | 0.000 | 0.000 | 0.001 | 0.001 \_\_init\_\_.py:359(namedtuple)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 \_\_init\_\_.py:422(<genexpr>)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 \_\_init\_\_.py:424(<genexpr>)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 \_weakrefset.py:36(\_\_init\_\_)
 | 36 | 0.000 | 0.000 | 0.000 | 0.000 \_weakrefset.py:81(add)
 | 126 | 0.000 | 0.000 | 0.000 | 0.000 enum.py:265(\_\_call\_\_)
 | 126 | 0.000 | 0.000 | 0.000 | 0.000 enum.py:515(\_\_new\_\_)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 enum.py:795(\_\_or\_\_)
 | 57 | 0.000 | 0.000 | 0.000 | 0.000 enum.py:801(\_\_and\_\_)
 | 1 | 0.000 | 0.000 | 0.003 | 0.003 linecache.py:6(<module>)
 | 1 | 2.732 | 2.732 | 25.097 | 25.097 orderByCEP\_Multithreaded.py:3(<module>)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 orderByCEP\_Multithreaded.py:37(thread\_merge)
 | 35 | 0.000 | 0.000 | 0.002 | 0.000 orderByCEP\_Multithreaded.py:38(\_\_init\_\_)
 | 1 | 0.000 | 0.000 | 0.014 | 0.014 queue.py:1(<module>)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 queue.py:13(Empty)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 queue.py:17(Full)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 queue.py:199(\_init)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 queue.py:21(Queue)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 queue.py:214(PriorityQueue)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 queue.py:233(LifoQueue)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 queue.py:27(\_\_init\_\_)
 | 2 | 0.000 | 0.000 | 0.001 | 0.000 re.py:231(compile)
 | 2 | 0.000 | 0.000 | 0.001 | 0.000 re.py:286(\_compile)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:223(\_compile\_charset)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:250(\_optimize\_charset)
 | 3 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:376(\_mk\_bitmap)
 | 3 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:378(<listcomp>)
 | 5 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:388(\_simple)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:414(\_get\_literal\_prefix)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:441(\_get\_charset\_prefix)
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:482(\_compile\_info)
 | 4 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:539(isstring)
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:542(\_code)
 | 2 | 0.000 | 0.000 | 0.001 | 0.000 sre\_compile.py:557(compile)
 | 11/2 | 0.000 | 0.000 | 0.000 | 0.000 sre\_compile.py:64(\_compile)
 | 11 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:111(\_\_init\_\_)
 | 18 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:159(\_\_len\_\_)
 | 41 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:163(\_\_getitem\_\_)
 | 5 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:167(\_\_setitem\_\_)
 | 20 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:171(append)
 | 17/8 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:173(getwidth)
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:223(\_\_init\_\_)
 | 54 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:232(\_\_next)
 | 36 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:248(match)
 | 47 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:253(get)
 | 17 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:285(tell)
 | 8 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:294(\_class\_escape)
 | 4/2 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:407(\_parse\_sub)
 | 5/2 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:469(\_parse)
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:76(\_\_init\_\_)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:81(groups)
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:829(fix\_flags)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:84(opengroup)
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:845(parse)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 sre\_parse.py:96(closegroup)
 | 1 | 0.000 | 0.000 | 0.009 | 0.009 threading.py:1(<module>)
 | 35 | 0.000 | 0.000 | 19.464 | 0.556 threading.py:1024(join)
 | 35 | 0.000 | 0.000 | 19.464 | 0.556 threading.py:1062(\_wait\_for\_tstate\_lock)
 | 35 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:1120(daemon)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:1158(Timer)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:1188(\_MainThread)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:1190(\_\_init\_\_)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:1207(\_DummyThread)
 | 70 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:1230(current\_thread)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:203(Condition)
 | 39 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:215(\_\_init\_\_)
 | 36 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:239(\_\_enter\_\_)
 | 36 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:242(\_\_exit\_\_)
 | 35 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:248(\_release\_save)
 | 35 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:251(\_acquire\_restore)
 | 36 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:254(\_is\_owned)
 | 35 | 0.000 | 0.000 | 0.252 | 0.007 threading.py:263(wait)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:334(notify)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:357(notify\_all)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:369(Semaphore)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:449(BoundedSemaphore)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:487(Event)
 | 36 | 0.000 | 0.000 | 0.001 | 0.000 threading.py:498(\_\_init\_\_)
 | 70 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:506(is\_set)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:512(set)
 | 35 | 0.000 | 0.000 | 0.252 | 0.007 threading.py:533(wait)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:566(Barrier)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:720(BrokenBarrierError)
 | 35 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:727(\_newname)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:738(Thread)
 | 36 | 0.000 | 0.000 | 0.002 | 0.000 threading.py:757(\_\_init\_\_)
 | 35 | 0.000 | 0.000 | 0.254 | 0.007 threading.py:828(start)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:87(\_RLock)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:890(\_set\_ident)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:893(\_set\_tstate\_lock)
 | 35 | 0.000 | 0.000 | 0.000 | 0.000 threading.py:966(\_stop)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 token.py:1(<module>)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 token.py:74(<dictcomp>)
 | 20 | 0.000 | 0.000 | 0.000 | 0.000 tokenize.py:112(group)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 tokenize.py:113(any)
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 tokenize.py:114(maybe)
 | 3 | 0.000 | 0.000 | 0.000 | 0.000 tokenize.py:137(\_all\_string\_prefixes)
 | 24 | 0.000 | 0.000 | 0.000 | 0.000 tokenize.py:148(<listcomp>)
 | 1 | 0.000 | 0.000 | 0.003 | 0.003 tokenize.py:21(<module>)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 tokenize.py:217(TokenError)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 tokenize.py:219(StopTokenizing)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 tokenize.py:222(Untokenizer)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 tokenize.py:99(TokenInfo)
 | 1 | 0.000 | 0.000 | 0.008 | 0.008 traceback.py:1(<module>)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 traceback.py:223(FrameSummary)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 traceback.py:310(StackSummary)
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 traceback.py:426(TracebackException)
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_imp.\_fix\_co\_filename}
 | 21 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_imp.acquire\_lock}
 | 1 | 0.013 | 0.013 | 0.013 | 0.013 {built-in method \_imp.create\_dynamic}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_imp.exec\_dynamic}
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_imp.is\_builtin}
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_imp.is\_frozen}
 | 28 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_imp.release\_lock}
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_sre.compile}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_thread.\_set\_sentinel}
 | 87 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_thread.allocate\_lock}
 | 85 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method \_thread.get\_ident}
 | 35 | 0.002 | 0.000 | 0.002 | 0.000 {built-in method \_thread.start\_new\_thread}
 | 25 | 0.001 | 0.000 | 0.001 | 0.000 {built-in method builtins.\_\_build\_class\_\_}
 | 7 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.any}
 | 8/1 | 0.000 | 0.000 | 25.097 | 25.097 {built-in method builtins.exec}
 | 42 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.getattr}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.globals}
 | 57 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.hasattr}
 | 218 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.isinstance}
2797379/2797373 | 0.226 | 0.000 | 0.226 | 0.000 {built-in method builtins.len}
 | 37 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.max}
 | 60 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.min}
 | 15 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.ord}
 | 77 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.print}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method builtins.repr}
 | 12 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method from\_bytes}
 | 72 | 0.004 | 0.000 | 0.004 | 0.000 {built-in method io.open}
 | 6 | 0.001 | 0.000 | 0.001 | 0.000 {built-in method marshal.loads}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method math.ceil}
 | 19 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method posix.fspath}
 | 14 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method posix.getcwd}
 | 1 | 0.182 | 0.182 | 0.182 | 0.182 {built-in method posix.rename}
 | 35 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method posix.stat}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method sys.\_getframe}
 | 5 | 0.000 | 0.000 | 0.000 | 0.000 {built-in method time.time}
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 {method '\_\_contains\_\_' of 'frozenset' objects}
 | 36 | 0.000 | 0.000 | 0.000 | 0.000 {method '\_\_enter\_\_' of '\_thread.lock' objects}
 | 36 | 0.000 | 0.000 | 0.000 | 0.000 {method '\_\_exit\_\_' of '\_thread.lock' objects}
 | 177 | 19.716 | 0.111 | 19.716 | 0.111 {method 'acquire' of '\_thread.lock' objects}
 | 213 | 0.000 | 0.000 | 0.000 | 0.000 {method 'add' of 'set' objects}
 | 35 | 0.000 | 0.000 | 0.000 | 0.000 {method 'append' of 'collections.deque' objects}
 | 699505 | 0.052 | 0.000 | 0.052 | 0.000 {method 'append' of 'list' objects}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {method 'close' of '\_io.BufferedReader' objects}
 | 70 | 0.002 | 0.000 | 0.002 | 0.000 {method 'close' of '\_io.BufferedWriter' objects}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {method 'disable' of '\_lsprof.Profiler' objects}
 | 8 | 0.000 | 0.000 | 0.000 | 0.000 {method 'endswith' of 'str' objects}
 | 5 | 0.000 | 0.000 | 0.000 | 0.000 {method 'extend' of 'list' objects}
 | 28 | 0.000 | 0.000 | 0.000 | 0.000 {method 'find' of 'bytearray' objects}
 | 11 | 0.000 | 0.000 | 0.000 | 0.000 {method 'format' of 'str' objects}
 | 10 | 0.000 | 0.000 | 0.000 | 0.000 {method 'get' of 'dict' objects}
 | 6 | 0.000 | 0.000 | 0.000 | 0.000 {method 'isidentifier' of 'str' objects}
 | 3 | 0.000 | 0.000 | 0.000 | 0.000 {method 'items' of 'dict' objects}
 | 218 | 0.000 | 0.000 | 0.000 | 0.000 {method 'join' of 'str' objects}
 | 35 | 0.000 | 0.000 | 0.000 | 0.000 {method 'locked' of '\_thread.lock' objects}
 | 699307 | 0.196 | 0.000 | 0.196 | 0.000 {method 'pack' of 'Struct' objects}
 | 1398616 | 0.537 | 0.000 | 0.537 | 0.000 {method 'read' of '\_io.BufferedReader' objects}
 | 6 | 0.020 | 0.003 | 0.020 | 0.003 {method 'read' of '\_io.FileIO' objects}
 | 70 | 0.000 | 0.000 | 0.000 | 0.000 {method 'release' of '\_thread.lock' objects}
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 {method 'replace' of 'str' objects}
 | 60 | 0.000 | 0.000 | 0.000 | 0.000 {method 'rpartition' of 'str' objects}
 | 236 | 0.000 | 0.000 | 0.000 | 0.000 {method 'rstrip' of 'str' objects}
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 {method 'seek' of '\_io.BufferedReader' objects}
 | 2 | 0.000 | 0.000 | 0.000 | 0.000 {method 'setter' of 'property' objects}
 | 70 | 0.246 | 0.004 | 0.246 | 0.004 {method 'sort' of 'list' objects}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {method 'split' of 'str' objects}
 | 64 | 0.000 | 0.000 | 0.000 | 0.000 {method 'startswith' of 'str' objects}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {method 'tell' of '\_io.BufferedReader' objects}
 | 3 | 0.000 | 0.000 | 0.000 | 0.000 {method 'translate' of 'bytearray' objects}
 | 2097919 | 0.740 | 0.000 | 0.740 | 0.000 {method 'unpack' of 'Struct' objects}
 | 36 | 0.000 | 0.000 | 0.000 | 0.000 {method 'upper' of 'str' objects}
 | 1 | 0.000 | 0.000 | 0.000 | 0.000 {method 'values' of 'dict' objects}
 | 699307 | 0.420 | 0.000 | 0.420 | 0.000 {method 'write' of '\_io.BufferedWriter' objects}
