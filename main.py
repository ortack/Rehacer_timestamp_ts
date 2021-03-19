import ffmpy
import sys
import os

#comandotots = 'ffmpeg.exe  -i %s  -vcodec copy  -acodec copy  -sn  -threads 1  video.ts ' %sys.argv[1]
#comandotompg = 'ffmpeg.exe -ss {} -i video.ts -s 1280x720 -aspect 16:9 -map 0:0 -map 0:1  -c:v libx264 -b:v 1000k -c:a aac -b:a 128k -f mp4  -t {} {}'.format(sys.argv[2],sys.argv[3],sys.argv[4])#
#input = ffmpeg.input('in.mp4')
#audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
#video = input.video.hflip()
#out = ffmpeg.output(audio, video, 'out.mp4')


def main():
    try:
        ff = ffmpy.FFmpeg(
        inputs={sys.argv[1]: None},
        outputs={sys.argv[4]: '-ss {} -s 1280x720 -aspect 16:9 -map 0:0 -map 0:1  -c:v libx264 -b:v 1000k -c:a aac -b:a 128k -f mp4  -t {}'.format(sys.argv[2],sys.argv[3])}
        )
        ff.cmd
        ff.run()
    except:
        print('usage: fichero in duracion error : ',sys.exc_info()[0])
        sys.exit(1)

if __name__ == '__main__':
    main()