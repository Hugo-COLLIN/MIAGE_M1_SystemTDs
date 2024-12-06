#! /usr/bin/python3
import sys
import os
import time

def synchronize_process(process_num):
    # Define synchronization files
    sync_dir = "/tmp/rendezvous/"
    os.makedirs(sync_dir, exist_ok=True)
    
    ready_file = f"{sync_dir}process{process_num}_ready"
    all_ready_file = f"{sync_dir}all_ready"
    
    print(f"P{process_num} : Bonjour")
    print(f"P{process_num} : Création et initialisation des fichiers de synchronisation")
    
    # Create ready file
    with open(ready_file, 'w') as f:
        f.write(str(os.getpid()))
    
    print(f"P{process_num}: Je suis prêt")
    
    # Check if all processes are ready
    def check_all_ready():
        return all(os.path.exists(f"{sync_dir}process{i}_ready") for i in range(1, 4))
    
    # Wait for all processes to be ready
    while not check_all_ready():
        time.sleep(0.1)
    
    # Create all_ready file to signal synchronization point
    with open(all_ready_file, 'w') as f:
        f.write("Synchronization point")
    
    print(f"P{process_num}: Tu est prêt ?")
    
    # Ensure all processes see the all_ready file
    time.sleep(0.2)
    
    print(f"P{process_num}: Merci d'être venu !")
    print(f"P{process_num} : fin")
    
    # Optional: cleanup
    os.remove(ready_file)
    if process_num == 3:  # last process cleans up all files
        os.remove(all_ready_file)

def main():
    # Ensure a process number is provided
    if len(sys.argv) != 2:
        print("Usage: ./6.2.py <process_number>")
        sys.exit(1)
    
    # Get the process number from command-line argument
    process_num = int(sys.argv[1])
    
    # Run the synchronization logic
    synchronize_process(process_num)

if __name__ == '__main__':
    main()