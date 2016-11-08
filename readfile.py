from astropy.io import fits
import matplotlib.pyplot as plt 


dir_data_raw='/Users/hqchen/filacf/data_cubes/'
dir_data_proc='/Users/hqchen/filacf/data_proc/'

#No=input('put number, quote:\n')
#string='_a1.0005_CL'+No+'_N256_Lv7.fits'

def get_raw_data(CL_No,Lv=7,data_dir=dir_data_raw):

    string='_a1.0005_CL'+CL_No+'_N256_Lv'+str(Lv)+'.fits'

    hdulist=fits.open(data_dir+'temperature'+string)
    temp=hdulist[0].data
    hdulist.close()

    hdulist=fits.open(data_dir+'potential'+string)
    pot=hdulist[0].data
    hdulist.close()

    hdulist=fits.open(data_dir+'rhogas'+string)
    rhogas=hdulist[0].data
    hdulist.close()

    hdulist=fits.open(data_dir+'rhodm'+string)
    rhodm=hdulist[0].data
    hdulist.close()

    hdulist=fits.open(data_dir+'vx'+string)
    vx=hdulist[0].data
    hdulist.close()

    hdulist=fits.open(data_dir+'vy'+string)
    vy=hdulist[0].data
    hdulist.close()

    hdulist=fits.open(data_dir+'vz'+string)
    vz=hdulist[0].data
    hdulist.close()
    return temp,pot,rhogas,rhodm,vx,vy,vz
'''
for i in range(256):
	slc=temp[i]
	if i==20:
		plt.imshow(slc)
		plt.show()
hdulist.close()
'''
