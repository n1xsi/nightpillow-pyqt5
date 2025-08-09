from PyQt5.QtWidgets import QApplication

from app.main_window import MainWindow
from app.calculator import SleepCalculator
from app.constants import (
    TOGGLE_TEXT_WAKE_UP, TOGGLE_TEXT_GO_TO_BED,
    WAKE_UP_RESULT_PREFIX, GO_TO_BED_RESULT_PREFIX,
    ERROR_TEXT
)

import sys


class AppController:
    """
    Контроллер, который связывает UI (MainWindow) и логику (SleepCalculator).
    """

    def __init__(self, view: MainWindow, calculator: SleepCalculator):
        self.view = view
        self.calculator = calculator
        self._connect_signals()

    def _connect_signals(self):
        """Подключает сигналы от виджетов к слотам (методам) контроллера."""
        self.view.toggle_switch.toggled.connect(self._on_toggle_changed)
        self.view.calculate_button.clicked.connect(self._on_calculate)

    def _on_toggle_changed(self, is_checked: bool):
        """Обновляет текст над переключателем при его изменении."""
        text = TOGGLE_TEXT_GO_TO_BED if is_checked else TOGGLE_TEXT_WAKE_UP
        self.view.toggle_label.setText(text)

    def _on_calculate(self):
        """
        Вызывается при нажатии на кнопку 'Рассчитать'.
        Запускает процесс расчёта и обновления результата.
        """
        input_time = self.view.time_input.text()
        is_wake_up_mode = self.view.toggle_switch.isChecked()

        if is_wake_up_mode:
            # Режим "надо лечь": рассчитываем время пробуждения
            times = self.calculator.calculate_wake_up_times(input_time)
            prefix = WAKE_UP_RESULT_PREFIX
        else:
            # Режим "надо встать": рассчитываем время отхода ко сну
            times = self.calculator.calculate_bed_times(input_time)
            prefix = GO_TO_BED_RESULT_PREFIX

        self._update_result_label(times, prefix)

    def _update_result_label(self, times: list[str], prefix: str):
        """Обновляет текстовую метку с результатом."""
        if not times:
            text = ERROR_TEXT
        else:
            text = f"{prefix}\n{' '.join(times)}."

        self.view.result_label.setText(text)


def main():
    """Главная функция для запуска приложения."""
    app = QApplication(sys.argv)

    # Создаем компоненты MVC
    view = MainWindow()
    calculator = SleepCalculator()
    # Контроллер связывает их вместе
    controller = AppController(view=view, calculator=calculator)

    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
