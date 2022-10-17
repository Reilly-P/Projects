registrations = ["47-FBI", "BOND-007", "RF-FBI18", "MARICA-13", "13A-FBILL"]
i = 0
FBIs = 0
iterations = 0
lines = []
for FBI in registrations:
        iterations += 1
        if "FBI" in FBI:
            FBIs += 1
            lines.append(iterations)

if FBIs == 0:
    print("HE GOT AWAY!")
print(lines)