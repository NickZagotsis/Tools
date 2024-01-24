import os,time
WEIRDNESS = 8 #Len of files' extentions to be "Weird"
def log(event): #function to log progress
    import datetime
    now = str(datetime.datetime.now())[:-4]
    print(now+':'+event)

def dir_path(string): #Function to check for directory or file
    if os.path.isdir(string):
        return string
    elif os.path.isfile(string):
        return string
    raise 'Must provide a directory or a file containing file names'
def argparser(): #takes the arguments of the user
    import argparse
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input-dir", required=False,
        type=dir_path, default='.',help="The directory or file to search for file extentions")
    args=parser.parse_args()
    return args.input_dir
def main():
    input = argparser()
    log("Program started")
    start = time.time()
    ext = []
    counter = []
    if os.path.isdir(input): #if the provided input is a directory, Recurse and find all files' extentions
        for r , d ,f in os.walk(input):
                for file in f:
                    full = os.path.join(r,file).rstrip("\n")
                    if ".git" in full or "." not in full: #can add some more exceptions if you like here
                        continue
                    full = full.split('.')
                    full = full[-1]
                    if full in ext:
                        counter[ext.index(full)] += 1
                    else:
                        ext.append(full)
                        counter.append(1)
    else:
        with open(input) as f: #If a file is provided
            while True:
                full = f.readline().rstrip("\n")
                if len(full)==0:
                    break
                if ".git" in full or "." not in full or full.endswith(".&"):
                        continue
                full = full.split('.')
                full = full[-1]
                if full in ext:
                    counter[ext.index(full)] += 1
                else:
                    ext.append(full)
                    counter.append(1)
    weird = []
    weirdc = []
    for i in range(len(ext)):
        if len(ext[i])>=WEIRDNESS: #you can change weirdness. Default is at 8
            weird.append(ext[i])
            weirdc.append(counter[i])
            continue
        print(f"Extention {ext[i]}: {counter[i]}")
    if len(weird)>0:
        print("---------------------------------------")
        print("Weird extentions (len>8)")
        for i in range(len(weird)):
            print(f"Extention {weird[i]}: {weirdc[i]}")
    print("---------------------------------------")
    end = time.time()
    log(f"Program finished with execution time:{end-start}")
if __name__ == "__main__":
    main()