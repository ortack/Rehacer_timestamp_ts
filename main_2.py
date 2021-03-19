import sys
import os
import subprocess

ffmpeg = 'C:/Program Files (x86)/CREATECNA/Cellarium Search 4/RenderLibs/ffmpeg.exe'
video = 'C:/CTSearch/temp/video.ts'
comandotots = f'ffmpeg -i "{fichero_in}" -vcodec copy  -acodec copy  -sn  -threads 1  video.ts'
comandotompg = f'ffmpeg.exe -ss {inpoint} -i video.ts -s 1280x720 -aspect 16:9 -map 0:0 -map 0:1  -c:v libx264 -b:v 1000k -c:a aac -b:a 128k -f mp4  -t {duracion} "{fichero_out}"'
def main():
    try:
        fichero_in = filedialog.askopenfilename(title="Select a question file to open.", filetypes=[("XLSX files", "*.xlsx")])
        subprocess.run([ffmpeg, '-i', fichero_in, '-vcodec', 'copy', '-acodec', 'copy', '-sn', '-threads', '1', video], shell=True,)
    except:
        print('usage: fichero in duracion')
        sys.exit(1)

window = Tk()
window.update()
window.title("Flash Cards by Eddie.Snipes@gmail.com")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)



if __name__ == '__main__':
    window.mainloop()
    #main()