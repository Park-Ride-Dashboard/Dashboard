# Import necessary libraries
from dash import html, dcc
import dash_bootstrap_components as dbc

#---------stylings---------------------------
SIDEBAR_STYLE = { #style options of the sidebar
    "position": "fixed",
    "top": "3.5rem",
    "right": 0,
    "bottom": 0,
    "width": "auto",
    "height": "93%",
    "padding": "2rem 1rem", #spaces between the content
    "background-color": "#333333",
    "overflow": "scroll",
}

BUTTON_STYLE = { #style of the buttons in the sidebar
    "width": "10rem",
    "height": "3.5rem",
    "text-align":"center",
    "background-color":"white",
    "border": "black",
    "color": "black"
}

#---------------------------------------------



#---------generating of icons-----------------

#trash icon for clearing all filters
FA_icon_Trash = html.I(className="fa fa-trash fa-lg")

#---------------------------------------------



#---------functions-----------------

def get_sidebar() -> html.Div:
    """
    This function defines and returns a Dash layout for the sidebar.

    Returns
    -------
    sidebar:
        The layout of the sidebar of the page including the add_location popup and the advanced filter pop up.
    """


    #documentation for the attributes of single components gets lesser the further down, since its always the same pattern
    sidebar = html.Div(  # Create a div element for the sidebar
        [
            #sidebar visible components
            dbc.Nav(
                [
                    html.H4("Filter Options",style={'color': 'white'}),
                    html.Div(html.Hr(),style={"color": "#b3b3b3"}),
                    html.H5("Location",style={'color': 'white'}),  # Label of the name search bar
                    dbc.Input(  # Input field for the name
                        id="sideboard_name_filter"  ,  # Set the id of the input field to sideboard_name_filter
                        type="text",  # Set the type of the input field to text
                        debounce=False,  # Set the debounce-attribute of the input field to False
                        value=None,  # Set the value of the input field to an empty string
                        placeholder="Location Name",  # Set the placeholder of the input field to Location Name
                        autofocus=True  # Set the autofocus-attribute of the input field to True
                    ),
                    html.Hr(), # Line break
                    html.H5("Occupancy:",style={'color': 'white'}),  # Label for the occupancy input field
                    dbc.RadioItems(  # Radio buttons to select the occupancy
                        options=[  # Define the options of the radio buttons
                                    {'label': 'High', 'value': 'high'},  # Option for high occupancy
                                    {'label': 'Medium', 'value': 'medium'},  # Option for medium occupancy
                                    {'label': 'Low', 'value': 'low'}, # Option for low occupancy
                                    {'label': 'No Filter', 'value': None}  # Option for no occupancy
                                ],
                        value=None,  # Set the value of the radio buttons to None
                        inline=False,  # Set the inline-attribute of the radio buttons to False
                        id="sideboard_occupancy_filter" ,  # Set the id of the radio buttons to sideboard_occupancy_filter
                        style={'color': 'white'} #style of the buttons
                    ),
                    html.Hr(),
                    html.H5("Max. Price per Day (\u20ac)",style={'color': 'white'}),  # Label of the price filter
                    dbc.Input(  # Input field
                        id="sideboard_price_filter" , #ID
                        type="number",  # Set the type of the input field to number
                        debounce=False,  # Set the debounce-attribute of the input field
                        value=None,  # Set the value of the input field
                        placeholder="Price",  # Set the placeholder of the input field

                    ),
                    html.Hr(),
                    dbc.Button(  # Button to filter the locations With all filters / open the advanced filter pop up
                        "Advanced Filter",  # Text of the button
                        id="advanced_filter_button" ,  # Set the id of the button to advanced_filter_button
                        value=999,
                        size= "md",
                        style=BUTTON_STYLE  # Set the style of the button to BUTTON_STYLE
                    ),
                    dbc.Label("Filters active: 0",style = {"margin-top":"2%", "color":"white"}, id="active_filters"), # Number of current filters
                    html.Hr(),
                    dbc.Button(  # Button to clear all filters
                        [FA_icon_Trash, " Clear Filter"],  # Icon + Text of the button
                        id="clear_filter_button" ,  # Set the id of the button to clear_filter_button
                        size= "md",
                        style=BUTTON_STYLE  # Set the style of the button to BUTTON_STYLE
                    ),
                    html.Br(),

                ],
                vertical=True, # allign elements vertically
                pills=True, # "pill" style for components
            ),
            dbc.Modal(  # Modal to display the advanced filter
                        # filters in advanced filter mostly drop down to allow multiple value filtering
                [
                    dbc.ModalHeader(dbc.ModalTitle("Filter all Categories")),  # Header of the modal
                    dbc.ModalBody(  # Body of the modal
                        [
                            dbc.Label("Name of Location:",style = {"margin-top":"2%"}), # Header of the modal
                            dbc.Input(
                                id="modal_advanced_filter_name" , # name filter id
                                type="text",  # Set the type of the input field to text
                                debounce=True,  # Set the debounce-attribute of the input field to True
                                placeholder="Specify location name", #the text which is vialized as long as nothing is choosen
                                value=None  # Set the value of the input field
                            ),
                           dbc.Label("Occupancy:",style = {"margin-top":"2%"}), # occupancy filter
                            dcc.Dropdown(
                                options=[ #options visalized as a dropdown
                                    {'label': 'High', 'value': 'high'},
                                    {'label': 'Medium', 'value': 'medium'},
                                    {'label': 'Low', 'value': 'low'},
                                ],
                                placeholder="Specify occupancy",  #the text which is vialized as long as nothing is choosen
                                id="modal_advanced_filter_occupancy" , # individuell id of this component
                                multi=True,#multiple values can be selected
                            ),
                            dbc.Label("Address:",style = {"margin-top":"2%"}), # adress filter
                            dbc.Input(
                                id="modal_advanced_filter_address" , # individuell id of this component
                                type="text",  # Set the type of the input field to text
                                debounce=True,  # Set the debounce-attribute of the input field to True
                                placeholder="Specify address", #the text which is vialized as long as nothing is choosen
                                value=None  # Set default value
                            ),
                            dbc.Label("Administration:",style = {"margin-top":"2%"}), #administration filter
                            dbc.RadioItems(  # Radio buttons
                                options=[  # Define the options of the radio buttons
                                            {'label': 'yes', 'value': 'yes'},  # administration
                                            {'label': 'no', 'value': 'no'},  # no administration
                                            {'label': 'no specification', 'value': None}  # not specified
                                        ],
                                value=None,  # Set the value of the radio buttons to None
                                inline=True,  # Set the inline-attribute of the radio buttons
                                id="modal_advanced_filter_administration"   # Set the id
                            ),
                            dbc.Label("Type of Facility:",style = {"margin-top":"2%"}), # type of  facility filter
                            dcc.Dropdown(
                                options=[ # options of this charakteristic visalized as a dropdown
                                    {'label': 'car park', 'value': 'car park'},
                                    {'label': 'separate area', 'value': 'separate area'},
                                    {'label': 'at the edge of the road / on the road', 'value': 'at the edge of the road / on the road'},
                                ],
                                placeholder="Specify the type of the facility",#the text which is vialized as long as nothing is choosen
                                id="modal_advanced_filter_kind" , # individuell id of this component
                                multi=True, #multiple inputs are possible
                            ),

                            dbc.Label("Number of Parking Lots (class):",style = {"margin-top":"2%"}), # parking lot filter
                             dcc.Dropdown(
                                 options=[ # options of this charakteristic visalized as a dropdown
                                     {'label': '1-25', 'value': '1-25'},
                                     {'label': '25-50', 'value': '25-50'},
                                     {'label': '50-100', 'value': '50-100'},
                                     {'label': '100-200', 'value': '100-200'},
                                     {'label': '200-1200', 'value': '200-1200'},
                                 ],
                                 placeholder="Specify number of parking slots", #the text which is vialized as long as nothing is choosen
                                 id='modal_advanced_filter_number_parking_lots' , # individuell id of this component
                                 multi=True, #multiple inputs are possible
                             ),
                             dbc.Label("Max. Price per Day (\u20ac):",style = {"margin-top":"2%"}),# price filter
                             dbc.Input(
                                 id="modal_advanced_filter_price" , # individuell id of this component
                                 type="number",  # Set the type of the input field to text
                                 debounce=False,  # Set the debounce-attribute of the input field to True
                                 placeholder="Price in \u20ac", #the text which is vialized as long as nothing is choosen
                                 value=None  # Set the value of the input field to an empty string
                             ),

                            dbc.Label("Road Network Connection:",style = {"margin-top":"2%"}), # transport connection filter
                            dcc.Dropdown(
                                options=[ # options of this charakteristic visalized as a dropdown
                                    {'label': 'superordinate network within the city (interstate)', 'value': 'superordinate network within the city (interstate)'},
                                    {'label': 'superordinate network out of town (interstate)', 'value': 'superordinate network out of town (interstate)'},
                                    {'label': 'subordinate network in the city', 'value': 'subordinate network in the city'},
                                    {'label': 'subordinate network out of town', 'value': 'subordinate network out of town'},
                                ],
                                placeholder="Specify connection", #the text which is visualized as long as long as nothing is choosen
                                id="modal_advanced_filter_road_network_connection" , # individuell id of this component
                                multi=True, #multiple inputs are possible
                            ),


                            dbc.Label("Surrounding Infrastructure:",style = {"margin-top":"2%"}), # surrounding infrastructure filter
                            dcc.Dropdown(
                                options=[# options of this charakteristic visalized as a dropdown
                                    {'label': 'green spaces', 'value': 'green spaces'},
                                    {'label': 'living spaces', 'value': 'living spaces'},
                                    {'label': 'industrial areas', 'value': 'industrial areas'},
                                    {'label': 'industrial parks', 'value': 'industrial parks'},
                                    {'label': 'mixed areas', 'value': 'mixed areas'},
                                ],
                                placeholder="Specify surrounding infrastructure", #the text which is visualized as long as long as nothing is choosen
                                id="modal_advanced_filter_surrounding_infrastructure" , # individuell id of this component
                                multi=True, #multiple inputs are possible
                            ),




                        ]
                    ),
                    dbc.ModalFooter(  # Footer of the modal
                        [
                            dbc.Button(  # Button to apply the filter and close the modal, will keep/save the selected filters
                                "Apply",  # Text of the button
                                color="primary",  # Set the color of the button to primary
                                id="modal_filter_submit_button"   # Set the id of the button to modal_submit_button
                            ),
                            dbc.Button(  # Button to discard the changes and close the the modal, will delete the filters
                                "Discard",  # Text of the button
                                id="modal_filter_cancel_button"   # Set the id of the button to modal_cancel_button
                            ),
                        ]
                    ),
                ],
                id="modal_filter_window" ,  # Set the id of the modal to modal_filter_window
                centered=True,  # Set the centered-attribute of the modal to True
            ),

            dbc.Modal(  # Modal to display the pop up for adding a location
                        # uses single option dropdowns since only one value can be set per characteristic
                [
                    dbc.ModalHeader(dbc.ModalTitle("Add Location")),  # Header of the modal
                     dbc.ModalBody(  # Body of the modal
                        [
                            html.H4("Mandatory Fields:"), # url and location name are mandatory attributes
                            dbc.Label("*API-Link:",style = {"margin-top":"2%"}), # name of the characteristic as a label
                            dbc.Input(
                                placeholder="Specify the API", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_url" , # individuell id of this component
                                type="text",  # Set the type of the input field
                                debounce=True,  # Set the debounce-attribute of the input field
                                value=None  # Set the value of the input field
                            ),
                            dbc.Label("*Location Name:",style = {"margin-top":"2%"}), # name of the characteristic as a label
                            dbc.Input(
                                placeholder="Specify the location name", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_name" , # individuell id of this component
                                type="text",  # Set the type of the input field to text
                                debounce=True,  # Set the debounce-attribute of the input field to True
                                value=None  # Set the value of the input field
                            ),
                            html.H4("Optional Fields:",style = {"margin-top":"5%"}), # nice to have but none of these attributes are necessary to add location
                            dbc.Label("Address:",style = {"margin-top":"2%"}), # name of the characteristic as a label
                            dbc.Input(
                                placeholder="Specify the address", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_address" , # individuell id of this component
                                type="text",  # Set the type of the input field to text
                                debounce=True,  # Set the debounce-attribute of the input field to True
                                value=None  # Set the value of the input field
                            ),
                            dbc.Label("Administration:",style = {"margin-top":"2%"}), # name of the characteristic as a label
                            dcc.Dropdown(
                                options=[ # options of this charakteristic visalized as a dropdown
                                    {'label': 'yes', 'value': 'yes'},
                                    {'label': 'no', 'value': 'no'},
                                ],
                                placeholder="Specify administration", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_administration" # individuell id of this component
                            ),
                            dbc.Label("Type of Facility:",style = {"margin-top":"2%"}), # name of the characteristic as a label
                            dcc.Dropdown(
                                options=[ # options of this charakteristic visalized as a dropdown
                                    {'label': 'car park', 'value': 'car park'},
                                    {'label': 'separate area', 'value': 'separate area'},
                                    {'label': 'at the edge of the road / on the road', 'value': 'at the edge of the road / on the road'},
                                ],
                                placeholder="Specify the type of the facility", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_kind" # individuell id of this component
                            ),

                            dbc.Label("Number of Parking Spots (class):",style = {"margin-top":"2%"}), # name of the characteristic as a label
                            dcc.Dropdown(
                                options=[ # options of this charakteristic visalized as a dropdown
                                    {'label': '1-25', 'value': '1-25'},
                                    {'label': '25-50', 'value': '25-50'},
                                    {'label': '50-100', 'value': '50-100'},
                                    {'label': '100-200', 'value': '100-200'},
                                    {'label': '200-1200', 'value': '200-1200'},
                                ],
                                placeholder="Specify Number of parking spots", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_number_parking_lots"
                            ),
                            dbc.Label("Max Price per Day (\u20ac):",style = {"margin-top":"2%"}),# name of the characteristic as a label
                            dbc.Input(
                                placeholder="Specify the max price in \u20ac", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_price" , # individuell id of this component
                                type="number",  # Set the type of the input field
                                debounce=True,  # Set the debounce-attribute of the input field
                                value=None  # Set the value of the input field
                            ),

                            dbc.Label("Number of Public Transport Connections:",style = {"margin-top":"2%"}), # name of the characteristic as a label
                            dbc.Input(
                                placeholder="Specify the public transport accessibility", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_public_transport" , # individuell id of this component
                                type="text",  # Set the type
                                debounce=True,  # Set the debounce-attribute
                                value=None  # Set the default value
                            ),

                            dbc.Label("Road Network Connection:",style = {"margin-top":"2%"}), # name of the characteristic as a label
                            dcc.Dropdown(
                                options=[ # options of this charakteristic visalized as a dropdown
                                    {'label': 'superordinate network within the city (interstate)', 'value': 'superordinate network within the city (interstate)'},
                                    {'label': 'superordinate network out of town (interstate)', 'value': 'superordinate network out of town (interstate)'},
                                    {'label': 'subordinate network in the city', 'value': 'subordinate network in the city'},
                                    {'label': 'subordinate network out of town', 'value': 'subordinate network out of town'},
                                ],
                                placeholder="Specify the transport connection", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_road_network_connection" # individuell id of this component
                            ),


                            dbc.Label("Surrounding Infrastructure:",style = {"margin-top":"2%"}), # name of the characteristic as a label
                            dcc.Dropdown(
                                options=[ # options of this charakteristic visalized as a dropdown
                                    {'label': 'green spaces', 'value': 'green spaces'},
                                    {'label': 'living spaces', 'value': 'living spaces'},
                                    {'label': 'industrial areas', 'value': 'industrial areas'},
                                    {'label': 'industrial parks', 'value': 'industrial parks'},
                                    {'label': 'mixed areas', 'value': 'mixed areas'},
                                ],
                                placeholder="Specify the surrounding infrastructure", #the text which is visualized as long as long as nothing is choosen
                                id="modal_add_location_surrounding_infrastructure" # individuell id of this component
                            ),



                        ]
                    ),
                     dbc.ModalFooter(  # Footer of the modal
                        [
                            # warning if one of the mandatory fields is not filled out
                            dbc.Label("Fill out all mandatory fields!", id="modal_field_warning" , style={"display":"none", "color":"red"}),
                            dbc.Button(  # Button to add location and close the modal
                                "Add",  # Text of the button
                                color="primary",  # Set the color of the button to primary
                                id="modal_add_location_submit_button"   # Set the id of the button
                            ),
                            dbc.Button(  # Button to close the modal, changes will be discarded
                                "Discard",  # Text of the button
                                id="modal_add_location_cancel_button"   # Set the id of the button
                            ),
                        ]
                    ),
                ],
                id="modal_add_location" ,  # Set the id of the modal
                size="lg",
                centered=True,  # Set the centered-attribute of the modal to True
            ),
            #placeholder div for signal of advanced filter
            html.Div(id="placeholder_div_filter" , style={"display":"none"}),
            #placeholder div for signal of location addition
            html.Div(id="placeholder_div_adding" , style={"display":"none"}),

        ],
        #set the style of the sidebar
        style=SIDEBAR_STYLE,
    )

    return sidebar  # Return the sidebar as a div element

#-------------------------------------------------------------------
