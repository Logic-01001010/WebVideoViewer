import os
from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def main():

    path = "./static/video/"
    file_list = []

    for root, dirs, files in os.walk(path):

        
        for dir in dirs:
            file_list.append(dir)


    #print(file_list)


    
    
    return render_template('index.html', file_list = file_list)


@app.route('/list/<path:folder>')
def list(folder): 
    
    path = "./static/video/"+folder
    file_list = os.listdir(path)

    video_list=[]
    subtitle_list=[]
    #print(file_list)



    for i in file_list:
        if i.endswith(".mkv"):
            video_list.append(i)
    #print(video_list)


    for i in file_list:
        if i.endswith(".smi") or i.endswith(".srt"):
            subtitle_list.append(i)
    #print(subtitle_list)


    return render_template('list.html', folder=folder, videos = video_list, subtitles = subtitle_list)





@app.route('/selector', methods = ['GET', 'POST'])
def selector():


    content = request.json
    #print(content['video'], content['subtitle'])
    
    return render_template("video.html", video = content['video'], subtitle = content['subtitle'])


@app.route('/video', methods = ['GET'])
def video():
    

    folder = request.args.get('folder')
    video = request.args.get('video')
    subtitle = request.args.get('subtitle')


    return render_template("video.html", folder = folder ,video = video, subtitle = subtitle)







if __name__== '__main__':

    
            

    
    app.run(host='0.0.0.0',port='82', threaded=True, debug=True)
