from setuptools import find_packages, setup

# fake to satisfy mypy
__version__ = "0.0.0"
exec(open("prelabTutor/version.py").read())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai_uni",
    version=__version__,
    description="",
    author="Mayk Caldas",
    author_email="maykcaldas@gmail.com",
    url="https://github.com/",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain_openai",
        "langchainhub",
        "langchainhub",
        "openai",
        "python-dotenv",
        "requests",
        "chromadb",
        "llama_index",
        "streamlit",
        ],
    test_suite="tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)