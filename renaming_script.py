'''
Be very careful using this script. It can modify folders and files recursively so a small error could effect everything
under the parent directory where this lives.

The purpose is to easily scan through and check for naming convention errors in our filing system and then correct them
if necessary.

Due to Drop Box being case insensitive some sections have to be commented out and run one at a time to work properly.

Ask Mike Flanigan if you have questions.
'''

import os, glob, csv

'''
Uncomment one section at a time and wait for drop box to sync between actions
Place this script in the directory you want to change (recursive == TRUE)
'''

'''
Run this first section first to upper case all directory names and change it so drop box syncs it.
'''
for name in glob.iglob(os.getcwd()+'/**/*',recursive=False):
    if os.path.isdir(name):
        if name[len(name)-2:len(name)] != '_a':
            new_name = name.upper()+'_a'
           try:
                os.rename(name,new_name)
                print(new_name)
            except PermissionError:
                print('!!!!!!!!!!!!! Failed to name:',name,' due to permission error !!!!!!!!!!!!!!!')
        else: print(name)

'''
Run this second (w/o the first bit) to remove the letters from the directory so they're returned to the original name.
'''
##for name in glob.iglob(os.getcwd()+'/**/*',recursive=True):
##    if os.path.isdir(name):
##        if name[len(name)-2:len(name)] == '_a':
##            new_name = name[0:len(name)-2]
##            try:
##                os.rename(name,new_name)
##                print(new_name)
##            except PermissionError:
##                print('!!!!!!!!!!!!! Failed to name:',name,' due to permission error !!!!!!!!!!!!!!!')
##        else: print(name,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! didnt have an _a !!!!!!!!!!!!!!!!!')


'''
This section loads a csv file of manufacturers abbrevs and checks the capitilzation on them.
'''

## load Manufacturer abbrevs
##tot_incorrect_cases = 0
##with open('Abbrevs.csv', 'r') as f:
##    reader = csv.reader(f)
##    Manufacturers = list(reader)
##for Comp in Manufacturers:
##    Comp[0] = '_'+Comp[0]+'_'
##    correct_count = 0
##    incorrect_count = 0
##    na_count = 0
##    print(' ')
##    print('Reviewing:',Comp[0])
##    print(' ')
##    for name in glob.iglob(os.getcwd()+'/**/*',recursive=True):
##        if not os.path.isdir(name):
##            if not Comp[0] in name and Comp[0].lower() in name.lower(): # name is in but wrong case
##                print('wrong case ' ,name)
##                incorrect_count += 1
##            elif Comp[0] in name: # in and case is correct
##                print('correct case' , name)
##                correct_count += 1
##            else: # not in at all
##                na_count += 1
##    print('incorrect casing:',incorrect_count)
##    print('correct casing:',correct_count)
##    print('files without abbrev:',na_count)
##    tot_incorrect_cases += incorrect_count
####    break # only needed if want to stop early
##print(tot_incorrect_cases,' total incorrectly cased names.')


'''
This section renames every solid part with a suffix so that drop box syncs the capitilzation changes.
A sectioin in here can also remove that suffix after dropbox has synced.
'''
## rename every solid part in COTs so dropbox syncs it
##error_count = 0
##for name in glob.iglob(os.getcwd()+'/**/*',recursive=True):
##    i = 0
##    Found = False
##    if not os.path.isdir(name):
##        while not Found:
##            if name[len(name)-i-1:len(name)-i] == '.':
####                print(name[len(name)-i-1:len(name)])
##                if name[len(name)-i-1-4:len(name)].lower() == '_mpf.sldprt': # RENAMING EVERY SLDPRT file if using .lower
##                    
####                    print('RENAME THIS FILE !!!!!!!!!!!!!!!!')
##                    try:
####                        new_name = name[0:len(name)-i-1]+'_MPF.SLDPRT'
####                        os.rename(name,new_name)
##                        print(name)
####                        print(new_name)
##                        removed_new_name = name[0:len(name)-i-1-4]+'.SLDPRT'
####                        os.rename(name,removed_new_name)
##                        print(removed_new_name)
##                    except PermissionError:
##                        print('!!!!!!!!!!!!! Failed to name:',name,' due to permission error !!!!!!!!!!!!!!!')
##                        error_count += 1
##                Found = True
##
##            else: i += 1
##            if i > 20: break
##print(error_count,' errors occurred.')
