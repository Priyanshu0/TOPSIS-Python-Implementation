import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis_101883059-Priyanshu_Tuli", # Replace with your own username
    version="0.1",
    author="Priyanshu Tuli",
    author_email="priyanshu1tuli@gmail.com",
    description="A python implementation of TOPSIS method for multiple criteria decision making",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Priyanshu0/TOPSIS-Python-Implementation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)