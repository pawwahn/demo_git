def convertTime(n):
    hours,remainder = divmod(n,3600)
    minutes, seconds = divmod(remainder, 60)
    print(hours,minutes,seconds)

convertTime(100)