#include <QWidget>

class ClickableWidget : public QWidget {
	Q_OBJECT

	private:
		void mouseReleaseEvent(QMouseEvent * event);
	signals:
		void clicked();
};
