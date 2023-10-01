import setuptools

setuptools.setup(
    name="peaqoffpeak",
    version="0.1.0",
    author="Magnus Eldén",
    description="Partial wrapper for Svk Mimer Api",
    packages=["peaqoffpeak, peaqoffpeak.models"],
    install_requires=[
          'requests',
      ],
)   