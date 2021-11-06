import pandas as pd
df = pd.read_excel('naturescapedatabase.ods')
# print (df)
# print(df.columns)

# Another example of list comprehension
# [print(type(x)) for x in (df["checkSun"].unique())]

# short_df = df.iloc [:,:14]
# print (short_df)

def createSppPara(filtered_df):
    final_paragraph = ''
    for _, row in filtered_df.iterrows():
        # "type", "nameCommon", "nameScientific", "maxheightM", "foliageType", "notes"
        final_paragraph += "Species: {}\nCommon name: {}\nMaximum height:{}\n\n".format(row["nameScientific"], row["nameCommon"], row["maxheightM"])
    return (final_paragraph)

userChoice1 = input ('Choose 1 for Sun, 2 for Partial Sun, 3 for Shade')
userChoice2 = input ('Choose 1 for Dry, 2 for Moist, 3 for Wet')
if userChoice1 == "1":
    dfSun = df[df["checkSun"] == True]
    if userChoice2 == "1":
        dfSunDry = dfSun[dfSun["checkDry"] == True]
        print(createSppPara(dfSunDry))
        # print (dfSunDry[["type", "nameCommon", "nameScientific", "maxheightM", "foliageType", "notes"]])
    elif userChoice2 == "2":
        dfSunMoist = dfSun[dfSun["checkMoist"] == True]
        print(createSppPara(dfSunMoist))
        # print (dfSunMoist["nameCommon"])
    elif userChoice2 == "3":
        dfSunWet = dfSun[dfSun["checkWet"] == True]
        print (dfSunWet["nameCommon"])

if userChoice1 == "2":
    dfPartialSun = df[df["checkPartialSun"] == True]
    if userChoice2 == "1":
        dfPartialSunDry = dfPartialSun[dfPartialSun["checkDry"] == True]
        print (dfPartialSunDry["nameCommon"])
    elif userChoice2 == "2":
        dfPartialSunMoist = dfPartialSun[dfPartialSun["checkMoist"] == True]
        print (dfPartialSunMoist["nameCommon"])
    elif userChoice2 == "3":
        dfPartialSunWet = dfPartialSun[dfPartialSun["checkWet"] == True]
        print (dfPartialSunWet["nameCommon"])

if userChoice1 == "3":
    dfShade = df[df["checkShade"] == True]
    if userChoice2 == "1":
        dfShadeDry = dfShade[dfShade["checkDry"] == True]
        print (dfShadeDry["nameCommon"])
    elif userChoice2 == "2":
        dfShadeMoist = dfShade[dfShade["checkMoist"] == True]
        print (dfShadeMoist["nameCommon"])
    elif userChoice2 == "3":
        dfShadeWet = dfShade[dfShade["checkWet"] == True]
        print (dfShadeWet["nameCommon"])
    else:
        print ('please enter 1, 2 or 3')



    



    
    
    # Ask to print each item individually
    # [print(x) for x in speciesList]

    # It's a condensed way to write this:
    # for x in speciesList:
    #     print(x)


    # This is the heart of our slicing in pandas dataframes When we use something
    # that looks like this: df[df["mycolumn"] == "something"]
    # we are iterating each of the values (for each row) from "mycolumn" and evaluating
    # if they are the same as "something" or not. If they are, a True is given. Otherwise
    # False. How does python keep track of what condition is true/false as it goes over
    # the different values of "mycolumn"? It creates a new list, filled only with the
    # verdictsTrue/False. When we pass that list of verdict to our original dataframe,
    # the program gives back a new subdataframe with only the rows where the verdict was True.
    
    #this is what pandas does if it was of type list. But because it's not this code doesn't
    # work.
    # mylist = ["cat", "dog", "rat"]
    # mylistBool = [True, True, False]
    # mylist[mylistBool]
    
    # This code does work! It uses the index of one of the lists (botch lists have the same
    # number of items so it doesn't matter which one we pick) to evaluate from mylistBool, then retrieve
    # from mylist.
    # for index in range(len(mylist)):
    #     if mylistBool[index] == True:
    #         print(mylist[index])
            

    # This is what python sees when passing the column checkSun
    # df[df[False, False, False, False, True] == True]]
    
    
    # print(speciesList)

    # #this is list comprehension
    # speciesList = [x for x in dfSun["nameScientific"].unique()]
    # #this is the same output from the line above but using a traditional for loop
    # speciesList = []
    # for x in dfSun["nameScientific"].unique():
    #     speciesList.append(x)

# e and extract the different values
# that can be found in that column, creating a list. Then, call
# that list tagsSunExp

# This part creates lists with unique records for the different columns in our table
# tagsSunExp = df["Sun Exposure"].unique()
# tagsMoisPref = df["Moisture Preference"].unique()

# This part runs for loops with the purpose of:
#   - Checking if the user input is in the list of valid values for the column of interest
#   - Creating a subdataframe (i.e. creating a new subtable) that narrows the number of possible species

# One for loop for each column in the dataframe that will be used to narrow the search

# for tagExp in tagsSunExp:

# dfSun = df(df['nameScientific']) & (df['checkSun' == True])
#Create a subdataframe that contains only species where sun == true
# dfSun = df[df['checkSun'] == True]
# print (dfSun)

# RUN THIS AT THE END
# Print out the list of candidate species for the user

# speciesList = sub_df["Name - Scientific"].unique()
# for species in speciesList:
#    print(species)


