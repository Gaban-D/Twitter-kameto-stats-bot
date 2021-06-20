from datetime import timedelta


class Stats:
    streams_durations_array = []
    games_played = []
    viewer_peak = 0
    view_count = 0
    total_duration = ""

    def calculate_total_streams_duration(self):

        duration_timedelta = timedelta(seconds=0)
        for duration in self.streams_durations_array:
            duration_timedelta += timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)

        converted_duration = str(duration_timedelta).split(":")
        self.total_duration = "{heures} heures, {minutes} minutes et {seconds} secondes"\
            .format(heures=converted_duration[0], minutes=converted_duration[1], seconds=converted_duration[2])

        return self.total_duration
