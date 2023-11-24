from flask_restful import Resource, abort
from flask import request
from app.models import CompanyModel, ReportModel

dummy_data = [
    {"id": 1, "name": "Ford", "ticker": "F", "statuscolor": "blue lighten-1 white--text",
     "naics": "NAICS: 541511", "numbers": "1000", "date": "2023-11-10"},
    {"id": 2, "name": "Shell", "ticker": "AAPL", "statuscolor": "info",
     "naics": "NAICS: 541511", "numbers": "1000", "date": "2023-11-10"},
    {"id": 3, "name": "Amazon", "ticker": "AAPL", "statuscolor": "warning",
     "naics": "NAICS: 541511", "numbers": "1000", "date": "2023-11-10"}
]

reports = [{"id": 1, "name": "Ford", "date": "2023-01-01", "heading": "Title latest News", "content": "In the heart of the bustling city, where the vibrant energy of urban life meets the calming whispers of nature, lies a place of remarkable juxtaposition. Tall skyscrapers stretch toward the heavens, casting shadows over busy streets teeming with the hustle and bustle of daily life. Yet, within this concrete jungle, pockets of greenery emerge like sanctuaries of serenity, inviting weary souls to take a moment of respite. The air is filled with the melodic symphony of city sounds—honking horns, laughter, footsteps, and the distant hum of machinery. It's a tapestry woven with the threads of diversity, each person contributing to the rich fabric of communal existence. As the sun sets, the cityscape transforms into a canvas painted with hues of orange and pink, a breathtaking display that momentarily halts the relentless march of time. In every corner, stories unfold, dreams take flight, and the city, with all its complexities, continues its eternal dance of life.", "url": "https://www.google.com"},
             {"id": 2, "name": "Amazon", "date": "2023-01-01", "heading": "Updated News", "content": "In the heart of the bustling city, where the vibrant energy of urban life meets the calming whispers of nature, lies a place of remarkable juxtaposition. Tall skyscrapers stretch toward the heavens, casting shadows over busy streets teeming with the hustle and bustle of daily life. Yet, within this concrete jungle, pockets of greenery emerge like sanctuaries of serenity, inviting weary souls to take a moment of respite. The air is filled with the melodic symphony of city sounds—honking horns, laughter, footsteps, and the distant hum of machinery. It's a tapestry woven with the threads of diversity, each person contributing to the rich fabric of communal existence. As the sun sets, the cityscape transforms into a canvas painted with hues of orange and pink, a breathtaking display that momentarily halts the relentless march of time. In every corner, stories unfold, dreams take flight, and the city, with all its complexities, continues its eternal dance of life.", "url": "https://www.google.com"},
             {"id": 3, "name": "Shell", "date": "2023-01-01", "heading": "Tonight's Updates", "content": "In the heart of the bustling city, where the vibrant energy of urban life meets the calming whispers of nature, lies a place of remarkable juxtaposition. Tall skyscrapers stretch toward the heavens, casting shadows over busy streets teeming with the hustle and bustle of daily life. Yet, within this concrete jungle, pockets of greenery emerge like sanctuaries of serenity, inviting weary souls to take a moment of respite. The air is filled with the melodic symphony of city sounds—honking horns, laughter, footsteps, and the distant hum of machinery. It's a tapestry woven with the threads of diversity, each person contributing to the rich fabric of communal existence. As the sun sets, the cityscape transforms into a canvas painted with hues of orange and pink, a breathtaking display that momentarily halts the relentless march of time. In every corner, stories unfold, dreams take flight, and the city, with all its complexities, continues its eternal dance of life.", "url": "https://www.google.com"},
             {"id": 4, "name": "Ford", "date": "2023-01-01", "heading": "Latest Update", "content": "In the heart of the bustling city, where the vibrant energy of urban life meets the calming whispers of nature, lies a place of remarkable juxtaposition. Tall skyscrapers stretch toward the heavens, casting shadows over busy streets teeming with the hustle and bustle of daily life. Yet, within this concrete jungle, pockets of greenery emerge like sanctuaries of serenity, inviting weary souls to take a moment of respite. The air is filled with the melodic symphony of city sounds—honking horns, laughter, footsteps, and the distant hum of machinery. It's a tapestry woven with the threads of diversity, each person contributing to the rich fabric of communal existence. As the sun sets, the cityscape transforms into a canvas painted with hues of orange and pink, a breathtaking display that momentarily halts the relentless march of time. In every corner, stories unfold, dreams take flight, and the city, with all its complexities, continues its eternal dance of life.", "url": "https://www.google.com"}]


class GetDataResource(Resource):
    def get(self, month):
        if month not in ['This Month', 'Last Month', 'Before Last Month']:
            abort(404, message="Invalid month specified")

        # companies_with_reports = (
        #     CompanyModel.query
        #     .join(ReportModel, CompanyModel.ticker == ReportModel.ticker)
        #     .all()
        # )
        # dummy_data = CompanyModel.query.all()
        # serialized_companies = [
        #     {
        #         'id': company.id,
        #         'name': company.name,
        #         'ticker': company.ticker,
        #         'report_count': len(company.reports),
        #         'date': "2023-11-10"
        #     }
        #     for company in companies_with_reports
        # ]
        # serialized_companies = [data.json() for data in dummy_data]
        return {"data": dummy_data, "month": month}


companies = ["Ford", "Amazon", "Shell", "Apple"]

class GetCompaniesList(Resource):
    def get(self):
        # Dummy implementation
        return {"data": companies}

class GetReportsList(Resource):
    def get(self, company_name=None):
        if company_name:
            filtered_companies = [report for report in reports if report['name'] == company_name]
            return {'data': filtered_companies}
        else:
            return {'data': reports}

class FinDataResource(Resource):
    def get(self, company_name):
        if company_name == 'Ford':
            series = {
                "name": company_name,
                'data': [10, 20, 35, 50, 49, 60, 70, 91, 125]
            }
        elif company_name == 'Shell':
            series = {
                "name": company_name,
                'data': [30, 40, 35, 50, 49, 60, 70, 91, 125]
            }
        elif company_name == 'Amazon':
            series = {
                "name": company_name,
                'data': [50, 60, 35, 50, 49, 60, 70, 91, 125]
            }
        else:
            series = {
                "name": company_name,
                'data': [0, 0, 0, 0, 0, 0, 0, 0, 0]
            }
        xaxis = {'time': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01',
                '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01',
                '2020-09-01']}
        return {'series': [series], 'xaxis': xaxis}

# Additional resources can be added here
