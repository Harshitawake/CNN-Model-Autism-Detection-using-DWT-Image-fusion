
import os



def rename_sMRI(folder_path):
    files = os.listdir(folder_path)
    print(f'total files :{len(files)}')
    
    mydict={}
    mylist=[]
    for filename in files:
        if filename.endswith(".jpg"):
            name , extension = os.path.splitext(filename)
            parts = name.split("_")
            #print(parts)
            #print(parts[1],(int(parts[-1][-4:])))
            if parts[1] not in mydict:
                mylist=[]
            mylist.append(int(parts[-1][-4:]))
            mydict[parts[1]]=mylist

            #print(parts[1],mylist)
            #print(mydict[parts[1]])
            
    #print(mydict)
    
    for filename in files:
        if filename.endswith(".jpg"):
            name , extension = os.path.splitext(filename)
            parts = name.split("_")
            if parts[1] in mydict:
                myindex=mydict[parts[1]].index(int(parts[-1][-4:]))
                new_filename=parts[1]+f'_{myindex+1}.jpg'
                new_file_path = os.path.join(folder_path, new_filename)
                #print(new_filename)
                if not os.path.exists(new_file_path):
                    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
                else:
                    
                    print(f"Skipping '{new_filename}' as it already exists.")
    print('sMRI Done')
    

    
def rename_fMRI(folder_path):
    files = os.listdir(folder_path)
    for filename in files:
        if filename.endswith(".png"):
            name , extension = os.path.splitext(filename)
            #print(name)
            if len(name)==5:
                
                new_filename=name+'_1.jpg'
                #print(new_filename)
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            else:
                new_filename=name+'.jpg'
                #print(new_filename)
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    print('fMRI Done')


sMRI_folder_path = 'D:/mamtadiproject/data/Child 2-10/sMRI - bkp/Control/'

fMRI_folder_path = 'D:/mamtadiproject/data/Child 2-10/fMRI - bkp/Control/'

#files=os.listdir('D:/mamtadiproject/data/Child 2-10/fMRI - bkp/Autism/')
#print(files)
#rename_sMRI(sMRI_folder_path)
rename_fMRI(fMRI_folder_path)
