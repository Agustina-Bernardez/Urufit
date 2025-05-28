# importo la funcion que defini en init
from website import create_app 

# creo una instancia de la aplicacion usando la funcion create_app
app = create_app()

if __name__ == '__main__': 
    app.run(debug=True)
    