import json

iteration = int(input('Enter iteration: '))

r = 'r' 
l = 'l'
  
old = [r] 
new = old 

d = {
    "iterations": [

    ]
}

cycle = 1
  
totalCount = 0
while cycle<iteration: 
    
    new = old
    new.append(r)
    
    old.reverse()
    count = 0
    for char in range(0, len(old)):  
         
        if old[char] == r:  
            old.insert(char + 1, l) 

        
        elif old[char] == l:  
            
           old.insert(char + 1, r) 
        print(str(count)+"/"+str(len(old))+" iterations of "+str(cycle)+" Complete")
        count += 1
        
    for i in range(0, len(old)):
        new.append(old[i])
  
    totalCount += count
    print("\n"*50+str(totalCount)+" Iterations completed.")
    old = new  
    """
    with open("Save",'a') as fish:
        fish.write("Generation "+str(cycle)+": "+new+'\n')
    """

    with open(f"save/{cycle}.json", 'w+') as fp:
        try:
            fish = json.load(fp)
        except json.JSONDecodeError:
            fish = d
        fish["iterations"] = new
        fp.truncate(0)
        json.dump(fish, fp, indent=4)
    cycle = cycle + 1