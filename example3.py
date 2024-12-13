projectscore = int(input("Enter the project score:"))
internalscore =int(input("Enter the internal score:"))
externalscore=int(input("Enter the external score:"))
if projectscore>=50 & internalscore>=50 & externalscore>=50:
     total_marks=float((0.7*projectscore)+(0.1*internalscore)+(0.2*externalscore))
     print(total_marks)
     if total_marks>90.0:
        print("A grade")
     elif total_marks>80.0:
        print("B grade")
     elif total_marks>70.0:
         print("C grade")
     else:
         print("D grade")
else:
    if projectscore<50:
      print("failed in project with score",projectscore)
    if internalscore<50:
      print("failed in internal with score", internalscore)
    if externalscore<50:
      print("failed in external with score", externalscore)
