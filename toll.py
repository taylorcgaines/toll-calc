oldfile = open("input.txt","r")
newfile = open("fromfile.txt","wr")

#THIS IS THE FORMAT FOR THE OBJECTS
# {
#       “Location”: ,
#       “Type”: ,
#       “Cash”:,
#       “Axles2noTag”: ,
#       “Axles2tag”: ,
#       “Axles3": ,
#       “Axles4”: ,
#       “Axles5": ,
#       “Axles6”:
#     }

newfile.write("module.exports = {")
newfile.write(" tollway: [")

for line in oldfile:
    newfile.write("{")
    data = line.split("    ")
    newfile.write("'Location': " + data[0] + ",")
    newfile.write("'Type': " + data[1] + ",")
    if "Cash Not Accepted" in data[2]:
        newfile.write("Cash: False")
    else:
        newfile.write("Cash: True")
    #TODO for word in data[2], SPLIT and take the last entry and save it to Axles2noTag
    newfile.write("'Axles2noTag': " + data[3] + ",")
    newfile.write("'Axles2tag': " + data[4] + ",")
    newfile.write("'Axles3': " + data[5] + ",")
    newfile.write("'Axles4': " + data[6] + ",")
    newfile.write("'Axles5': " + data[7] + ",")
    newfile.write("'Axles6': " + data[8] + ",")

oldfile.close()
newfile.close()
