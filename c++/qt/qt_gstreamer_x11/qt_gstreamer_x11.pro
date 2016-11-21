# TEMPLATE = app
# TARGET = qt_gstreamer_x11

MOC_DIR = .tmp
OBJECTS_DIR = .tmp
 
# QT = core gui
 
SOURCES += *.cpp

# "Uses gstreamer-1.0"
CONFIG += link_pkgconfig
PKGCONFIG += gstreamer-1.0 gstreamer-video-1.0
