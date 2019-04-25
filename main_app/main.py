import subprocess
import os
import sys

def determine_result_status(result_file_path):
    failed_occurence = count_word_occurence_of_file(result_file_path, "FAILED")
    if(failed_occurence > 0):
        return False
    else:
        return True

def count_word_occurence_of_file(file_path, word):
    file_object = open(file_path,"r")
    file_content = file_object.read().upper()
    number_of_occurence = file_content.count(word.upper())
    return number_of_occurence

def find_last_created_folder(folder_path):
    parent_folder_content = os.listdir(folder_path)
    older_folder_name = "no one"
    older_folder_time = 0
    for folder_name in parent_folder_content:
        folder_edit_time = os.path.getctime(folder_path+"/"+folder_name)
        if older_folder_time < folder_edit_time:
            older_folder_time = folder_edit_time
            older_folder_name = folder_name
    return folder_path+"/"+older_folder_name

def execute():
    process = subprocess.Popen("../sub_process/test_simulator.sh", shell=True, stdout=subprocess.PIPE)
    process.wait()
    current_result_folder = find_last_created_folder("../result_folder")
    current_result_file_path = current_result_folder+"/result.html"
    test_status = determine_result_status(current_result_file_path)
    print test_status
    #Read some file content / make a mail & send a mail
    print 0 if test_status else 1 
    sys.exit(0 if test_status else 1)

if __name__ == '__main__':
    execute()