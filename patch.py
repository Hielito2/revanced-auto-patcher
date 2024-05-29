#!/usr/bin/python3

"""
A python script to easily patch APKs with ReVanced or ReVanced Extended.
To configure the script's behaviour, edit the default settings below, or run
"python patch.py --help" to see the command-line argument interface help.
"""

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
        'arch': 'arm64-v8a'                                 # The architecture of downloaded APKs: armeabi-v7a or arm64-v8a or x86 or x86_64.
    },
    'defaultPatchSource': 'rv',                             # Select whether the default provider should be ReVanced or ReVancedExtended
    'patchSources': {
        'rv': {
            'patches': {
                'proj': 'revanced/revanced-patches',
                'ver': 'latest',                            # Use 'latest' or specify the desired release version
                'type': 'application/java-archive',         # The content type of the file (for download identification)
            },
            'integrations': {
                'proj': 'revanced/revanced-integrations',
                'ver': 'latest',                            # Use 'latest' or specify the desired release version
                'type': 'application/vnd.android.package-archive', # The content type of the file (for download identification)
            },
            'cli': {
                'proj': 'revanced/revanced-cli',
                'ver': 'latest',                            # Use 'latest' or specify the desired release version
                'type': 'application/java-archive',         # The content type of the file (for download identification)
            },
            'prepend': 'RV '                                # Prepend this to the patched output file names
        },
        'rvx': {
            'patches': {
                'proj': 'inotia00/revanced-patches',
                'ver': 'latest',                            # Use 'latest' or specify the desired release version
                'type': 'application/jar',                  # The content type of the file (for download identification)
            },
            'integrations': {
                'proj': 'inotia00/revanced-integrations',
                'ver': 'latest',                            # Use 'latest' or specify the desired release version
                'type': 'application/vnd.android.package-archive', # The content type of the file (for download identification)
            },
            'cli': {
                'proj': 'inotia00/revanced-cli',
                'ver': 'latest',                            # Use 'latest' or specify the desired release version
                'type': 'application/jar',                  # The content type of the file (for download identification)
            },
            'prepend': 'RVX '                               # Prepend this to the patched output file names
        }
    }
}
# This map helps the auto-downloader interface
# org and repo define an APKMirror link
# arch is an override for the preferred arch setting
appMap = {
    'Amazon Shopping': {
        'package': 'com.amazon.mShop.android.shopping',
        'org': 'amazon-mobile-llc',
        'repo': 'amazon-shopping'
    },
    'Backdrops': {
        'package': 'com.backdrops.wallpapers',
        'org': 'backdrops',
        'repo': 'backdrops-wallpapers',
        'arch': 'noarch'
    },
    'CandyLink VPN': {
        'package': 'com.candylink.openvpn',
        'org': 'liondev-io',
        'repo': 'candylink-vpn',
        'arch': 'universal'
    },
    'Facebook': {
        'package': 'com.facebook.katana',
        'org': 'facebook-2',
        'repo': 'facebook'
    },
    'Icon Pack Studio': {
        'package': 'ginlemon.iconpackstudio',
        'org': 'smart-launcher-team',
        'repo': 'icon-pack-studio',
        'arch': 'noarch'
    },
    'Infinity for Reddit': {
        'package': 'ml.docilealligator.infinityforreddit',
        'org': 'docile-alligator',
        'repo': 'infinity-for-reddit',
        'arch': 'universal'
    },
    'Inshorts': {
        'package': 'com.nis.app',
        'org': 'inshorts-formerly-news-in-shorts',
        'repo': 'inshorts-news-in-60-words-2'
    },
    'Instagram': {
        'package': 'com.instagram.android',
        'org': 'instagram',
        'repo': 'instagram-instagram'
    },
    'irplus': {
        'package': 'net.binarymode.android.irplus',
        'org': 'binarymode',
        'repo': 'irplus-infrared-remote',
        'arch': 'noarch'
    },
    'Lightroom': {
        'package': 'com.adobe.lrmobile',
        'org': 'adobe',
        'repo': 'lightroom'
    },
    'Meme Generator': {
        'package': 'com.zombodroid.MemeGenerator',
        'org': 'zombodroid',
        'repo': 'meme-generator-free',
        'arch': 'universal'
    },
    'Messenger': {
        'package': 'com.facebook.orca',
        'org': 'facebook-2',
        'repo': 'messenger'
    },
    'Mi Fitness': {
        'package': 'com.xiaomi.wearable',
        'org': 'beijing-xiaomi-mobile-software-co-ltd',
        'repo': 'mi-wear-\u5C0F\u7C73\u7A7F\u6234'
    },
    'MyFitnessPal': {
        'package': 'com.myfitnesspal.android',
        'org': 'myfitnesspal-inc',
        'repo': 'calorie-counter-myfitnesspal',
        'arch': 'universal'
    },
    'NetGuard': {
        'package': 'eu.faircode.netguard',
        'org': 'marcel-bokhorst',
        'repo': 'netguard-no-root-firewall',
        'arch': 'universal'
    },
    'Nyx Music Player': {
        'package': 'com.awedea.nyx',
        'org': 'awedea',
        'repo': 'nyx-music-player',
        'arch': 'universal'
    },
    'pixiv': {
        'package': 'jp.pxv.android',
        'org': 'pixiv-inc',
        'repo': 'pixiv',
        'arch': 'noarch'
    },
    'Photomath': {
        'package': 'com.microblink.photomath',
        'org': 'google-inc',
        'repo': 'photomath',
        'arch': 'universal'
    },
    'Recorder': {
        'package': 'com.google.android.apps.recorder',
        'org': 'google-inc',
        'repo': 'google-recorder'
    },
    'Reddit': {
        'package': 'com.reddit.frontpage',
        'org': 'redditinc',
        'repo': 'reddit',
        'arch': 'universal'
    },
    'Solid Explorer': {
        'package': 'pl.solidexplorer2',
        'org': 'neatbytes',
        'repo': 'solid-explorer-beta'
    },
    'Sony Headphones Connect': {
        'package': 'com.sony.songpal.mdr',
        'org': 'sony-corporation',
        'repo': 'sony-headphones-connect'
    },
    'Strava': {
        'package': 'com.strava',
        'org': 'strava-inc',
        'repo': 'strava-running-and-cycling-gps',
        'arch': 'universal'
    },
    'Sync for Lemmy': {
        'package': 'io.syncapps.lemmy_sync',
        'org': 'sync-apps-ltd',
        'repo': 'sync-for-lemmy'
    },
    'TickTick': {
        'package': 'com.ticktick.task',
        'org': 'ticktick-limited',
        'repo': 'ticktick-to-do-list-with-reminder-day-planner'
    },
    'TikTok': {
        'package': 'com.ss.android.ugc.trill',
        'org': 'tiktok-pte-ltd',
        'repo': 'tik-tok'
    },
    'Trakt': {
        'package': 'tv.trakt.trakt',
        'org': 'trakt',
        'repo': 'trakt',
        'arch': 'universal'
    },
    'Tumblr': {
        'package': 'com.tumblr',
        'org': 'tumblr-inc',
        'repo': 'tumblr',
        'arch': 'universal'
    },
    'Twitch': {
        'package': 'tv.twitch.android.app',
        'org': 'twitch-interactive-inc',
        'repo': 'twitch',
        'arch': 'universal'
    },
    'VSCO': {
        'package': 'com.vsco.cam',
        'org': 'vsco',
        'repo': 'vsco-cam'
    },
    'WarnWetter': {
        'package': 'de.dwd.warnapp',
        'org': 'deutscher-wetterdienst',
        'repo': 'warnwetter',
        'arch': 'universal'
    },
    'Windy.app': {
        'package': 'co.windyapp.android',
        'org': 'windy-weather-world-inc',
        'repo': 'windy-wind-weather-forecast',
        'arch': 'universal'
    },
    'X': {
        'package': 'com.twitter.android',
        'org': 'x-corp',
        'repo': 'twitter',
        'arch': 'universal'
    },
    'Youtube': {
        'package': 'com.google.android.youtube',
        'org': 'google-inc',
        'repo': 'youtube'
    },
    'Youtube Music': {
        'package': 'com.google.android.apps.youtube.music',
        'org': 'google-inc',
        'repo': 'youtube-music'
    },
    'Yuka': {
        'package': 'io.yuka.android',
        'org': 'yuka-apps',
        'repo': 'yuka-food-cosmetic-scan',
        'arch': 'universal'
    }
}

import argparse
import glob
import json
import re
import shutil
import subprocess
import tempfile
import textwrap
import urllib.request

class Patcher:
    tools = ['cli', 'patches', 'integrations']

    def __init__(self, args):
        patchSourceData = args.patchSrc
        self.outPrepend = patchSourceData['prepend']
        self.outDir = args.outDir
        Patcher.__ensureDirectory(self.outDir)
        self.toolsDir = args.toolsDir
        Patcher.__ensureDirectory(self.toolsDir)
        self.optionsDir = args.optionsDir
        Patcher.__ensureDirectory(self.optionsDir)
        self.keystorePath = args.keystore
        Patcher.__ensureDirectory(os.path.dirname(self.keystorePath))
        for tool in self.tools:
            Patcher.__ensureTool(
                self.toolsDir,
                project=patchSourceData[tool]['proj'],
                version=getattr(args, tool + '_version'),
                content_type=patchSourceData[tool]['type'])
        self.toolPaths = {
            i: glob.glob(os.path.join(self.toolsDir, '*{}*'.format(i)))[0] for i in self.tools
        }

    @staticmethod
    def CheckJava():
        try:
            result = subprocess.run(
                ['java', '-XshowSettings', '-version'],
                stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=True)
            match = re.search(
                r'java\.class\.version = (\d+)(?:\.\d+)+', result.stderr.decode('ascii', 'ignore'))
            if (not match or int(match[1]) < 55):
                print('### The installed java version is too old. Please update it.')
                return False
        except subprocess.CalledProcessError(e):
            print('### Error running java! Please install it and make sure it is in the path.')
            return False
        return True

    def Patch(self, srcPath, optionsPath = None):
        srcFile = os.path.basename(srcPath)
        outPath = os.path.join(self.outDir, self.outPrepend + srcFile)
        optionsFile = optionsPath if optionsPath else os.path.splitext(Patcher.__normalFileName(srcFile))[0] + '.json'
        tempDir = os.path.join(tempfile.gettempdir(), 'revanced-resource-cache')
        print('### Patching {}...'.format(srcFile))
        try:
            subprocess.run([
                'java', '-jar',
                self.toolPaths['cli'], 'patch',
                '--patch-bundle=' + self.toolPaths['patches'],
                '--merge=' + self.toolPaths['integrations'],
                '--options=' + os.path.join(self.optionsDir, optionsFile),
                '--keystore=' + self.keystorePath,
                '--temporary-files-path=' + tempDir,
                '--out=' + outPath,
                srcPath
            ], stdout=sys.stdout, stderr=sys.stderr, check=True)
            print('### Finished patching {} successfully!'.format(os.path.abspath(outPath)))
        except subprocess.CalledProcessError:
            print('### Failed to patch {}!'.format(srcFile))
        try:
            # Purge the temp directory after patching (the built-in purger likes to fail)
            shutil.rmtree(tempDir)
        except:
            pass

    def DownloadAndPatch(self, appId):
        apkPath = self.Download(appId)
        if apkPath:
            self.Patch(apkPath, os.path.join(scriptDir, appId + '.json'))
            os.remove(apkPath)
        try:
            os.rmdir(os.path.dirname(apkPath))
        except:
            pass

    def Download(self, appId):
        self.__ensureApkmd()

        appData = appMap[appId]
        try:
            appVer = self.__getAppVersion(appData['package'])
        except subprocess.CalledProcessError:
            print('### Error: The patcher could not be called.'.format(appId))
            return None
        except RuntimeError:
            print('### Error: {} is not supported by the patcher.'.format(appId))
            return None
        apkmdConfig = {
            'options': {
                'arch': appData['arch'] if 'arch' in appData.keys() else settings['download']['arch'],
            },
            'apps': [{
                'name': '{} {}'.format(appId, appVer if appVer else 'latest'),
                'org': appData['org'],
                'repo': appData['repo']
            }]
        }
        if appVer != None:
            apkmdConfig['apps'][0].update({'version': appVer})

        print('### Downloading {}...'.format(appId + (' ' + appVer if appVer else '')))

        fd, configPath = tempfile.mkstemp(suffix='.json')
        with os.fdopen(fd, 'w') as file:
            json.dump(apkmdConfig, file)

        try:
            # Try downloading the correct arch version
            subprocess.run(
                [self.apkmdPath, configPath], cwd=tempfile.gettempdir(),
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                check=True)
            path = os.path.join(
                tempfile.gettempdir(), 'downloads', apkmdConfig['apps'][0]['name'] + '.apk')
            if not os.path.exists(path):
                print('### Failed to find a correct version of {} or blocked by server!'.format(appId))
                return None
            return path
        except subprocess.CalledProcessError:
            print('### Failed to download {}!'.format(appId))
            return None
        finally:
            os.remove(configPath)

    def __getAppVersion(self, appPackage):
        result = subprocess.run([
            'java', '-jar',
            self.toolPaths['cli'], 'list-patches',
            '--filter-package-name=' + appPackage,
            '--with-versions',
            '--with-packages',
            self.toolPaths['patches']
        ], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True)
        output = result.stdout.decode('ascii', 'ignore')
        if not appPackage in output:
            raise RuntimeError("App unsupported by patcher.")
        versions = re.findall(r'^\s*(\d+\.\d+(?:\.\d+)*)\s*$', output, re.MULTILINE)
        versions = [tuple(map(int, x.split('.'))) for x in versions]
        versions.sort(reverse=True)
        if not versions:
            return None
        return '.'.join(str(x) for x in versions[0])

    @staticmethod
    def __ensureDirectory(directory):
        '''Ensures that the path's directory exists'''
        try:
            os.makedirs(directory)
        except FileExistsError:
            pass

    @staticmethod
    def __normalFileName(path):
        '''Removes version strings from the file name'''
        regex = r'\b\s*v?\d+(?:\.\d+)*(?:-[^\s]*)?\b'
        return re.sub(regex, '', path)

    def __ensureApkmd(self):
        if hasattr(self, 'apkmdPath'):
            return
        Patcher.__ensureTool(
            self.toolsDir,
            project='tanishqmanuja/apkmirror-downloader',
            version='latest',
            name_filter='apkmd.exe' if os.name == 'nt' else 'apkmd' if os.name == 'posix' else None
        )
        self.apkmdPath = glob.glob(os.path.join(self.toolsDir, 'apkmd*'))[0]

    @staticmethod
    def __ensureTool(
        directory, project, version = 'latest',
        content_type = None, name_filter = None):
        '''Prepares one ReVanced tool'''

        def clearExistingTools(directory, assetName):
            '''Deletes older versions of the given tool'''
            regex = r'^([^\d]*)v?\d+(?:\.\d+(?:\.\d+)?)?[^\d]*(\.[^\.]+)$'
            assetGlob = re.sub(regex, r'\1*\2', assetName)
            for file in glob.glob(os.path.join(directory, assetGlob)):
                os.remove(file)

        if version != 'latest':
            version = 'tags/v' + version.lstrip('v')
        url = 'https://api.github.com/repos/{0}/releases/{1}'.format(project, version)
        releaseData = json.loads(urllib.request.urlopen(url).read())
        for asset in releaseData['assets']:
            if ((not content_type or asset['content_type'] == content_type) and
                (not name_filter or re.match('^{}$'.format(name_filter), asset['name']))):
                assetName = asset['name']
                assetVer = releaseData['tag_name'].lstrip('v')
                if assetVer not in assetName:
                    assetName = os.path.splitext(assetName)
                    assetName = ''.join((assetName[0], '-', assetVer, assetName[1]))
                assetPath = os.path.join(directory, assetName)
                if (not os.path.exists(assetPath)):
                    print('### Downloading tool {}...'.format(assetName))
                    Patcher.__ensureDirectory(directory)
                    clearExistingTools(directory, assetName)
                    assetUrl = asset['browser_download_url']
                    urllib.request.urlretrieve(assetUrl, assetPath)

def main():
    def argCheck(x):
        arg = next((j for j, l in ((i, i.casefold()) for i in appMap.keys()) if l == x.casefold()), None)
        if not arg: arg = x if os.path.exists(x) else None
        if not arg: raise argparse.ArgumentTypeError("file or app not found: " + x)
        return arg
    parser = argparse.ArgumentParser(
        prog='ReVanced Auto Patcher',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''\
            Selectable app names:
                                    "{}"
            '''.format('", "'.join(sorted(appMap.keys())))))
    parser.add_argument(
        'files or apps', nargs='*',
        type=argCheck,
        default=glob.glob(os.path.join(settings['srcDir'], '*.apk')),
        help='One or more APK file to patch or app name(s) to download and patch.\n' +
             'Patching all APKs in the default source directory if unspecified.\n' +
             'See available app names below.')
    parser.add_argument('--keystore', '-k', default=os.path.abspath(settings['keystore']), help='The path of the keystore file with which to sign the APKs (default: %(default)s)')
    parser.add_argument('--optionsDir', default=os.path.abspath(settings['optionsDir']), help='The directory to store patch options files in (default: %(default)s)')
    parser.add_argument('--outDir', '-o', default=os.path.abspath(settings['outDir']), help='The directory to write patched APKs to (default: %(default)s)')
    parser.add_argument(
        '--patchSrc', choices=settings['patchSources'], default=settings['defaultPatchSource'],
        type=lambda x : settings['patchSources'][x], help='The patch source to use. Use "rv" for ReVanced and "rvx" for ReVanced Extended (default: %(default)s).')
    parser.add_argument('--toolsDir', default=os.path.abspath(settings['toolsDir']), help='The directory to store tools and patches in (default: %(default)s)')
    for tool in Patcher.tools:
        parser.add_argument(
            '--{}-version'.format(tool),
            type=lambda str : str if re.match(r'^latest|v?\d+(?:\.\d+)*(?:-[^ ]+)?$', str) else raise_(argparse.ArgumentTypeError("invalid version")),
            default=settings['patchSources'][settings['defaultPatchSource']][tool]['ver'], help='The tool version to use (default: %(default)s)')
    args = parser.parse_args()

    if not Patcher.CheckJava():
        exit(1)

    patcher = Patcher(args)
    for path in getattr(args, 'files or apps'):
        if path in appMap.keys():
            patcher.DownloadAndPatch(path)
        else:
            patcher.Patch(path)

if __name__ == "__main__":
    main()