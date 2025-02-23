# Create New Venv
manishkumarsaraf@Manishs-MBP-2 OGM.Bots.Streamlit.Project1 % python3.12 -m venv .venv_p312
# Venv Path:
cd '/Users/manishkumarsaraf/Library/Mobile Documents/com~apple~CloudDocs/OGM/OGM.Bots/OGM.Bots.Streamlit.Project1'
source .venv_p312/bin/activate
deactivate
# Reach App directory
cd '/Users/manishkumarsaraf/Library/Mobile Documents/com~apple~CloudDocs/OGM/OGM.Bots/OGM.Bots.Streamlit.Project1/OGM.insy/src/app'

# Install jupyter lab
pip install jupyter lab
 # Run streamlit
streamlit run mainVectorIndex.p


## Github
# Check Current Remotes:
(.venv_p312) manishkumarsaraf@MacBookPro OGM.insy % git remote -v
origin  https://OGMWorldWide@dev.azure.com/OGMWorldWide/OGM.MLOPS.Azure/_git/OGM.insy (fetch)
origin  https://OGMWorldWide@dev.azure.com/OGMWorldWide/OGM.MLOPS.Azure/_git/OGM.insy (push)
# Add GitHub as a Remote
git remote add github <your-github-repo-url>
git remote add github https://github.com/mksaraf/ogm.insy2.git
# Verify Remote Version
(.venv_p312) manishkumarsaraf@MacBookPro OGM.insy % git remote -v
github  https://github.com/mksaraf/ogm.insy2.git (fetch)
github  https://github.com/mksaraf/ogm.insy2.git (push)
origin  https://OGMWorldWide@dev.azure.com/OGMWorldWide/OGM.MLOPS.Azure/_git/OGM.insy (fetch)
origin  https://OGMWorldWide@dev.azure.com/OGMWorldWide/OGM.MLOPS.Azure/_git/OGM.insy (push)
# Push to Both Remotes:
git push origin main
git push github main

# Pull
git pull github main

# Remove github remote
git remote remove github
# Push to new repo in github
git init
git add .
git commit -m "Initial commit with specific folders"
git remote add github https://github.com/mksaraf/ogm.insy2.git


# 