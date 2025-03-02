from setuptools import setup, find_packages

setup(
    name='suppChatbot',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A support chatbot for answering how-to questions related to Customer Data Platforms (CDPs) using NLP.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'nltk',
        'spacy',
        'beautifulsoup4',
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)