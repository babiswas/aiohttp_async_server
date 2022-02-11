class Server:
   HOST_NAME="https://captivateprimestage1.adobe.com"
   API_VERSION="primeapi/v2"


class API_LO:
   END_POINT="learningObjects"
   LO_ENDPOINT=Server.HOST_NAME+"/"+Server.API_VERSION+"/"+END_POINT


class API_CATLOG:
   END_POINT="catalogs"
   CATLOG_ENDPOINT=Server.HOST_NAME+"/"+Server.API_VERSION+"/"+END_POINT


class OAUTH:
   END_POINT=Server.HOST_NAME+"/"+"oauth/token/refresh"
   CLIENT_ID="6041f924-5745-435a-8515-efcbc8a3d371"
   CLIENT_SECRET="d10fa92b-412f-435f-a190-67859157ed07"
   REFRESH_TOKEN="85b32fe6a3527a3eb88f9d1fe0fd43b9"
   TOKEN=""



   