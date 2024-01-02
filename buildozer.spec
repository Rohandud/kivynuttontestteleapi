[app]

# (str) Title of your application
title = ButtonApp

# (str) Package name
package.name = buttonapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyTelegramBotAPI

# (str) Custom source folders for requirements
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyTelegramBotAPI

# (str) Custom source folders for requirements
# Sets custom source for the requirements so that buildozer will look
# for a folder named 'custom_requirements' in the root of the app and
# use it as the source.
# source.custom_requirements = custom_requirements

# (list) Garden requirements (>=2.1.0, only use versions compatible with your Kivy & Python versions)
#garden_requirements = kivy

# (str) The license of your software
#license = GPL

# (str) Package version
version = 1.0

# (list) Application categories
#categories = Tool

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (string) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (string) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Application build permissions
# android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if build settings are too big
warn_on_buildsize = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (int) Seed for random parts of the build process
# The default is set by the python random module.
# This is used by Android, but not Android NDK builds.
# android.ndk_build_param = APP_CFLAGS += " -std=c99"

# (int) Target Android API, should be as high as possible.
# android.api = 27

# (int) Android API to use
# android.api = 27

# (int) Minimum API required
# android.minapi = 21

# (int) Android NDK version to use
#android.ndk = 19b

# (int) Android NDK version to use for JNI
#android.ndk_path = jni

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path = /opt/android-ndk-r19c

# (str) Android NDK version to use for JNI
# android.ndk_version = 19b

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.arch = armeabi-v7a

# (int) android add default libraries
# android.ndk_captures = arm-linux-androideabi-clang
# android.add_default_libraries = True

# (int) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.renpy.android.PythonActivity

# (int) Android app theme, default is okay for Kivy-based app
# android.app_theme = @android:style/Theme.NoTitleBar

# (list) Pattern to whitelist for the whole project
# source.whitelist_patterns = assets/*,res/drawable/*
# (list) Pattern to whitelist for the whole project
# source.whitelist_patterns = assets/*,res/drawable/*

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
# (should match the corresponding option in the AndroidManifest.xml file)
# android.orientation = landscape

# (bool) Indicate whether the screen should stay on
# android.wakelock = False

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so

# (list) Android additional libraries to copy into libs/x86
#android.add_libs_x86 = libs/android_x86/*.so

# (list) Android additional libraries to copy into libs/arm64-v8a
#android.add_libs_arm64_v8a = libs/android_arm64_v8a/*.so

# (list) Android additional libraries to copy into libs/x86_64
#android.add_libs_x86_64 = libs/android_x86_64/*.so

# (bool) Automatically package any system Python modules
#android.bootstrap = sdl2

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android packaging mode, one of 'apk', 'aab' or 'apk-bundle'
#android.arch = armeabi-v7a

# (str) Android packaging mode, one of 'apk', 'aab' or 'apk-bundle'
#apk-bundle = False

# (list) Android ADB whitelist
#android.adb_whitelist = False

# (int) android.app_bundle = False

# (int) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (int) Android logcat buffers to include
# android.logcat_filters = *:S python:D

# (int) Compile platform dependent parts of python packages as .so
# --compile is added to python args and any entries in compile_ext that
# match one of these patterns are compiled.
#android.ndk_captures = arm-linux-androideabi-clang
#android.add_default_libraries = True

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process.
#android.add_jars = foo.jar,bar.jar,path/to/more/jars.jar

# (bool) Enable the new Android layout
# android.new_layout = True

# (str) Java class that should be used for the splash screen
# android.splash_screen = org.test.splashscreen.SplashScreen

# (str) Relative path to the obb file.
# android.obb_filename = %(source.dir)s/main.obb

# (str) Key for signing the debug apk.
# android.signing.debug = True

# (str) Key for signing the release apk.
# android.signing.release = True

# (str) URL of the Android NDK (if it doesn't exist, it's downloaded.)
#android.ndk
