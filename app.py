from flask import Flask, render_template, request, redirect, send_file, make_response
from core import video_name
import urllib.parse

app = Flask(__name__)

from core import get_video_data, download_video_from_link


@app.route('/')  
def index():
    return render_template("index.html")
  
@app.route('/download', methods=['POST'])
def download():
    if 'link_input_field' in request.form:
        url = request.form['link_input_field']
        print("URL - ", url)
        video_link = get_video_data(url)
        save_path = download_video_from_link(video_link)
        
        print("SAVE: ",save_path)

        try:
            response = make_response(send_file(save_path, as_attachment=True))
    
            # Set the file name as it will appear in the download dialog
            response.headers['Content-Disposition'] = 'attachment; filename="downloaded_file.txt"'
    
             # Set the Content-Type header explicitly
            response.headers['Content-Type'] = 'application/octet-stream'
    
            return response
        except Exception as e:
            print("Error sending file:", e)
            return 'Error sending file'
    else:
        return 'Błąd: Brak URL w polu '

if __name__ == '__main__':
    app.run(debug=True)
