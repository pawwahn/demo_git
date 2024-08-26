seconds = 103894

hours, remainder = divmod(seconds, 3600)
#print(hours, remainder)
minutes, sec = divmod(remainder, 60)
print(hours, minutes, sec)