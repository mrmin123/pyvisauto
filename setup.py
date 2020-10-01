import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvisauto",
    version="1.0.3",
    author="Minyoung Choi",
    author_email="minyoung.choi@gmail.com",
    description="pyvisauto - a vision-based automation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrmin123/pyvisauto",
    packages=['pyvisauto'],
    install_requires=[
        'opencv-contrib-python-headless~=4.1.2.30',
        'pillow~=7.2.0',
        'pyautogui~=0.9.48',
        'pytesseract~=0.3.0',
        'numpy~=1.17.4',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4.*, <3.8',
)
