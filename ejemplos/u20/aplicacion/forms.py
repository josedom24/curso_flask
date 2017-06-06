from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet('images', IMAGES)

class UploadForm(FlaskForm):
    upload = FileField('selecciona imagen:', validators=[
        FileRequired("Debes indicar una imagen"),
        FileAllowed(images, 'Images only!')
    ])
    submit = SubmitField('Submit')

