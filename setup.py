from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="scrapgpt",
    version="1.1.0",
    description="Python library for scraping ChatGPT",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Dusk Light",
    packages=["scrapgpt"],
    zip_safe=False,
    project_urls={
        "Documentation": "https://github.com/dusklight00/scrapgpt",
    },
    install_requires=[
        "webscapy"
    ]
)