# ubcbest-website
_Website for Biomedical Engineering Student Team_  

![logo](./static/img/best-logo.gif)

To run this locally, you must install the `Python` and `Flask` on your computer.  
To install Flask using `pip`, run  
> ```pip install -r requirements.txt```  

Then to start the server, run  
> ```python webserver.py```  

Presently, the website is hosted on google appengine.  
Visit the deployed website [here](ubc-best.appspot.com).  

To push changes to deployed website, run  
> ```appcfg.py -A <app-id> -V v1 update .```  
