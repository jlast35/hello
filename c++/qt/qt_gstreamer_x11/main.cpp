 #include <gst/video/videooverlay.h>
#include <QApplication>
#include <QWidget>

int main(int argc, char *argv[])
{
  // This is an event-driven Qt GUI application
  QApplication *app = new QApplication(argc, argv);

  // when the last UI window is closed, also exit the app event loop
  app->connect(app, SIGNAL(lastWindowClosed()), app, SLOT(quit()));

  // Create and display a QWidget to render video on
  QWidget video_widget;
  video_widget.show();

  // initialize GStreamer
  gst_init(&argc, &argv);

  // Setup a minimal GStreamer video test pipeline using an x11 video sink
  GstElement *pipeline = gst_pipeline_new("xvoverlay");
  GstElement *src = gst_element_factory_make("videotestsrc", NULL);
  GstElement *sink = gst_element_factory_make("xvimagesink", NULL);
  gst_bin_add_many(GST_BIN(pipeline), src, sink, NULL);
  gst_element_link(src, sink);

  // Make GStreamer's x11 videosink render to the x11 window ID associated with the video_widget
  gst_video_overlay_set_window_handle(GST_VIDEO_OVERLAY(sink), video_widget.winId());

  // Run the pipeline
  gst_element_set_state(pipeline, GST_STATE_PLAYING);

  // Finally, start the app event loop
  app->exec();
}
