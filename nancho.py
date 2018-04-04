"""Mute music app if browser audio is playing."""

# author: Chris Emmery
# license: MIT

import subprocess as sp
import re
from time import sleep


def parse_pacmd(browser, music):
    """Parses the pacmd list to find browser and music states."""
    
    states = {browser: 0, music: 0}
    app_data = {}
    
    for line in sp.Popen("pacmd list-sink-inputs", shell=True, stderr=sp.PIPE, stdout=sp.PIPE,
                         ).stdout.read().decode('utf-8').split('\n'):
        
        if any(key + ': ' in line for key in ['index', 'state', 'client', 'muted']):
            line = re.sub(" {2,}|\t", '', line)
            key, value = line.split(': ')
            app_data[key] = value

            if key == 'client':
                for hook in states:
                    if hook in app_data['client']:
                        states[hook] = app_data['index'] if app_data['state'] == 'RUNNING' \
                                       and app_date['muted'] != 'yes' else 0
                app_data = {}

    return states[browser], states[music]
                 
                 
if __name__ == '__main__':
    
    import argparse
    parser = argparse.ArgumentParser()
    # data args
    parser.add_argument('--browser', default='Firefox', help='The name identifier of your standard browser.')
    parser.add_argument('--music', default='Spotify', help='The name identififier of your music app.')
    parser.add_argument('--poll_time', type=int, default=3, help='Change the amount of time script parses pacmd.')
    parser.add_argument('--pause', action='store_true', help='Pauses player rather than sending mute command (Spotify only!).')
    args = parser.parse_args()

    was_playing = False
    while True:

        browser_state, music_state = parse_pacmd(args.browser, args.music)
        pac_cmd = "pacmd set-sink-input-mute {ix} {val}"
        spt_cmd = "qdbus org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.{0}"
        # mute music
        if browser_state and music_state:
            sp.Popen(pac_cmd.format(ix=music_state, val=1) if not args.pause else spt_cmd.format("Pause"), shell=True)
            was_playing = True
        # unmute music
        if not browser_state and was_playing:
            sp.Popen(pac_cmd.format(ix=music_state, val=0) if not args.pause else spt_cmd.format("Play"), shell=True)
            was_playing = False

        sleep(args.poll_time)
