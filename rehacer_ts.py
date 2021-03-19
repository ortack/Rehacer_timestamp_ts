import sys
import os
import subprocess


path, file = os.path.split(sys.argv[1])
ffmpeg = 'ffmpeg.exe'
video = sys.argv[1]  
video_temp = path + '/temp.mpg'
video_old = sys.argv[1] + '.old'
def main():
    if len(sys.argv) == 3:
        try:
            print(video, video_temp)
            subprocess.run([ffmpeg, '-i', video, '-vcodec', 'copy', '-acodec', 'copy', '-c:s', 'copy', '-map', '0:v:0', '-map','0:a', '-map', '-0:s','-ignore_unknown', '-sn', '-threads', '1', video_temp], shell=True,)
        except Exception as e:
            print(e)
            sys.exit(1)
        if sys.argv[2] == 'copiado':
            if os.path.exists(video_temp):
                os.rename(video, video_old)
            if os.path.exists(video) is False:
                os.rename(video_temp, video)
        elif sys.argv[2] == 'borrado':
            if os.path.exists(video_temp):
                os.remove(video)
            if os.path.exists(video) is False:
                os.rename(video_temp, video)
    else:
        print('El segundo argumento debe de ser "borrado" para borrar el fichero original o "copiado" para renombrar el fichero original como .old')
if __name__ == '__main__':
    main()