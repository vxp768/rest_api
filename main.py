import iss_apis as iss
import web_app
import udemy_flask
import restful

def query_nasa_iss():
    iss.iss_query()

if __name__ == '__main__':
    #query_nasa_iss()
    #web_app.web_start()
    #udemy_flask.app_run()
    restful.app_run()