def getBase(n):
        if n < 100000:
                if n<100:
                        if n<10:
                                return 1
                        else:
                                return 10
                else:
                        if n < 1000:
                                return 100
                        else:
                                if n<10000:
                                        return 1000
                                else: 
                                        return 10000
        else:
                if n < 10000000:
                        if n < 1000000:
                                return 100000
                        else:
                                return 1000000
                else:
                        if n < 100000000:
                                return 10000000
                        else:
                                if n < 1000000000:
                                        return 100000000
                                else:
                                        #add new here
                                        return 1000000000

