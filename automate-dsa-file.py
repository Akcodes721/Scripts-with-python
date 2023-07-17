import git

# Initialize the repository
repo = git.Repo('/home/akshayk721/githubtuto')

# Set the desired branch
branch_name = 'master'
repo.git.checkout(branch_name)

# Add, commit, and push the changes
repo.git.add('--all')
repo.index.commit('Daily code update')
origin = repo.remote(name='origin')
origin.push()
