from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import pandas as pd
from model import preprocess_data, make_predictions, predict
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def handle_predict():
    if request.method == 'POST':
        # Check if the user uploaded a file
        file = request.files['file']
        if file:
            # Save the uploaded file temporarily
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)
            
            # Load the uploaded CSV file
            try:
                test_df = pd.read_csv(filepath)
            except Exception as e:
                return jsonify({'success': False, 'message': f'Error loading CSV: {str(e)}'}), 400
            
            # Check if the DataFrame is empty
            if test_df.empty:
                return jsonify({'success': False, 'message': 'Uploaded CSV is empty.'}), 400

            # Use the predict function from model.py to generate predictions
            predictions_df = predict(test_df)  # Call the predict function with the DataFrame
            
            # Save the predictions to a CSV file
            output_filepath = os.path.join('uploads', 'predictions.csv')
            predictions_df.to_csv(output_filepath, index=False)
            
            return jsonify({'success': True, 'message': 'Predictions generated successfully', 'output_file': output_filepath})

    return jsonify({'success': False, 'message': 'Error processing file'}), 400


# Route to download the predictions file
@app.route('/download')
def download():
    output_filepath = os.path.join('uploads', 'predictions.csv')
    return send_file(output_filepath, as_attachment=True, download_name='predictions.csv')

# Route to get prediction data for the chart
@app.route('/chart-data')
def chart_data():
    output_filepath = os.path.join('uploads', 'predictions.csv')
    if os.path.exists(output_filepath):
        df = pd.read_csv(output_filepath)
        # Group by Item_Identifier and Outlet_Identifier and calculate total sales
        chart_data = df.groupby(['Item_Identifier', 'Outlet_Identifier'])['Item_Outlet_Sales'].sum().reset_index()
        # Sort by total sales
        chart_data = chart_data.sort_values('Item_Outlet_Sales', ascending=False)
        return jsonify(chart_data.to_dict(orient='records'))
    return jsonify([])

if __name__ == '__main__':
    # Ensure the uploads directory exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)