from app import db


class Decoration(db.Model):
    __tablename__ = "decoration"
    decoration_id = db.Column('id', db.Integer, primary_key=True)
    decoration_type = db.Column('typeOfDecorations', db.String(20))
    decoration_place = db.Column('decorationPlace', db.String(20))
    decoration_color = db.Column('color', db.String(20))

    def __str__(self):
        return str("decoration id: " + str(self.decoration_id) + "\ndecoration type: " + str(
            self.decoration_type) + "\ndecoration place: " + str(self.decoration_place) + "\ndecoration color: " + str(
            self.decoration_color))
