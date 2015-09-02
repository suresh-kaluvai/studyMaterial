def buildConnectionString(params):
    """
        Build Connection string from dictionary of parameters
        
        Returns String
    """
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {
                    "server": "mpilgrm", \
                    "database": "master", \
                    "uid": "sa", \
                    "pwd": "secret"
                }

    print buildConnectionString(myParams)
    print buildConnectionString.__doc__
    print __name__
