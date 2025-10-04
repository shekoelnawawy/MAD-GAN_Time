import os
import numpy as np
import time

os.makedirs('output', exist_ok=True)
print('-----------------------------------------------------------------------------------------------------------------------------')

# with is like your try .. finally block in this case
with open('experiments/settings/sepsis.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"least\",\n"
train_data[3] = "\"patient\": \"0\",\n"

# and write everything back
with open('experiments/settings/sepsis.txt', 'w') as train_file:
    train_file.writelines(train_data)

os.makedirs(os.path.join('output', 'least'), exist_ok=True)
start_time = time.perf_counter()
os.system('python RGAN.py --settings_file sepsis > ./output/least/train.txt')
end_time = time.perf_counter()
elapsed_time_less = end_time - start_time
print('-----------------------------------------------------------------------------------------------------------------------------')

# with is like your try .. finally block in this case
with open('experiments/settings/sepsis.txt', 'r') as train_file:
    # read a list of lines into data
    train_data = train_file.readlines()

# now change the 2nd line, note that you have to add a newline
train_data[2] = "\"year\": \"all\",\n"
train_data[3] = "\"patient\": \"0\",\n"

# and write everything back
with open('experiments/settings/sepsis.txt', 'w') as train_file:
    train_file.writelines(train_data)

os.makedirs(os.path.join('output', 'all'), exist_ok=True)
start_time = time.perf_counter()
os.system('python RGAN.py --settings_file sepsis > ./output/all/train.txt')
end_time = time.perf_counter()
elapsed_time_all = end_time - start_time
print('-----------------------------------------------------------------------------------------------------------------------------')
print(f"All Patients Elapsed Time: {elapsed_time_all:.6f} seconds")
print(f"Less Vulnerable Elapsed Time: {elapsed_time_less:.6f} seconds")
print('Percentage Decrease One-Class SVM = '+str(((elapsed_time_all-elapsed_time_less)/elapsed_time_all)*100))
