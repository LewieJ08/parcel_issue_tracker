from setuptools import setup, find_packages

setup(
    name="parcel_issue_tracker",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "matplotlib",
        "pandas",
    ],  
    entry_points={  
        "console_scripts": [
            "parcel-issue-tracker=parcel_tracker_issue.main:main" 
        ]
    },
    author="Lewie Jackson",
    author_email="LewieJ08@gmail.com",
    description="A simple data visualisation program for external csv data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LewieJ08/parcel_issue_tracker",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)