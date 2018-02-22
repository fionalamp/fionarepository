print("Hmerologio")
import calendar

x = int(input("Δώσε μήνα : "))
y = int(input("Δώσε έτος : "))
calndr = calendar.month(y, x)

print("Ημερολόγιο του έτους:", y, "και του",x, " μήνα, είναι:")

print (calndr)
