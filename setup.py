from setuptools import find_packages,setup

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="Shipment Price Predictor",
    version='0.0.po1',
    author="Sachin",
    author_email="sachindagar477@gmail.com",
    description="Predicts the shipping price based on various factors",
    url="https://github.com/sachin1024/shipment-price-predictor",
    packages=find_packages(),
    install_requires=required
)
