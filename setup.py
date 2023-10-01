import setuptools

setuptools.setup(
    name="homeline",
    version="2.0.3",
    author="Magnus Eldén",
    description="Wrapper for the Compare It Homeline Api",
    packages=["peaqoffpeak, peaqoffpeak.models"],
    install_requires=[
          'requests',
      ],
)   