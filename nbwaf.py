import json
from os.path import exists

def check(path, conf):
    try:
        notfoundpage = "404.php"
        chkpth = list(path)
        chkpth[0] = ""
        #print(chkpth)
        lastpath = "".join(chkpth)
        #print(lastpath)
        pathl = path.split(".")
        ext = "." + pathl[1]
        dirc = pathl[0]
        #print(dirc)
        #print(ext)
        f = open(conf, "r").read()
        c = json.loads(f)
        print(lastpath)
        #print(c[dirc])
        try:
            confv = c[lastpath]
            confv = confv.split(";")
        except:
            confv = c[notfoundpage]
            confv = confv.split(";")

        alwstatus = 0
        allowedextl = confv[0].split("(")[1].split(")")[0].split(",")
        blockedextl = confv[1].split("(")[1].split(")")[0].split(",")
        print(blockedextl)
        perms = confv[3]
        #print(perms)

        for l in range(len(allowedextl)):
            if ext == allowedextl[l]:
                alwstatus = 1
                break

        for m in range(len(blockedextl)):
            if ext == blockedextl[m]:
                alwstatus = 2
                break

        #print(alwstatus)
        file_exists = exists(lastpath)
        #print(file_exists)
        if file_exists == True:
            return alwstatus,file_exists, perms, lastpath, ext
        
        if file_exists == False:
            return alwstatus,file_exists, perms, notfoundpage , ext
    except:
        return 0,False,0,"NBERR0.php"




