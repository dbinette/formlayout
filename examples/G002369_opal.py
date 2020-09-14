# python 3.7
# PySide2

import datetime
import pprint
import formlayout

#############################################################################

def example_0(arg):
    """Demonstrate as many formlayout variants as possible."""
    
    page0 = [(None,"this page intentionally left blank")]

    page1 = [(None          , "<center><i>This screen illustrates a variety of widgets<br>some appear the same and differ only in their return value</i></center>")  # some info text
            ,(None          , None)   # a divider line
            ,(None          ,"line2")  #("line1","line2","line3"))
            ,("int1"        , 12)
            ,("int2"        , 3456789)
            ,("float1"      , 1.2)
            ,("float2"      , 22.1)
            ,("str1::this is a tooltip"        , "this is a string with a tooltip")
            # note the ' *' is part of the field name.. that seems awkward
            ,("str2 *::the red star indicates a required item", "")
            ,("str3 *"      , "this required item has no tooltip")
            ,("str4"        , "just a string")

                              # [ list : drop down list with item  '2' selected
            ,("list1"       , [3, "0", "1", "2", "3", "4"])
                              # [ list : drop down list with item  '--' selected
            ,("list2"       , ["--", ("none", "None"), ("--", "Dashed"),("-.", "DashDot"), ("-", "Solid"),("steps", "Steps"), (":", "Dotted")])
                              # ( tuple : vertical radio buttons with item  '--' selected
            ,("list3"       , ("--", ("none", "None"), ("--", "Dashed"),("-.", "DashDot"), ("-", "Solid"),("steps", "Steps"), (":", "Dotted")))
                              # ( tuple : vertical radio buttons with item 'Solid' selected
            ,("list4"       , (4, "None", "Dashed", "DashDot", "Solid"," Steps", "Dotted") )
                              # [ list : drop down list with item 'Solid' selected
            ,("list5"       , [4, "None", "Dashed", "DashDot", "Solid"," Steps", "Dotted"] )
            ,(None          , "linebreak1")
            ,("slider1"     , "slider:500:1000")
            ,("slider2"     , "slider:-100:100@-50")
            ,(None          , "linebreak2")
            ,("font1"       , ("Arial", 10, False, True))
            ,("color1"      , "red")
            ,("color2"      , "green")
            ,("color4"      , "#0000ff")
            ,("color3"      , "#b00") # this format does not seem to be accepted
            # note extended syntax begin {
            ,("checkbox1"   , ("0h"    ,"cb1a","cb1b","cb1c","cb1d")) # horizontal default off
            ,("checkbox2"   , ("1h"    ,"cb2a","cb2b","cb2c","cb2d")) # horizontal default on
            ,("checkbox3"   , ("0h1010","cb3a","cb3b","cb3c","cb3d")) # horizontal specified states
            ,("checkbox4"   , ("1v0101","cb4a","cb4b","cb4c","cb4d")) # vertical specified states
            # note extended syntax end }
            ,("checkbox5"   , False)
            ,("checkbox6"   , True)
            ,("radio1"      , ((2, ("radio1a","radio1alabel") ,("radio1b","radio1blabel") ,("radio1c","radio1clabel") ,("radio1d","radio1dlabel") )))
            ,("password1"   , "password")
            ,("time1"       , datetime.time(12, 34, 56))
            ,("date1"       , datetime.date(2010, 12, 24))
            ,("datetime1"   , datetime.datetime(2010, 12, 24))
            ,("calendar1"   , "calendar")
            ,("calendar2"   , "calendar:")
            ,("calendar3"   , "calendarM")
            ,("calendar4"   , "calendarM@2010,12,24")
            ,("file1"       , "file")
            ,("file2"       , "file:*.py")
            ,("dir1"        , "dir")
            ,("str2"        , """str2 this is a \nMULTILINE\nstring""")
            ,("image1"      , "Qt.jpg")  # will not render if there is a label
            ,(None          , "Qt.jpg")  # file must exist in local folder
            ]

    page2 = [("pressure"     ,123.4)
            ,("velocity"     ,36   )
            ,("temperature"  ,25.0 )
            ,("Calibration certificate #", "s/n acme xxx")
            ]
        
    def on_apply_pressed(data,other):
        print("woohoo!!! you pressed apply and the data was: {}".format(data))
        #print(f"other data was {other}")`
  
    result = formlayout.fedit(((page1, "page1tab", "page 1 Tabcomment" + " "*100)  # 100 space padding required to expand tabbed form
                              ,(page2 ,"page2tab", "page 2 Tabcomment")
                              )
                              ,title        = arg
                              ,comment      = "This is comment1."  # gets lost on tabbed dialog
                              ,icon         = "Qt.jpg"
                              ,parent       = None
                              ,apply        = ("&APPLY",on_apply_pressed)
                              ,ok           = "&OKAY"
                              ,cancel       = "&NO-WAY"
                              ,result       = "dict"     # ["list", "dict", "OrderedDict", "JSON", "XML"]
                              ,outfile      = None       # "outfile"  # will get .py ,.json ,.xml file extension
                              ,type         = "form"     # ["form", "questions"]
                              ,scrollbar    = True
                              ,background_color = None
                              #,widget_color= None
                              # djb additions
                              ,size         = (600,1000)
                              ,position     = (600,200)
                             )
    return result

#############################################################################
def example_1(arg):    
    """A simple example."""

    formfields = [("Name"    , "Paul")
                 ,(None      , None)
                 ,(None      , "Information:")
                 ,("Age"     , 30)
                 ,("Sex"     , [0, "Male", "Female"])
                 ,("Size"    , 12.1)
                 ,("Eyes"    , "cyan")
                 ,("Married" , True)
                 ]
    result = formlayout.fedit(formfields
                             ,result    = "dict"    # ["list", "dict", "OrderedDict", "JSON", "XML"]
                             ,type      = "form"    # ["form", "questions"]
                             ,title     = arg
                             ,comment   = "This is just an <b>example</b>."
                             )
    return result

#############################################################################
def example_2(arg):    
    """A form that uses scrollbars."""
    page1 = [("pressure"        , 123.4)
            ,("velocity"        , 36   )
            ,("temperature"     , 25.0 )
            ,("serial Number"   , "s/n acme xxx")
            ]

    page2 = [("Name"        , "Paul")
            ,(None          , None)
            ,(None          , "Qt.jpg")
            ,(None          , "Information:")
            ,("Age"         , 30)
            ,("Sex"         , [0, "Male", "Female"])
            ,("Size"        , 12.1)
            ,("Eyes"       , "cyan")
            ,("Hair"        , "#954535")
            ,("Married1"    , True)
            ,("Married2"    , True)
            ,("Married3"    , True)
            ,("Married4"    , True)
            ,("Married5"    , True)
            ,("Married6"    , True)
            ,("Married7"    , True)
            ,("Married8"    , True)
            ,("Married9"    , True)
            ,("Married10"   , True)
            ,("Married11"   , True)
            ,("Married12"   , True)
            ,("Married13"   , True)
            ,("Married14"   , True)
            ,("Married15"   , True)
            ,("Married16"   , True)
            ,("Married17"   , True)
            ,("Married18"   , True)
            ,("Married19"   , True)
            ,("Married20"   , True)
            ]


    result = formlayout.fedit(
                             ((page1,"page1","<h1>title for page1</h1><hr>")
                             ,(page2,"page2","title for page2")
                             )
                             ,result            = "dict"    # ["list", "dict", "OrderedDict", "JSON", "XML"]
                             ,type              = "form"    # ["form", "questions"]
                             ,title             = arg
                             ,comment           = "This is just an <b>example</b>."
                             ,scrollbar         = True
                             ,background_color  = "cyan"
                             ,widget_color      = "pink"
                             )
    return result

#############################################################################
def example_3(arg):
    """Groups and lists. example code from other places"""

    def create_datalist_example():
        return [("str", "this is a string"),
                ("str", """this is a 
                MULTILINE
                string"""),
                ("list", [0, "1", "3", "4"]),
                ("list2", ["--", ("none", "None"), ("--", "Dashed"),("-.", "DashDot"), ("-", "Solid"),("steps", "Steps"), (":", "Dotted")]),
                ("float", 1.2),
                (None, "Other:"),
                ("int", 12),
                ("font", ("Arial", 10, False, True)),
                ("color", "#123409"),
                ("bool", True),
                ("date", datetime.date(2010, 10, 10)),
                ("datetime", datetime.datetime(2010, 10, 10)),]
        
    def create_datagroup_example():
        datalist = create_datalist_example()
        return ((datalist, "Category 1", "Category 1 comment"),
                (datalist, "Category 2", "Category 2 comment"),
                (datalist, "Category 3", "Category 3 comment"))
    
    datalist = create_datalist_example()

    
    #--------- datagroup inside a datagroup example
    datalist  = create_datalist_example()
    datagroup = create_datagroup_example()
    result    = formlayout.fedit(((datagroup, "Title 1", "Tab 1 comment"),
                                  (datalist ,"Title 2", "Tab 2 comment"),
                                  (datalist ,"Title 3", "Tab 3 comment")),
                                  title = arg)
    return result


#############################################################################
def example_4(arg):    
    """Present Multiple pages, no scroll bars."""


    # action buttons, other than apply, would be nice
    #def on_button_1(arg1,arg2):        print(f"button_1 pressed({arg1},{arg2}")
    #def on_button_2(arg1,arg2):        print(f"button_2 pressed({arg1},{arg2}")
    #def on_button_3(arg1,arg2):        print(f"button_3 pressed({arg1},{arg2}")

    pageV = [("pressure"      ,123.4)
            ,("velocity"      ,36   )
            ,("temperature"   ,25.0 )
            ,("serial Number" ,"s/n acme xxx")
            ]

    pageT   = [("Name"  ,"something")
             ,(None     ,None)
             ]

    pageP   = [("Name"   ,"something")
              ,(None     ,None)
              ]

    pageR =   [("Name *::this is a tooltip" , "something")
              ,(None            , None)
              #,("pumpit"        , ("button",on_button_1))
              #,("drain valve"   , ("button",on_button_2))
              #,("fill tank"     , ("button",on_button_3))
              ,("motion","slider:500:1000")
              ,("radios",(2,("a","12"),("b","22"),("c","34"),("d","36")))

              ]

    result = formlayout.fedit(
                             ((pageV,"Valve"        ,"valve page")
                             ,(pageT,"Tank"         ,"tank page")
                             ,(pageP,"Pump"         ,"pump page")
                             ,(pageR,"Run Controls" ,"Run controls")
                             )
                             ,result    = "dict"    # ["list", "dict", "OrderedDict", "JSON", "XML"]
                             ,type      = "form"    # ["form", "questions"]
                             ,title     = arg
                             ,comment   = "This is just an <b>example</b>."
                             )
    return result


#############################################################################

def multi():
    """Scan for fuynctions named examples_* and offer them to the user."""
    while True:
        
        #try:
        #    # the messagebox is is not included in the standard formlayout
        #    if not formlayout.messageBoxYesNo("so tell me","are you ready to rock?"):
        #        break
        #except:
        #    pass

        # build up a list of examples from this code units python namespace
        # formlayout wants the selected value as the first item
        examples = (1,*[ x for x in globals() if x.startswith("example_") ])

        # create a form with two controls, we only use the first one
        formdata = [("UsersChoice", examples) 
                   ,("greeting"   , "salut!") 
                   ,(None         , "<hr>") 
                   ,(None         , "<center style='background-color:pink;'>CANCEL will exit the program!</small>") 
                   ]

        # get the users choices
        result = formlayout.fedit(formdata
                                 ,result    = "dict"
                                 ,title     = "a plethora of examples"
                                 ,comment   = "<center style='margin:0 25px 0 25px;'>Select the example <b>you</b> want to run<br><i>although i suggest you use example 0</i></center>"
                                 ,scrollbar = True
                                 #,style    = "QDialog{background:#bff; color:blue;} *{color:blue};" # not with background or widget color
                                 ,style     = "QDialog{background:url(opal.jpg); color:blue;} *{color:blue};" # not with background or widget color
                                 ,icon      = "opal.jpg"
                                 )
        if result:
            # get the choice of example
            examplename = examples[result["UsersChoice"]]
            greeting    = "{} ( {} )".format(examplename,result["greeting"])
            print("**********************************")
            print(examplename)
            print("**********************************")
            # invoke the selected example function
            result_from_example = globals()[examplename](greeting)

            # all the examples return the form result,  format it for display via PrettyPrinter
            print("the form data as rendered by pprint")
            pprint.PrettyPrinter(indent=2).pprint(result_from_example)
        else:
            break

#############################################################################
if __name__ == "__main__":
    multi()

#############################################################################
# end


