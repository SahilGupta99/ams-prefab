import os

class Config:
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@localhost/product_management"
    SQLALCHEMY_DATABASE_URI = (
        "mysql+mysqlconnector://avnadmin:AVNS_6Y_ELomxkTzGtorz1p5@"
        "prefab-ams-prefab.l.aivencloud.com:22480/defaultdb"
        "?ssl_ca=/Product-Management-final/ca.pem"
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "static/uploads"
    ALLOWED_IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}
    ALLOWED_VIDEO_EXTENSIONS = {"mp4", "mov", "avi"}


