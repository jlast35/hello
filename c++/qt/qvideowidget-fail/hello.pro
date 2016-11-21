TEMPLATE = app
TARGET = qvideowidget-fail
 
QT = core gui
 
SOURCES +=  main.cpp
LIBS += -lgstapp-1.0

# "Uses gstreamer-1.0"
CONFIG += link_pkgconfig
PKGCONFIG += gstreamer-1.0 
# gstreamer-video-1.0 gstreamer-plugins-base-1.0
