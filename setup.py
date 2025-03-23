from setuptools import setup, find_packages

# Read README.md for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='testronaut',
    version='1.0.1',
    description='A CLI tool that bridges code analytics, automated test generation, and smart CI/CD optimization—so your dev workflow scales with your codebase.',
    long_description=long_description,
    long_description_content_type="text/markdown",  # 👈 Very important for markdown formatting
    author='Siddarth Satish',
    author_email='saladguy12@gmail.com',
    url='https://github.com/Dknx8888/grizzy7',
    packages=find_packages(include=['interface', 'interface.*']),
    install_requires=[
        'click',
        'python-dotenv',
        'requests',
        'memory_profiler',
        'google-genai',
        'protobuf'
    ],
    entry_points={
        'console_scripts': [
            'testronaut=interface.cli:main',
        ]
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
