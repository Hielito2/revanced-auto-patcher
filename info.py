# This map configures usable patch sources.
# * rv defines ReVanced, rvx defines ReVanced Extended.
#   Each defines 3 tools: patches, integrations, cli, which are downloaded from github:
#   * proj field defines the github project.
#   * ver defines the target tool version to download (latest by default).
#   * type defines the MIME type of the binary to download.
# * subdir defines the subdir under the tools dir to which to download. Avoids RV/RVX collisions.
# * prepend defines a tag to put before the patched executable name.
patchSources = {
    'rv': {
        'cli': {
            'proj': 'revanced/revanced-cli',
            'ver': 'latest',
            'type': 'application/java-archive',
        },
        'patches': {
            'proj': 'revanced/revanced-patches',
            'ver': 'latest',
            'type': 'text/plain',
        },
        'subdir': 'RV',
        'prepend': 'RV '
    },
    'rvx': {
        'patches': {
            'proj': 'inotia00/revanced-patches',
            'ver': 'latest',
            'type': 'application/jar',
        },
        'integrations': {
            'proj': 'inotia00/revanced-integrations',
            'ver': 'latest',
            'type': 'application/vnd.android.package-archive',
        },
        'cli': {
            'proj': 'inotia00/revanced-cli',
            'ver': 'latest',
            'type': 'application/jar',
        },
        'subdir': 'RVX',
        'prepend': 'RVX '
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