#include <ClickableWidget.h>
#include <iostream>

void ClickableWidget::mouseReleaseEvent(QMouseEvent * event) {
	(void) event;
	std::cout << "Widget Clicked\n";
	emit clicked();
}
