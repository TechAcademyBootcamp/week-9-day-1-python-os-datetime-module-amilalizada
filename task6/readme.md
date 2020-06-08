# Task: Create a Coder class.
init (self, project_name) - must create a coder project within the init function.
create_package (self, package_name) - must create a package (folder) within the project
change_directory (self, package_name = 'project_dir') - should change the directory we are in to package_name directory. If package_name cannot be sent, or if it is sent as 'project_dir', then we must tell the project directory where we are.
print_working_directory (self): must print the directory we are in.
create_file (self, file_name) - should create a file named file_name where we make the change directory
write_code (self, file_name, code) - must write code in the given file
run_code (self, file_name) must run the file where we are.