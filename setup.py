from setuptools import setup, find_packages
import os

# A list of all subdirectories containing .pyc files
pyc_subdirectories = []
versions_dir = os.path.join('plc_conn', '__versions')
if os.path.exists(versions_dir) and os.path.isdir(versions_dir):
    for version_subdir in os.listdir(versions_dir):
        if os.path.isdir(os.path.join(versions_dir, version_subdir)):
            pyc_subdirectories.append(os.path.join('__versions', version_subdir, '*.pyc'))

setup(
    name='plc_conn',
    version='0.1.0',
    author='<Your Name>', # Placeholder, user can change
    author_email='<your_email@example.com>', # Placeholder, user can change
    description='A Python library for PLC communication',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='<project_url>', # Placeholder, user can change
    packages=find_packages(include=['plc_conn', 'plc_conn.*']),
    package_data={
        'plc_conn': pyc_subdirectories,
    },
    python_requires='>=3.8',
    install_requires=[
        # No external dependencies for now
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License', # Assuming MIT based on typical open source projects
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
)
