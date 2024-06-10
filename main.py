import requests

def get_weather(locale_id, token):
    url = f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{locale_id}/current?token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter a previsão do tempo: {response.status_code}")
        return None

def main():

    locale_id = "3477"
    token = ""
    
    weather_data = get_weather(locale_id, token)
    if weather_data:
        response_data = current_weather(weather_data)
        print(response_data)

def current_weather(weather_data):
    if weather_data:
        response_data = (
            f"Dados climáticos atuais em {weather_data['name']} - {weather_data['state']}, {weather_data['country']}:\n"
            f"Condição: {weather_data['data']['condition']}\n"
            f"Temperatura: {weather_data['data']['temperature']}°C\n"
            f"Sensação Térmica: {weather_data['data']['sensation']}°C\n"
            f"Direção do Vento: {weather_data['data']['wind_direction']}\n"
            f"Velocidade do Vento: {weather_data['data']['wind_velocity']} km/h\n"
            f"Umidade: {weather_data['data']['humidity']}%\n"
            f"Pressão: {weather_data['data']['pressure']} hPa\n"
            f"Data e Hora: {weather_data['data']['date']}\n"
        )
        return response_data
    else:
        return "Não foi possível obter os dados meteorológicos."

if __name__ == "__main__":
    main()