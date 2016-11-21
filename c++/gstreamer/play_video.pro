TEMPLATE = app
TARGET = play_video

MOC_DIR = .tmp
OBJECTS_DIR = .tmp
 
QT = core gui
 
SOURCES +=  main.cpp

# "Uses gstreamer-1.0"
CONFIG += link_pkgconfig
PKGCONFIG += gstreamer-1.0
