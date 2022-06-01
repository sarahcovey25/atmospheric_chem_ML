import pandas as pd


class NaNChecker():
    """
    Python API to queury from AQS database.
    """
    # hey 

    def __init__(self, data):
        """
        initializes the object with the dataframe you want checked
        """
        # params for checking for Nans if needed
        # self.params = {
        #     'email': "orussell@g.hmc.edu",
        #     'key': "silverwren87"}
        self.df = pd.DataFrame(data=data)
    
    def print_df(self):
        """
        prints back the input data frame
        """
        return self.df

    def tally_nans(self, variable):
        """
        tallys up the spread of how many nans in a row

        Parameters:
            variable: string - name of column we want to check NaNs for
        """
        # creates a dataframe of just that variable
        var_df = self.df[variable]
        var_df_nans = var_df.isnull()
        # loop through all variables, if NaN 
        tally_df = pd.DataFrame({'NaNs':[]})
        tally = 0 # counts NaNs in a row

        for x in var_df_nans:
            if x == True: # so if val is NaN
                tally += 1
            if (x == False) and (tally != 0): # if we switch back to False and also the tally has stuff in it
                tally_df.loc[len(tally_df.index)] = tally # adds tally to the df
                tally = 0

        # I NOW NEED TO FIND THE BEST PLACES TO PUT THIS 

        return None