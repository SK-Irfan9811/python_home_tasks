def convert_to_meters(height_in_feet):
        idx1=0
        idx2=0
        if('f' in height_in_feet):
            idx1=height_in_feet.index('f')
        if('i' in height_in_feet):
            idx2=height_in_feet.index('i')

        if(idx1!=0 and idx2!=0):
            return int(height_in_feet[:idx1])*0.3048+int(height_in_feet[idx1+2:idx2])*0.0254
        elif(idx2==0):
            return int(height_in_feet[:idx1])*0.3048
        else:
            return int(height_in_feet[:idx2])*0.0254

l=['05ft10in','05f','04ft0in','00ft10in','10in','2in','03in']
height_in_meters=map((lambda x:round(convert_to_meters(x),3)),l)
print(list(height_in_meters))

