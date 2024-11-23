import os
import sys

scriptDir = os.path.dirname(os.path.abspath(sys.argv[0]))
# The following are the default settings. Edit to change the defaults.
settings = {
    'srcDir': scriptDir,                                    # Source APKs in the script's directory
    'outDir': scriptDir,                                    # Patched APKs written to the script's directory
    'toolsDir': os.path.join(scriptDir, 'tools'),           # The patch tools are downloaded to the 'tools' subdirectory
    'optionsDir': scriptDir,                                # The patch  configuration options are in the 'options' subdirectory
    'keystore': os.path.join(scriptDir, 'patch.keystore'),  # The keystore to sign the patched APKs is next to the script
    'download': {
        'arch': 'arm64-v8a',                                # The architecture of downloaded APKs: armeabi-v7a or arm64-v8a or x86 or x86_64.
        'dpi': 'nodpi'                                      # The DPI of the downloaded APIs: 240dpi, 320dpi, ...
    },
    'defaultPatchSource': 'rv'                              # Select whether the default provider should be ReVanced or ReVancedExtended
}