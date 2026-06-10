import os
import shutil

print("-----Welcome to file automation scripts-----")
a=input("Enter the path of your folder: ")
b=input("Enter name/path of the new JPG folder: ")
if not os.path.exists(b):
    os.makedirs(b)
    print(f"Created new folder: {b}")

print("\nAutomation started...")
moved_count = 0

for filename in os.listdir(a):
    
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
        
       
        source_path = os.path.join(a, filename)
        destination_path = os.path.join(b, filename)
        
        shutil.move(source_path, b)
        print(f"-> Moved: {filename}")
        moved_count += 1

print("\n-------------------------------------------")
print(f"Success! Total {moved_count} .jpg files moved successfully.")
print("-------------------------------------------")

