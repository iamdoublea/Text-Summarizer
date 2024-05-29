from setuptools import setup
from setuptools import find_packages

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = 'https://github.com/iamdoublea/Text-Summarizer'
AUTHOR_USER_NAME = 'https://github.com/iamdoublea/'
SRC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'contact@aadityaseal.com'

setup(
    name=SRC_REPO,
    version=__version__,
    description="Text Summarizer NLP Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https//github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    project_url={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    }
    )
