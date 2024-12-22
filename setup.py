from setuptools import setup, find_packages

setup(
    name="email_verification",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="Musarra-Passari",
    author_email="cityparkme@gmail.com",
    description="Un package per inviare codici di verifica via email",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuo_username/email_verification",  # URL del repository (opzionale)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
