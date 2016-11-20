#include <QApplication>
#include <QPushButton>
#include <QHBoxLayout>
#include <QLabel>
#include <QScrollBar> 
#include <QSizePolicy>
#include <QPixmap>
#include <QFile>

#include <ClickableWidget.h>

int main(int argc, char **argv)
{
 QApplication app (argc, argv);

 //QWidget window;
 ClickableWidget *window = new ClickableWidget;
 window->setWindowState(Qt::WindowFullScreen);

 QPushButton *backButton = new QPushButton;
 QString filename = "/content/menu/images/icons/icon-tb-back.png";
 backButton->setIcon(QIcon(filename));
 backButton->setIconSize(QPixmap(filename).rect().size());

 QPushButton *homeButton = new QPushButton();
 QIcon homeButtonIcon ("/content/menu/images/icons/icon-tb-home.png");
 homeButton->setIcon(homeButtonIcon);
 homeButton->setIconSize(QSize(46,42));

 QPushButton *settingsButton = new QPushButton();
 QIcon settingsButtonIcon ("/content/menu/images/icons/icon-tb-settings.png");
 settingsButton->setIcon(settingsButtonIcon);
 settingsButton->setIconSize(QSize(45,42));

 QPushButton *playButton = new QPushButton();
 QIcon playButtonIcon ("/content/menu/images/icons/movie-icon-play.png");
 playButton->setIcon(playButtonIcon);
 playButton->setIconSize(QSize(100,100));
 
 QPushButton *stopButton = new QPushButton();
 QIcon stopButtonIcon ("/content/menu/images/icons/movie-icon-stop.png");
 stopButton->setIcon(stopButtonIcon);
 stopButton->setIconSize(QSize(114,60));
 QObject::connect(stopButton, SIGNAL (clicked()), QApplication::instance(), SLOT (quit()));

 QPushButton *rewindButton = new QPushButton();
 QIcon rewindButtonIcon ("/content/menu/images/icons/movie-icon-rewind.png");
 rewindButton->setIcon(rewindButtonIcon);
 rewindButton->setIconSize(QSize(114,60));

 QPushButton *skipbackButton = new QPushButton();
 QIcon skipbackButtonIcon ("/content/menu/images/icons/movie-icon-skipback.png");
 skipbackButton->setIcon(skipbackButtonIcon);
 skipbackButton->setIconSize(QSize(114,60));

 QPushButton *fullscreenButton = new QPushButton();
 QIcon fullscreenButtonIcon ("/content/menu/images/icons/movie-icon-fullscreen.png");
 fullscreenButton->setIcon(fullscreenButtonIcon);
 fullscreenButton->setIconSize(QSize(114,60));

 QPushButton *forwardButton = new QPushButton();
 QIcon forwardButtonIcon ("/content/menu/images/icons/movie-icon-forward.png");
 forwardButton->setIcon(forwardButtonIcon);
 forwardButton->setIconSize(QSize(114,60));

 QPushButton *skipforwardButton = new QPushButton();
 QIcon skipforwardButtonIcon ("/content/menu/images/icons/movie-icon-skipforward.png");
 skipforwardButton->setIcon(skipforwardButtonIcon);
 skipforwardButton->setIconSize(QSize(114,60));

 QPushButton *audioButton = new QPushButton();
 QIcon audioButtonIcon ("/content/menu/images/icons/movie-icon-audio.png");
 audioButton->setIcon(audioButtonIcon);
 audioButton->setIconSize(QSize(114,60));

 QPushButton *subtitlesButton = new QPushButton();
 QIcon subtitlesButtonIcon ("/content/menu/images/icons/movie-icon-subtitles.png");
 subtitlesButton->setIcon(subtitlesButtonIcon);
 subtitlesButton->setIconSize(QSize(114,60));

 //QFont f("Arial", 30, QFont::Bold);

 QLabel *nowTime = new QLabel("0:00:00");
 //nowTime->setFont(f);

 QScrollBar *slider = new QScrollBar(Qt::Horizontal);
 slider->setMinimumHeight(40);
 slider->setSizePolicy(QSizePolicy::Expanding,QSizePolicy::Minimum);

 QLabel *endTime = new QLabel("2:34:56");
 //endTime->setFont(f);

 QLabel *movieTitle = new QLabel("Star Wars");
 //movieTitle->setFont(f);
 movieTitle->setObjectName("movieTitle");

 QHBoxLayout *topBarLayout = new QHBoxLayout;
 topBarLayout->addWidget(backButton);
 topBarLayout->addWidget(movieTitle);
 topBarLayout->addStretch();
 topBarLayout->addWidget(settingsButton);
 topBarLayout->addWidget(homeButton);

 QWidget *topBarPanel = new QWidget;
 topBarPanel->setLayout(topBarLayout);

 QHBoxLayout *sliderLayout = new QHBoxLayout;
 sliderLayout->addWidget(nowTime);
 sliderLayout->addWidget(slider);
 sliderLayout->addWidget(endTime);

 QWidget *sliderPanel = new QWidget;
 sliderPanel->setLayout(sliderLayout);

 QHBoxLayout *transportButtonsLayout = new QHBoxLayout;
 transportButtonsLayout->setSpacing(0);
 transportButtonsLayout->addStretch();
 transportButtonsLayout->addWidget(fullscreenButton);
 transportButtonsLayout->addWidget(stopButton);
 transportButtonsLayout->addWidget(skipbackButton);
 transportButtonsLayout->addWidget(rewindButton);
 transportButtonsLayout->addWidget(playButton);
 transportButtonsLayout->addWidget(forwardButton);
 transportButtonsLayout->addWidget(skipforwardButton);
 transportButtonsLayout->addWidget(audioButton);
 transportButtonsLayout->addWidget(subtitlesButton);
 transportButtonsLayout->addStretch();

 QWidget *transportButtonsPanel = new QWidget;
 transportButtonsPanel->setLayout(transportButtonsLayout);

 QVBoxLayout *overlayLayout = new QVBoxLayout;
 //overlayLayout->addLayout(topBarLayout);
 overlayLayout->addWidget(topBarPanel);
 overlayLayout->addStretch();
 //overlayLayout->addLayout(transportButtonsLayout);
 overlayLayout->addWidget(transportButtonsPanel);
 //overlayLayout->addLayout(sliderLayout);
 overlayLayout->addWidget(sliderPanel);

 QWidget *overlayPanel = new QWidget;
 overlayPanel->setLayout(overlayLayout);

 QVBoxLayout *windowLayout = new QVBoxLayout;
 windowLayout->addWidget(overlayPanel);

 window->setLayout(windowLayout);

// Moved the stylesheet to a separate file.
// You can tweak the UI without recompiling code now.
 QFile styleSheetFile("stylesheet.qss");
 styleSheetFile.open(QFile::ReadOnly);
 QString styleSheet = QLatin1String(styleSheetFile.readAll());
 window->setStyleSheet(styleSheet);

 // Note Stylesheet settings will only get applied to objects that have already been created!  Create first.  Set style.  Then display.
 //window.setStyleSheet("QWidget{background: black;} QPushButton{border: none; outline: none;} QLabel {font-family: Arial; font-size: 30pt; font-weight: bold; color: red;} QLabel#movieTitle {color : white;} QScrollBar::handle:horizontal {background: red; image: url(/content/menu/images/icons/tiefighter.png);}  QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal, QScrollBar::sub-line:horizontal, QScrollBar::add-line:horizontal{width: 0px;}");

 window->show();
 //overlayPanel->hide();
 sliderPanel->hide();

 return app.exec();
}
