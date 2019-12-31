from app import create_app


app = create_app(environment='development')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18080, debug=True)
