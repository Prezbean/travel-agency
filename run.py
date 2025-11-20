from app import create_app # Imports all files from app 
app = create_app()

if __name__ == "__main__":  # Allows the program to run as a whole
    app.run(debug=False)