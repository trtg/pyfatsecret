import hashlib#for computing hash
from rauth.service import OAuth1Service #see https://github.com/litl/rauth for more info
import shelve #for persistent caching of tokens, hashes,etc.
import time
#get your consumer key and secret after registering as a developer here: https://oauth.withings.com/en/partner/add

#FIXME add method to set default units and make it an optional argument to the constructor
class Fatsecret:
    def __init__(self,consumer_key,consumer_secret,verbose=0,cache_name='tokens.dat'):
        #cache stores tokens and hashes on disk so we avoid
        #requesting them every time.
        self.cache=shelve.open(cache_name,writeback=False)
        self.verbose=verbose        
        self.oauth=OAuth1Service(
                name='fatsecret',
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                request_token_url='http://www.fatsecret.com/oauth/request_token',
                access_token_url='http://www.fatsecret.com/oauth/access_token',
                authorize_url='http://www.fatsecret.com/oauth/authorize',
                header_auth=False)

        self.access_token = self.cache.get('fatsecret_access_token',None)
        self.access_token_secret = self.cache.get('fatsecret_access_token_secret',None)
        self.request_token =  self.cache.get('fatsecret_request_token',None)
        self.request_token_secret =  self.cache.get('fatsecret_request_token_secret',None)
        self.pin= self.cache.get('fatsecret_pin',None)
        
        #If this is our first time running- get new tokens 
        if (self.need_request_token()):
            self.get_request_token()
            got_access_token=self.get_access_token()
            if( not got_access_token):
                print "Error: Unable to get access token"
                    

    def dbg_print(self,txt):
        if self.verbose==1:
            print txt

    def get_request_token(self):
        self.request_token,self.request_token_secret = self.oauth.get_request_token(method='GET',params={'oauth_callback':'oob'})
        authorize_url=self.oauth.get_authorize_url(self.request_token)
        #the pin you want here is the string that appears after oauth_verifier on the page served
        #by the authorize_url
        print 'Visit this URL in your browser then login: ' + authorize_url
        self.pin = raw_input('Enter PIN from browser: ')
        self.cache['fatsecret_request_token']=self.request_token
        self.cache['fatsecret_request_token_secret']=self.request_token_secret
        self.cache['fatsecret_pin']=self.pin
        print "fatsecret_pin is ",self.cache.get('fatsecret_pin')

    def need_request_token(self):
        #created this method because i'm not clear when request tokens need to be obtained, or how often
        if (self.request_token==None) or (self.request_token_secret==None) or (self.pin==None):
            return True
        else:
            return False

    def get_access_token(self):
        print "in get_access_token"
        response=self.oauth.get_access_token('GET',
                request_token=self.request_token,
                request_token_secret=self.request_token_secret,
                params={'oauth_verifier':self.pin})
        data=response.content
        print response.content
        self.access_token=data.get('oauth_token',None)
        self.access_token_secret=data.get('oauth_token_secret',None)
        self.cache['fatsecret_access_token']=self.access_token
        self.cache['fatsecret_access_token_secret']=self.access_token_secret
        if not(self.access_token) or not(self.access_token_secret):
            print "access token expired "
            return False
        else:
            return True

    
    def food_get(self,food_id):
        params={'method': 'saved_meals.get','food_id':food_id,'format':'json'} 
        response=self.oauth.get(
                'http://platform.fatsecret.com/rest/server.api',
                params=params,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
                header_auth=False)
        return response.content

    def foods_search(self,search_expression,page_number=None,max_results=None):
        params={'method': 'foods.search','oauth_token': self.access_token,'search_expression':search_expression,'format':'json'} 
        if page_number!=None:
            params['page_number'] = page_number
        if max_results!=None:
            params['max_results'] = max_results

        response=self.oauth.get(
                'http://platform.fatsecret.com/rest/server.api',
                params=params,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
                header_auth=False)
        return response.content

    #FIXME allow specifying particular month(s)
    def food_entries_get_month(self,date=None):
        params={'method': 'food_entries.get_month','format':'json'} 
        if date!=None:
            params['date']=int(round(time.mktime(date.timetuple())/60/60/24))
        response=self.oauth.get(
                'http://platform.fatsecret.com/rest/server.api',
                params=params,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
                header_auth=False)
        #print response.content
        tmp=response.content['month']['day']
        #result=[(i['carbohydrate'],i['fat'],i['protein'],i['calories'],i['date_int']) for i in tmp] 
        return tmp

    
    def saved_meals_get(self):
        params={'method': 'saved_meals.get','format':'json'} 
        response=self.oauth.get(
                'http://platform.fatsecret.com/rest/server.api',
                params=params,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
                header_auth=False)
        return response.content

