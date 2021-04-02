import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyzoho-fulfillmenet-sastiam",
    version="0.0.1",
    author="sastiam",
    author_email="sfrancia@gmail.com",
    description="Dialogflow agent fulfillment library for Zohobot integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sastiam/pyzoho-fulfillment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)