import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__ ="0.0.0"
Author_User_Name= "ankita123429"
SRC_REPO="Textsummarizationapp"
AUTHOR_EMAIL="ankita.kathed@gmail.com"
REPO_NAME="text-summarization-app"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author_user_name=Author_User_Name,
    author_email=AUTHOR_EMAIL,
    description="A samll package on text",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{Author_User_Name}/{REPO_NAME}", 
    project_urls={
         "Bug_Tracker":f"https://github.com/{Author_User_Name}/{REPO_NAME}/issues"

     },
     package_dir={"":"src"},
     packages=setuptools.find_packages(where="src")
)




