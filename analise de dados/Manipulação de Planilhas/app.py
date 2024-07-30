from flask import Flask, send_file
import openpyxl
from io import BytesIO

app = Flask(__name__)

@app.route('/download-excel')
def download_excel():
    # Crie um workbook e uma planilha
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Dados'
    
    # Adicione alguns dados de exemplo
    data = [
        ['Nome', 'Idade'],
        ['Alice', 30],
        ['Bob', 25]
    ]
    for row in data:
        sheet.append(row)
    
    # Salve o workbook em um objeto BytesIO
    file_stream = BytesIO()
    workbook.save(file_stream)
    file_stream.seek(0)
    
    return send_file(file_stream, as_attachment=True, download_name='dados.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True)
