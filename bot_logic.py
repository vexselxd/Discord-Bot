import requests

def get_air_quality(city):
    """
    Función que obtiene la calidad del aire utilizando una API pública sin clave.
    """
    try:
        
        url = f"http://api.airvisual.com/v2/nearest_city?city={city}"
        response = requests.get(url)
        data = response.json()
        
        
        if response.status_code == 200:
           
            aqi = data.get('data', {}).get('current', {}).get('pollution', {}).get('aqius', 'No disponible')
            return {'aqi': aqi}
        else:
            return {'error': 'Error al obtener la calidad del aire'}
    
    except requests.exceptions.RequestException as e:
        return {'error': f"Error al conectarse con la API: {e}"}
