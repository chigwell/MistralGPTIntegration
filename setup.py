from setuptools import setup, find_packages

setup(
    name='MistralGPTIntegration',
    version='2025.5.180912',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='Integration utility for Mistral AI API to provide GPT-based functionalities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/MistralGPTIntegration',
    packages=find_packages(),
    install_requires=[
        'mistralai',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
