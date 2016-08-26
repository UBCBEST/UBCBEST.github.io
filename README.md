# ubcbest-website
_Website for Biomedical Engineering Student Team_  

![logo](./static/img/best-logo.gif)

To run this locally, you must install the `Python` and `Flask` on your
computer.  
To install Flask using `pip`, run  
> ```pip install -r requirements.txt```  

Then to start the server, run  
> ```python webserver.py```  

Presently, the [website](https://ubc-best.appspot.com) is hosted on
google__appengine.  
You must install the google_appengine python SDK requirements to make
changes to the deployed website. Follow the instructions
[here](https://cloud.google.com/appengine/docs/python/getting-started/python-standard-env) 
to set up your workspace.  
To run the app locally using appengine, you must install the project
requirements in the lib folder. Run  
> ```pip install -r requirements.txt -t lib```  
To run the app locally, run  
> ```dev_appserver.py .```  

To push changes to deployed website, run  
> ```appcfg.py -A <app-id> -V v1 update .```  
You must have the app id to be able to push changes to the deployed
website.
