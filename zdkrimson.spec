# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_data_files

# Modify these paths as needed
source_folder = 'C:/Users/User/Documents/mt/Sublime Text/Projects/zdkrimson'
# static_folder = f'{source_folder}/static'

# source_folder = ''

a = Analysis(
    ['main.py'],  # Replace with your main script
    pathex=[source_folder],
    binaries=[],
    datas=[
        (f'{source_folder}/favicon.ico', '.'),
        (f'{source_folder}/help.css', 'static'),
        (f'{source_folder}/help.html', 'static'),
        (f'{source_folder}/help.js', 'static'),
        (f'{source_folder}/index.css', 'static'),
        (f'{source_folder}/index.html', 'static'),
        (f'{source_folder}/index.js', 'static'),
        (f'{source_folder}/instances.css', 'static'),
        (f'{source_folder}/instances.html', 'static'),
        (f'{source_folder}/instances.js', 'static'),
        (f'{source_folder}/LICENSE', '.'),
        # (f'{source_folder}/main.py', '.'),
        # (f'{source_folder}/modelfetch.py', '.'),
        (f'{source_folder}/settings.css', 'static'),
        (f'{source_folder}/settings.html', 'static'),
        (f'{source_folder}/settings.js', 'static'),
        (f'{source_folder}/assets', 'assets'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='zdkrimson',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # Disable UPX compression
    console=True,  # Run in console mode
    cipher=None,
    icon=f'{source_folder}/favicon.ico',  # Path to icon file
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,  # Disable UPX compression
    cipher=None,
    clean=True,  # Clean the build directory
    name='zdkrimson'
)
