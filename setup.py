from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read()
    
setup(
    name="image_processing_2025",
    version="0.0.4",
    author="Barbara",
    author_email="",
    description="",
    long_description=page_description,
    long_description_content_type= "text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',

)    