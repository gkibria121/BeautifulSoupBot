from movie.main import *
##from main import *
def run(url,choise,pixel):

    if choise == '1':
       x= getGDS(url,pixel)
       if x==0:
            return 0
    elif choise == '2':
        x= getGDrive(url,pixel)
        if x==0:
            return 0

##run('https://mlwbd.cloud/movie/doctor-strange-in-the-multiverse-of-madness-2022/','1','720p')
