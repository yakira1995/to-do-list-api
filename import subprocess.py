import subprocess

# Change directory to your project
subprocess.run(["cd", "path/to/your/project"], shell=True)

# Initialize a git repository
subprocess.run(["git", "init"], shell=True)

# Add all files to staging
subprocess.run(["git", "add", "."], shell=True)
# Check the status of the git repository
subprocess.run(["git", "status"], shell=True)
# Commit changes with a message
subprocess.run(["git", "commit", "-m", "Initial commit for To-Do List API project"], shell=True)
# Removed invalid line as the commit is already handled above

