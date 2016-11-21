#include <glib.h>
#include <gst/gst.h>
#include <gst/video/videooverlay.h>
#include <gst/app/gstappsink.h>

#include <QApplication>
#include <QTimer>
#include <QWidget>
#include <QMutex>
#include <QImage>
#include <QLabel>

#include <cstdio>

class Capture {
  private:
        QImage m_image;
        QMutex m_mutex;
  public:
        GstElement *pipeline;
        static GstFlowReturn newSample(GstAppSink* sink, gpointer gSelf);
        QImage getFrame();
        Capture();
};


class VideoWidget : public QLabel {
  private:
	Capture *m_capture;
  public:
	VideoWidget(Capture *movie);
  protected:
	void paintEvent(QPaintEvent* paintEvent);
};


VideoWidget::VideoWidget(Capture *movie) {
	m_capture = movie;
}

void VideoWidget::paintEvent(QPaintEvent* paintEvent)
{
    setPixmap(QPixmap::fromImage(m_capture->getFrame()));
    QLabel::paintEvent(paintEvent);
}


Capture::Capture() {

  // prepare the pipeline
  pipeline = gst_pipeline_new("xvoverlay");
  GstElement *src = gst_element_factory_make("videotestsrc", NULL);
  GstElement *conv = gst_element_factory_make("videoconvert", NULL);
  GstElement *sink = gst_element_factory_make("appsink", NULL);
  gst_bin_add_many(GST_BIN(pipeline), src, conv, sink, NULL);
  gst_element_link_many(src, conv, sink, NULL);

  gst_app_sink_set_emit_signals(GST_APP_SINK(sink), TRUE);
  g_signal_connect(sink, "new-sample", G_CALLBACK(newSample), (gpointer)this);

  // run the pipeline
  GstStateChangeReturn sret = gst_element_set_state(pipeline, GST_STATE_PLAYING);
  g_print("Playing...\n");
  if (sret == GST_STATE_CHANGE_FAILURE) {
    gst_element_set_state(pipeline, GST_STATE_NULL);
    gst_object_unref(pipeline);
    // Exit application
    QTimer::singleShot(0, QApplication::activeWindow(), SLOT(quit()));
  }
}

GstFlowReturn Capture::newSample(GstAppSink* sink, gpointer gSelf)
{
    //g_print("New sample...");
    GstSample* sample = NULL;
    GstBuffer* sampleBuffer = NULL;
    GstMapInfo bufferInfo;

    Capture* self = static_cast<Capture* >(gSelf);
    sample = gst_app_sink_pull_sample(GST_APP_SINK(sink));
    if(sample != NULL)
    {
        sampleBuffer = gst_sample_get_buffer(sample);
        if(sampleBuffer != NULL)
        {
            gst_buffer_map(sampleBuffer, &bufferInfo, GST_MAP_READ);
	    //gsize sz = gst_buffer_get_size(sampleBuffer);
	    //g_print("%lu\n",sz);
            self->m_mutex.lock();
            self->m_image = QImage(bufferInfo.data, 600, 400, QImage::Format_Mono);
            self->m_mutex.unlock();
            gst_buffer_unmap(sampleBuffer, &bufferInfo);
        }
        gst_sample_unref(sample);
    }
    return GST_FLOW_OK;
}

QImage Capture::getFrame()
{
    QMutexLocker locker(&m_mutex);
    return m_image;
}

int main(int argc, char *argv[])
{
  gst_init(&argc, &argv);
  QApplication app(argc, argv);
  app.connect(&app, SIGNAL(lastWindowClosed()), &app, SLOT(quit()));

  Capture *movie = new Capture();

  // prepare the ui
  VideoWidget window(movie);
  //QLabel window;
  window.resize(600, 400);
  window.show();



  int ret = app.exec();

  window.hide();
  gst_element_set_state(movie->pipeline, GST_STATE_NULL);
  gst_object_unref(movie->pipeline);

  return ret;
}
