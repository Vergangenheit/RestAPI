from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"tim": {"age": 10, "height": 180},
         "bill": {"age": 50, "height": 178}}

videos = {}


class Video(Resource):
    def get(self, video_id: int):
        return videos[video_id]

    def put(self, video_id):
        return {"data": video_id}


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
