total_seconds = 9137

hours =total_seconds//3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(total_seconds , "seconds=", hours , " hours" , minutes , "minutes", seconds, "seconds")
