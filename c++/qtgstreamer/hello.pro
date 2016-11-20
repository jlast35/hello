TEMPLATE = app
TARGET = hello_gstreamer
 
QT = core gui
 
SOURCES +=  main.cpp

# "Uses gstreamer-1.0"
CONFIG += link_pkgconfig
PKGCONFIG += gstreamer-1.0 gstreamer-video-1.0
