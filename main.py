import pandas as pd

mtcars = pd.read_csv('https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv')
print(mtcars)


echo "# tester" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/drakesides/tester.git
git push -u origin master

git config --global user.email "lucasdrakesides@gmail.com"
git config --global user.name "Lucas Drake Sides"


