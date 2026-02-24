import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="end-to-end-ML-project"
AUTHOR_USER_NAME="AmitPrajapati53"
SRC_REPO="mlproject"
AUTHOR_EMAIL="amitprajapati.sspu@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "bug tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)