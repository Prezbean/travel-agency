from app import create_app # imports all files from app 
app = create_app()

if __name__ == "__main__":  #allows the programm to run as a whole
    app.run(debug=False)