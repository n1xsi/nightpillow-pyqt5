from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPainter
from PyQt5.QtCore import QSize, Qt
from qtwidgets import AnimatedToggle

from . import constants
from .utils import resource_path


class MainWindow(QWidget):
    """
    Главное окно приложения, отвечающее за отображение всех элементов UI.
    Использует абсолютное позиционирование для стабильной отрисовки
    в окне фиксированного размера.
    """

    def __init__(self):
        super().__init__()
        self._setup_ui()
        self._create_widgets()
        self._setup_positions()
        self._apply_styles()

    def _setup_ui(self):
        """Инициализирует основные параметры окна."""
        self.setWindowTitle(constants.APP_TITLE)
        self.setWindowIcon(QIcon(resource_path(constants.ICON_PATH)))
        self.setFixedSize(QSize(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
        self.background_image = QImage(resource_path(constants.BG_PATH))

    def paintEvent(self, event):
        """Отрисовывает фон, растягивая его на весь виджет."""
        painter = QPainter(self)
        if not self.background_image.isNull():
            painter.drawImage(self.rect(), self.background_image)

    def _create_widgets(self):
        """Создаёт все необходимые виджеты с указанием родителя."""
        self.time_label = QLabel(constants.TIME_LABEL, self)
        self.toggle_label = QLabel(constants.TOGGLE_TEXT_WAKE_UP, self)
        self.time_input = QLineEdit(self)
        self.toggle_switch = AnimatedToggle(
            parent=self,
            pulse_unchecked_color=constants.SECONDARY_COLOR,
            checked_color=constants.SECONDARY_COLOR,
            pulse_checked_color=constants.TEXT_COLOR
        )
        self.calculate_button = QPushButton(constants.CALCULATE_BUTTON_TEXT, self)
        self.result_label = QLabel(constants.INITIAL_RESULT_TEXT, self)

    def _setup_positions(self):
        """Размещает виджеты с помощью абсолютного позиционирования."""
        self.time_label.move(18, 55)
        self.toggle_label.move(175, 62)
        self.time_input.move(18, 105)
        self.toggle_switch.move(192, 90)
        self.calculate_button.move(18, 150)
        self.result_label.move(180, 150)
        self.result_label.setFixedWidth(370)

    def _apply_styles(self):
        """Применяет стили к виджетам."""
        base_text_style = f"font-family: {constants.FONT_FAMILY}; font-weight: bold; color: {constants.TEXT_COLOR};"
        self.time_label.setStyleSheet(f"{base_text_style} font-size: 16pt;")
        self.toggle_label.setStyleSheet(f"{base_text_style} font-size: 11pt; qproperty-alignment: AlignCenter;")

        self.result_label.setStyleSheet(f"{base_text_style} font-size: 12pt; qproperty-wordWrap: True; qproperty-alignment: AlignCenter;")
        self.result_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.result_label.setMinimumHeight(60)

        self.time_input.setPlaceholderText("23:00")
        self.time_input.setInputMask("00:00")

        self.time_input.setStyleSheet(f"""
            background-color: white;
            border: 2.5px solid {constants.PRIMARY_COLOR};
            font-family: {constants.FONT_FAMILY};
            font-weight: bold;
            font-size: 15pt;
        """)
        self.time_input.setAlignment(Qt.AlignCenter)
        self.time_input.setFixedSize(*constants.INPUT_SIZE)

        self.calculate_button.setStyleSheet(f"background-color: {constants.PRIMARY_COLOR}; {base_text_style} font-size: 12pt;")
        self.calculate_button.setFixedSize(*constants.BUTTON_SIZE)

        self.toggle_switch.setFixedSize(*constants.TOGGLE_SIZE)
