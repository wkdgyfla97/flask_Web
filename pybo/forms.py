from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired("제목 입력해주세요")])
    content = TextAreaField('내용', validators=[DataRequired("내용을 입력해주세요")])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('답글도 내용 좀 적어주셈')])