import dash
import dash_bootstrap_components as dbc 
from dash import dcc, html
from dash.dependencies import Input, Output

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Function to create a slider component
def create_slider(label, min_val, max_val, default_val, step_val, marks, slider_id, output_id):
    return html.Div([
        html.Label(label),
        dcc.Slider(
            min=min_val,
            max=max_val,
            value=default_val,
            step=step_val,
            id=slider_id,
            marks=marks,
            #style={'width': '80%'}
        ),
        html.Div(id=output_id),
        html.Br()
    ])

# Define your layout using Dash components
app.layout = html.Div([
    html.H3("Cattle Decision Tool for Drought Period (short-term)", style={'margin-bottom': '40px'}),
    html.P("Imagine you have a cow-calf operation. Now is a drought period - feed is scarce. ", style={'margin-bottom': '40px'}),
    html.P("It is costly to maintain the cow-calf pair. You may buy hay to keep the cow-calf.", style={'margin-bottom': '40px'}),
    html.P("So, should you sell your pair of cow-calf now or later?", style={'margin-bottom': '40px'}),
    html.P("The following decision tool aims to shed light on this decision. ", style={'margin-bottom': '40px'}),
    html.P("To do so, we estimate the minimum selling price for your cow to break even.", style={'margin-bottom': '40px'}),
    html.P("This tool is solely for educational purposes.", style={'margin-bottom': '40px'}),
    html.H4("A. Cow-calf Current Value", style={'margin-bottom': '40px'}),
    html.H6("Scroll the bar to determine the CURRENT value of your cow.", style={'margin-bottom': '40px'}),
    create_slider('A.1 Current Cow Value ($/head)', 0, 4000, 1800, 0.1, {i: f'${i}' for i in range(0, 4001, 500)},  'cow-value-slider', 'cow-value-output'),
    html.H6("Scroll the bar to determine the CURRENT calf weight and price.", style={'margin-bottom': '40px'}),
    create_slider('A.2 Current Calf Weight (lbs/head)', 0, 1000, 0, 0.1, {i: f'{i}' for i in range(0, 1001, 200)}, 'calf-weight-slider', 'calf-weight-output'),
    create_slider('A.3 Current Calf Price ($/lb)', 0, 20, 0, 0.1, {i: f'${i}' for i in range(0, 21, 2)}, 'calf-price-slider', 'calf-price-output'),
    html.H4("B. Future calf value", style={'margin-bottom': '40px'}),
    html.H6("Now let's assume the FUTURE calf price and weight.", style={'margin-bottom': '40px'}),
    create_slider('B.1 Future calf weight (lbs/head)', 0, 1000, 600, 0.1, {i: f'{i}' for i in range(0, 1001, 200)}, 'fc-w-slider', 'fc-w-output'),
    create_slider('B.2 Future calf price ($/lb)', 0, 20, 2.25, 0.1, {i: f'${i}' for i in range(0, 21, 2)}, 'fc-p-slider', 'fc-p-output'),
    html.H4("C. Typical cow cost", style={'margin-bottom': '40px'}),
    html.H6("In general, what is your annual cow cost?", style={'margin-bottom': '40px'}),
    create_slider('C.1 Annual Costs per Cow ($/cow)', 0, 2000, 1000, 0.1, {i: f'${i}' for i in range(0, 2001, 200)}, 'annual-cost-per-cow-slider', 'annual-cost-per-cow-output'),
    html.H6("How much of your annual cow cost has already been spent?", style={'margin-bottom': '40px'}),
    create_slider('C.2 Amount of Cow Cost Already Incurred (%)', 0, 100, 40, 0.1, {i: f'%{i}' for i in range(0, 101, 10)}, 'cow-cost-incurred-slider', 'cow-cost-incurred-output'),
    html.H4("D. Additional costs to keep the pair", style={'margin-bottom': '40px'}),
    html.P("Here we have two options (or two scenarios).", style={'margin-bottom': '10px'}),
    html.P("First, you already the know total estimated costs to keep the animals. If so, scroll the following bar. Otherwise, let it be zero.", style={'margin-bottom': '40px'}),
    html.H6("What is the total cost to keep the animals?", style={'margin-bottom': '40px'}),
    create_slider('D.1 Cost to keep the animal ($)', 0, 1500, 0, 0.1, {i: f'${i}' for i in range(0, 1501, 200)},  'cost-to-keep-the-animal-slider', 'cost-to-keep-the-animal-output'),
    html.P("The tool will consider detailed costs if you leave zero in the previous bar. The detailed costs are the second option (or scenario). ", style={'margin-bottom': '40px'}),
    html.H6("What is the total cost to keep the animals in detail?", style={'margin-bottom': '40px'}),
    html.P("Scroll the following bars to provide a detailed estimation of the total costs.", style={'margin-bottom': '40px'}),
    create_slider('D.2 Days feeding hay (days)', 0, 365, 210, 1, {i: f'{i}' for i in range(0, 366, 30)}, 'days-feeding-hay-slider', 'days-feeding-hay-output'),
    create_slider('D.3 Amount of hay fed (lbs/head/day)', 0, 60, 25, 0.1, {i: f'{i}' for i in range(0, 61, 10)}, 'amount-of-hay-fed-slider', 'amount-of-hay-fed-output'),
    create_slider('D.4 Hay price ($/ton)', 0, 1200, 600, 0.1, {i: f'${i}' for i in range(0, 1201, 200)}, 'hay-price-slider', 'hay-price-output'),
    create_slider('D.5 Other feed costs ($/day)', 0, 50, 0, 0.1, {i: f'${i}' for i in range(0, 51, 10)}, 'other-feed-costs-slider', 'other-feed-costs-output'),
    create_slider('D.6 All other costs ($/cow)', 0, 300, 0, 0.1, {i: f'${i}' for i in range(0, 301, 30)}, 'all-other-costs-slider', 'all-other-costs-output'),
    create_slider('D.7 Holding days (days)', 0, 365, 210, 1, {i: f'{i}' for i in range(0, 366, 30)}, 'holding-days-slider', 'holding-days-output'),
    create_slider('D.8 Interest rate for operating loans (%)', 0, 30, 5.5, 0.1, {i: f'%{i}' for i in range(0, 31, 5)}, 'interest-rate-for-operating-loans-slider', 'interest-rate-for-operating-loans-output'),

    # Add a div for displaying current calf value
    
    html.H3("Results", style={'margin-bottom': '40px'}),
    html.P("We calculate the following results given the values you chose in the bars. ", style={'margin-bottom': '10px'}),
    html.P("Below the results, we provide the formulas used to obtain the output values.", style={'margin-bottom': '40px'}),
    html.Div(id='current-calf-value-output'),
    html.P("R.1 = A.2 x A.3", style={'margin-bottom': '40px'}),
    html.Div(id='current-animal-value-output'),
    html.P("R.2 = A.1 + R.1", style={'margin-bottom': '40px'}),
    html.Div(id='future-calf-value-output'),
    html.P("R.3 = B.1 x B.2", style={'margin-bottom': '40px'}),
    html.Div(id='annual-cow-cost-output'),
    html.P("R.4 = C.1 x (1 - C.2)", style={'margin-bottom': '40px'}),
    html.Div(id='holding-cost-output'),
    html.P("If D.1 > 0, R.5 = D.1", style={'margin-bottom': '5px'}),
    html.P("Otherwise, R.5 = [(D.2 X D.3) X (D.4/2000)] + (D.5 X D.7) + D.6", style={'margin-bottom': '40px'}),
    html.Div(id='interest-on-additional-cost-output'),
    html.P("R.6 = R.5 X [ (D.8/360) x D.7]", style={'margin-bottom': '40px'}),
    html.Div(id='total-cost-to-hold-output'),
    html.P("R.7 = R.4 + R.5 + R.6", style={'margin-bottom': '40px'}),
    html.Div(id='break-even-output'),
    html.P("R.2 + R.7 - R.3", style={'margin-bottom': '40px'}),
    html.Br(),
], style={'margin': '40px'}) 

# Define callback functions to update the outputs
@app.callback(
    [Output('cow-value-output', 'children'),
     Output('calf-weight-output', 'children'),
     Output('calf-price-output', 'children'),
     Output('fc-w-output', 'children'),
     Output('fc-p-output', 'children'),
     Output('annual-cost-per-cow-output', 'children'),
     Output('cow-cost-incurred-output', 'children'),
     Output('cost-to-keep-the-animal-output', 'children'),
     Output('days-feeding-hay-output', 'children'),
     Output('amount-of-hay-fed-output', 'children'),
     Output('hay-price-output', 'children'),
     Output('other-feed-costs-output', 'children'),
     Output('all-other-costs-output', 'children'),
     Output('holding-days-output', 'children'),
     Output('interest-rate-for-operating-loans-output', 'children'),
     Output('current-calf-value-output', 'children'),
     Output('current-animal-value-output', 'children'),
     Output('future-calf-value-output', 'children'),
     Output('annual-cow-cost-output', 'children'),
     Output('holding-cost-output', 'children'),
     Output('interest-on-additional-cost-output', 'children'),
     Output('total-cost-to-hold-output', 'children'),
     Output('break-even-output', 'children')],
    [Input('cow-value-slider', 'value'),
     Input('calf-weight-slider', 'value'),
     Input('calf-price-slider', 'value'),
     Input('fc-w-slider', 'value'),
     Input('fc-p-slider', 'value'),
     Input('annual-cost-per-cow-slider', 'value'),
     Input('cow-cost-incurred-slider', 'value'),
     Input('cost-to-keep-the-animal-slider', 'value'),
     Input('days-feeding-hay-slider', 'value'),
     Input('amount-of-hay-fed-slider', 'value'),
     Input('hay-price-slider', 'value'),
     Input('other-feed-costs-slider', 'value'),
     Input('all-other-costs-slider', 'value'),
     Input('holding-days-slider', 'value'),
     Input('interest-rate-for-operating-loans-slider', 'value')]
)
def update_output(cow_value, calf_weight, calf_price, future_calf_weight, future_calf_price, annual_cost_per_cow, cow_cost_incurred, cost_to_keep_the_animal, days_feeding_hay, amount_of_hay_fed, hay_price, other_feed_costs, all_other_costs, holding_days, interest_rate_for_operating_loans):
    current_calf_value = calf_weight * calf_price  # Calculate Current Calf Value
    current_animal_value = cow_value + current_calf_value
    future_calf_value = future_calf_weight * future_calf_price  # Calculate Future Calf Value
    annual_cow_cost = annual_cost_per_cow*(1-(cow_cost_incurred/100))
    if cost_to_keep_the_animal > 0:
        holding_cost = cost_to_keep_the_animal
    else:
        holding_cost = ((days_feeding_hay * amount_of_hay_fed) * (hay_price / 2000)) + (other_feed_costs * holding_days) + all_other_costs
    interest_on_additional_cost = holding_cost*((interest_rate_for_operating_loans/100) /360)*holding_days
    total_cost_to_hold = annual_cow_cost + holding_cost + interest_on_additional_cost
    break_even = current_animal_value + total_cost_to_hold - future_calf_value
    return (
        f' ${cow_value}',
        f' {calf_weight} lbs',
        f' ${calf_price}',
        f' {future_calf_weight} lbs',
        f'${future_calf_price:.2f}',
        f'${annual_cost_per_cow}',
        f' {cow_cost_incurred}%',
        f'${cost_to_keep_the_animal}',
        f'Days: {days_feeding_hay}',
        f' Lbs/head/day: {amount_of_hay_fed}',
        f' $/ton: {hay_price}',
        f'$/day: {other_feed_costs}',
        f'$/cow: ${all_other_costs}',
        f'Days: {holding_days}',
        f'{interest_rate_for_operating_loans}%',
        f'R.1 Current Calf Value: ${current_calf_value:.2f}',
        f'R.2 Current animal value (cow + calf): ${current_animal_value:.2f}',
        f'R.3 Future calf value: ${future_calf_value:.2f}',
        f'R.4 Annual cow cost: ${annual_cow_cost:.2f}',
        f'R.5 Holding cost: ${holding_cost:.2f}',
        f'R.6 Interest on addional costs: ${interest_on_additional_cost:.2f}',
        f'R.7 Total addional costs to hold: ${total_cost_to_hold:.2f}',
        f'If the forecasted cow value is higher than ${break_even:.2f}, financially, it is interesting to keep the cow.',
    )

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080))) 
