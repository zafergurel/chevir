'''Encoder class
'''
import pexpect
from pexpect import popen_spawn

class Encoder:
    '''Chevir class'''
    def __init__(self, ffmpeg_path, logger):
        '''constructor'''
        self.ffmpeg_path = ffmpeg_path
        self.logger = logger

    def process(self, command_args, file_path, out_file_path):
        '''Returns a generator to handle ffmpeg
        process to convert flv_file to mp4 file.
        '''
        ffmpeg_command = command_args.format(ffmpeg_path=self.ffmpeg_path,
                                             file_path=file_path,
                                             out_file_path=out_file_path)
        ffmpeg_generator = self._create_progress_generator(ffmpeg_command)
        for status in ffmpeg_generator:
            yield status
            if status[2]:
                break

    def _create_progress_generator(self, ffmpeg_command):
        '''This generator returns a set of
        passed time, total time and process status
        which is a boolean. If True, process has finished.
        '''
        # thread = pexpect.spawn(ffmpeg_command)
        thread = pexpect.popen_spawn.PopenSpawn(ffmpeg_command)
        self.logger.debug("started %s" % ffmpeg_command)
        cpl = thread.compile_pattern_list([pexpect.EOF,
                                            r'Duration: (\d+:\d+:\d+)',
                                            r'time=(\d+:\d+:\d+)'])
        total_time = passed_time = 0
        while True:
            i = thread.expect_list(cpl, timeout=None)
            if i == 0: # EOF
                yield (passed_time, total_time, True)
                break
            elif i == 1:
                total_time = self._get_total_seconds(thread.match.group(1).decode())
            elif i == 2:
                passed_time = self._get_total_seconds(thread.match.group(1).decode())

            yield (passed_time, total_time, False)

    def _get_total_seconds(self, time_string):
        '''Converts hh:mm:ss to total seconds
        '''
        total = 0
        if not ':' in time_string:
            return None

        if time_string.count(':') != 2:
            return None

        for idx, val in enumerate([int(tmp) for tmp in time_string.split(':')]):
            if idx == 2:
                total += val
            elif idx == 1:
                total += val*60
            elif idx == 0:
                total += val*3600
        return total
