from setuptools import setup, find_packages

setup(
    name="interview",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "interview-service=src.main:main"
        ]
    },
    install_requires=[
        "fastapi",
        "uvicorn",
        "transformers",
        "google-cloud-storage"
    ]
)