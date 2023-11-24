from app.database import db

class CompanyModel(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ticker = db.Column(db.String(10), nullable=False)
    naics = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Company(name = {self.name}, ticker = {self.ticker}, naics = {self.naics})"

    def json(self):
        return {'id':self.id, 'name': self.name, 'ticker': self.ticker, 'naics': self.naics}
    
class ReportModel(db.Model):
    __tablename__ = 'reports'
    title = db.Column(db.String(80), primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    ticker = db.Column(db.String(10), nullable=False)
    date = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Report(title = {self.title}, content = {self.content}, ticker = {self.ticker}, date = {self.date})"

    def json(self):
        return {'title': self.title, 'content': self.content, 'ticker': self.ticker, 'date': self.date}
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class FinDataModel(db.Model):
    __tablename__ = 'fin'
    date = db.Column(db.String(10), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    total_current_assets = db.Column(db.Float, nullable=False)
    total_current_liab = db.Column(db.Float, nullable=False)