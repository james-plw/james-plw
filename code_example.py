"""
This is a copy of the main code used in the final week of my master's project, 
to showcase the kind of code I wrote and used to produce the figures in the accompanying documents.

Data was downloaded from "https://www.tng-project.org" (onto my Uni's server at the time due to the size of the simulation)
This code is not reproducible without downloading such data and editing variables such as basePath
"""
#number density color-coding
import illustris_python.illustris_python as il #library for accessing the IllustrisTNG simulation data
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import kde

def select(array, size, weights):
    sample = np.random.choice(array, size=size, replace=True, p=weights)
    return sample

def to_log12(z): #convert Z total to 12+log(O/H)
    # Assume that oxygen is 36% of the metal mass
    logOH = np.log10((0.36*z)/(0.73*16))
    return logOH + 12

def CDF(xarr, label, xarr2, label2, xlabel, title):
    x2=np.sort(xarr2)
    y2=np.arange(len(xarr2)) / float(len(xarr2))
    plt.plot(x2,y2,label=label2)
    x=np.sort(xarr)
    y=np.arange(len(xarr)) / float(len(xarr))
    plt.plot(x,y,label=label)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.legend()
    
def density(xarr,yarr,xlabel,ylabel,bins):
    nbins=bins
    k = kde.gaussian_kde([xarr,yarr])
    xi, yi = np.mgrid[xarr.min():xarr.max():nbins*1j, yarr.min():yarr.max():nbins*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))
    plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

basePath = '___path___/IllustrisTNG/TNG50-1/output/' #must be edited to match the path of your downloaded data if you want to run the code
fields = ['GFM_Metallicity','StarFormationRate','Coordinates','Masses']
subs_fields = ['SubhaloHalfmassRadType','SubhaloPos','SubhaloGasMetallicity',
               'SubhaloSFR','SubhaloMassType']
subhalos = il.groupcat.loadSubhalos(basePath,33,fields=subs_fields)

id_arr = np.array([])
Mstar_arr = np.array([])
subSFR_arr = np.array([])
Z_total_arr = np.array([])
fraction_arr = np.array([])
totalsfr_lowZ_arr = np.array([])

#model key values
Z_limit=0.3
sfr_weight=0
frac_weight=2.5

def frac(sub_id):
    h=0.6774 #hubble constant in units of [100 km/s/Mpc]
    z=2.00202813925285 #redshift
    SFR = subhalos['SubhaloSFR'][sub_id] #solar masses per year
    if(SFR>0.5):
        Mstar = subhalos['SubhaloMassType'][sub_id][4] * ((10**10)/h) #stellar=4
        if(Mstar>10**7):
            shmr = subhalos['SubhaloHalfmassRadType'][sub_id][4] / ((1+z)*h)
                                        #converting from ckpc/h to kpc ^^^
            Z_total = subhalos['SubhaloGasMetallicity'][sub_id] / 0.0127 #in solar units

            gas_info = il.snapshot.loadSubhalo(basePath,33,sub_id,'gas',fields=fields)
            x = (gas_info['Coordinates'][:,0] - subhalos['SubhaloPos'][sub_id][0]) / ((1+z)*h)
            y = (gas_info['Coordinates'][:,1] - subhalos['SubhaloPos'][sub_id][1]) / ((1+z)*h)
            z = (gas_info['Coordinates'][:,2] - subhalos['SubhaloPos'][sub_id][2]) / ((1+z)*h)
            r = np.sqrt(x**2 + y**2 + z**2)
            Z = gas_info['GFM_Metallicity'] / 0.0127
            sfr = gas_info['StarFormationRate']
            
            #within 10 stellar half mass radii, star-forming only, in lowZ gas
            Z = Z[(r<(10*shmr))*(sfr>0)] 
            sfr = sfr[(r<(10*shmr))*(sfr>0)]
            Z_lowZ = Z[Z < Z_limit]
            sfr_lowZ = sfr[Z < Z_limit]
            
            fraction = len(Z_lowZ)/len(Z) #fraction of SF cells that have a Z < 0.3 solar
            total_sfr = np.sum(sfr_lowZ) #total SF in the lowZ gas
            return sub_id, Mstar, SFR, Z_total, fraction, total_sfr;
        else:
            return 0, 0, 0, 0, 0, 0;
    else:
        return 0, 0, 0, 0, 0, 0;

def cells(sub_id):
    h=0.6774
    z=2.00202813925285
    shmr = subhalos['SubhaloHalfmassRadType'][sub_id][4] / ((1+z)*h)
    gas_info = il.snapshot.loadSubhalo(basePath,33,sub_id,'gas',fields=fields)
    x = (gas_info['Coordinates'][:,0] - subhalos['SubhaloPos'][sub_id][0]) / ((1+z)*h)
    y = (gas_info['Coordinates'][:,1] - subhalos['SubhaloPos'][sub_id][1]) / ((1+z)*h)
    z = (gas_info['Coordinates'][:,2] - subhalos['SubhaloPos'][sub_id][2]) / ((1+z)*h)
    r = np.array(np.sqrt(x**2 + y**2 + z**2) / shmr) #in units of shmr
    Z = np.array(gas_info['GFM_Metallicity'] / 0.0127) #solar
    sfr = np.array(gas_info['StarFormationRate'])
    #^^^ repeat from 'frac' function
    #within 10 stellar half mass radii, star forming only...
    Z = Z[(r<10)*(sfr>0)]
    r2 = r[(r<10)*(sfr>0)]
    sfr2 = sfr[(r<10)*(sfr>0)]
    return r2, Z, sfr2; #arrays

N=len(subhalos['SubhaloSFR']) #7,583,454
for i in range(0,N): #run the frac function for every subhalo in the snapshot
    sub_id, Mstar, SFR, Z_total, fraction, total_sfr = frac(i)
    if (Mstar != 0): #if function returns non-zero values
        #add key values for the filtered subs to their respective arrays
        id_arr = np.append(id_arr, sub_id)
        Mstar_arr = np.append(Mstar_arr, Mstar)
        subSFR_arr = np.append(subSFR_arr, SFR)
        Z_total_arr = np.append(Z_total_arr, Z_total)
        fraction_arr = np.append(fraction_arr, fraction)
        totalsfr_lowZ_arr = np.append(totalsfr_lowZ_arr, total_sfr)
N=id_arr.size


#selecting subhalos
weights = (fraction_arr**frac_weight)*(totalsfr_lowZ_arr**sfr_weight) / np.sum((fraction_arr**frac_weight)*(totalsfr_lowZ_arr**sfr_weight))
S=1000
sample = select(id_arr, S, weights) #random choice function, selects 1000 IDs

position = np.array([])
for n in range(0,S):
    position = np.append(position, np.where(id_arr == sample[n])) #finds position
    position = position.astype(int) #converts array to integers  

Z_total_arr_sample = Z_total_arr[position]
subSFR_arr_sample = subSFR_arr[position]
Mstar_arr_sample = Mstar_arr[position]

logZ = to_log12(Z_total_arr*0.0127)
logZ_sample = to_log12(Z_total_arr_sample*0.0127)
Mstar_log = np.log10(Mstar_arr) #from Mstar to log(Mstar)
Mstar_log_sample = Mstar_log[position]
i = len(Z_total_arr_sample[Z_total_arr_sample>0.3])
print('Fraction of selected subhalos with metallicity > 0.3 solar:', i/S)

def KStest(sample1, sample2):
    print(stats.ks_2samp(sample1, sample2))

print('Z limit = ', Z_limit, '& sfr weighting = ', sfr_weight, '& frac weight = ', frac_weight)
#CDF plots
CDF(logZ_sample,'Z-sample',logZ,'Z-all subs', '12 + log(O/H)',
    'Cumulative Distribution of metallicity in subhalos')
plt.show()
KStest(logZ_sample, logZ)

CDF(subSFR_arr_sample,'SFR-sample',subSFR_arr,'SFR-all subs', 'SFR / solar masses per year',
    'Cumulative Distribution of SFR in subhalos')
plt.xscale('log')
plt.show()
KStest(subSFR_arr_sample, subSFR_arr)

CDF(Mstar_log_sample,'Mstar-sample',Mstar_log,'Mstar-all subs', 'log(Mstar / Msolar)',
    'Cumulative Distribution of Mstar in subhalos')
plt.show()
KStest(Mstar_arr_sample, Mstar_arr)


#selecting cells
id_arr = id_arr.astype(int)
r_all = np.array([])
Z_all = np.array([])
sfr_all = np.array([])
r_sample = np.array([])
Z_sample = np.array([])
sfr_sample = np.array([]) 
for i in range(0,S):
    selected_id = id_arr[position[i]]
    r2, Z, sfr2 = cells(selected_id)
    r_lowZ = r2[Z<Z_limit]
    Z_lowZ = Z[Z<Z_limit] / np.amax(Z)
    sfr_lowZ = sfr2[Z<Z_limit] / np.amax(sfr2)
    
    Z = Z / np.amax(Z) #normalising
    sfr2 = sfr2 / np.amax(sfr2)
    r_all = np.append(r_all, r2) #array of all cells from all 1000 subs
    Z_all = np.append(Z_all, Z)
    sfr_all = np.append(sfr_all, sfr2)

    cell_weights = (sfr_lowZ)/np.sum(sfr_lowZ)
    #picking 1 cell for each subhalo
    r_sample = np.append(r_sample, select(r_lowZ, 1, cell_weights))
    Z_sample = np.append(Z_sample, select(Z_lowZ, 1, cell_weights))
    sfr_sample = np.append(sfr_sample, select(sfr_lowZ, 1, cell_weights))
#CDF plots
CDF(r_sample,'r-sample',r_all,'r-all cells', 'radial separation / shmr',
    'Cumulative Dist. of radial separation of GRBs from subhalo centre')
plt.xscale('log')
plt.show()
KStest(r_sample, r_all)

CDF(Z_sample,'Z-sample',Z_all,'Z-all cells', 'metallicity / max',
    'Cumulative Dist. of metallicity of GRBs in a subhalo')
plt.xscale('log')
plt.show()
KStest(Z_sample, Z_all)

CDF(sfr_sample,'sfr-sample',sfr_all,'sfr-all cells', 'sfr / max',
    'Cumulative Dist. of SF of GRB-originating cells in a subhalo')
plt.xscale('log')
plt.show()
KStest(sfr_sample, sfr_all)

#density plots
density(logZ_sample, Z_sample, 'subhalo 12 + log(O/H)','cell Z / Zmax', 300)
plt.show()
density(subSFR_arr_sample, sfr_sample, 'subhalo SFR / solar masses per year',
        'cell SFR / SFRmax',300)
plt.xscale('log')
plt.show()

#plot(logZ_sample, Z_sample, 'subhalo 12 + log(O/H)', 'cell Z / Zmax')
#plot(subSFR_arr_sample, sfr_sample, 'subhalo SFR / solar masses per year', 'cell SFR / SFRmax')
