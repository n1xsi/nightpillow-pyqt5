from datetime import datetime, timedelta
from . import constants


class SleepCalculator:
    """
    Выполняет расчёты оптимального времени сна на основе циклов.
    """

    def __init__(self):
        self.sleep_cycle = timedelta(minutes=constants.SLEEP_CYCLE_MINUTES)
        self.fall_asleep_time = timedelta(
            minutes=constants.FALL_ASLEEP_MINUTES)
        self.num_cycles = constants.NUM_CYCLES

    def calculate_bed_times(self, wake_up_time_str: str) -> list[str]:
        """
        Рассчитывает оптимальное время для отхода ко сну, если известно
        желаемое время пробуждения.

        Args:
            wake_up_time_str: Желаемое время пробуждения в формате "ЧЧ:ММ".

        Returns:
            Список из 6 вариантов времени для отхода ко сну, отсортированных
            от позднего к раннему.
        """
        try:
            wake_up_time = datetime.strptime(wake_up_time_str, "%H:%M")
        except ValueError:
            return []

        # Считаем, что заснуть нужно за 15 минут до начала первого цикла сна
        target_sleep_time = wake_up_time - self.fall_asleep_time

        bed_times = []
        current_time = target_sleep_time
        for _ in range(self.num_cycles):
            current_time -= self.sleep_cycle
            bed_times.append(current_time.strftime("%H:%M"))

        bed_times.reverse()  # Показываем от более ранних к более поздним
        return bed_times

    def calculate_wake_up_times(self, go_to_bed_time_str: str) -> list[str]:
        """
        Рассчитывает оптимальное время пробуждения, если известно
        время отхода ко сну.

        Args:
            go_to_bed_time_str: Время отхода ко сну в формате "ЧЧ:ММ".

        Returns:
            Список из 6 вариантов времени для пробуждения.
        """
        try:
            go_to_bed_time = datetime.strptime(go_to_bed_time_str, "%H:%M")
        except ValueError:
            return []

        # Пробуждение происходит после 15 минут засыпания и N циклов сна
        wake_up_start_time = go_to_bed_time + self.fall_asleep_time

        wake_up_times = []
        current_time = wake_up_start_time
        for _ in range(self.num_cycles):
            current_time += self.sleep_cycle
            wake_up_times.append(current_time.strftime("%H:%M"))

        return wake_up_times
