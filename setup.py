from setuptools import setup, find_packages

setup(
    name="logger_service",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Your logger uses standard library logging
    description="Logging service for microservices",
)