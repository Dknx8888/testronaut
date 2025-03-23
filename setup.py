from setuptools import setup, find_packages

setup(
    name='testronaut',
    version='0.1.16',
    description='A CLI tool that bridges code analytics, automated test generation, and smart CI/CD optimization—so your dev workflow scales with your codebase.',
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
        # Include any additional Python packages your CLI needs
    ],
    entry_points={
    'console_scripts': [
        'testronaut=interface.cli:main',
    ]
    },
    include_package_data=True,  # Ensures non-Python files (like .js assets) are included.
    # package_data={
    #     "interface": ["index.mjs", "package.json", "*.js"]
    # },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update if you choose a different license.
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
