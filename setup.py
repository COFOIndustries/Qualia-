from setuptools import setup, find_packages

setup(
    name="qualia",
    version="1.0.0",
    description="QUALIA: A multilingual translation tool",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/cofoindustries/qualia",
    packages=find_packages(),
    install_requires=[
        "googletrans==4.0.0-rc1",
    ],
    entry_points={
        "console_scripts": [
            "qualia=qualia.translate:main",  # CLI command: qualia
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
