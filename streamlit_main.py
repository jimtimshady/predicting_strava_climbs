###########
#### Streamlit Main #############

import streamlit as st
import importlib.util


# Create a container element
container = st.container()

# Set the background image for the container
with container:
    st.image('climb.jpg', output_format='auto', width=800)

# Add your app content inside the container
with container:
    # Create title
    st.markdown("<h1 style='text-align: center; font-size: 40px'>Cycling Ascent Time Prediction</h1>", unsafe_allow_html=True)

    # Create two columns
   # col1, col2 = st.columns((1, 2))
    col1, _, col2 = st.columns((1, 0.1, 2))

    # Create select menus in the first column
    with col1:
        rider_select = st.selectbox("Rider", ["Jim Shady"])
        model_select = st.selectbox("Model", ["model_regression_lin", "model_HGB_Regressor", "model_HGB_Regressor2", "model_RF_Regressor", "model_ElasticNetCV"])
        ascent_select = st.selectbox("Ascent", ["Stelvio", "Galibier", "Mont Ventoux", "Alp d' Huez", "Col du Tourmalet", "Alto de letras", "Teide", "Monte Grappa", "Hawk Hill", "Brocken"])

        # Create a button "Run"
        run_button = st.button("Run")

        # Create a reset button
        reset_button = st.button("Reset")

    # Create footer in the second column
    with col2:
        st.markdown("")

    # Show the result or error message
        if run_button:
            spec = importlib.util.spec_from_file_location("module.name", f"{model_select}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            df_model = module.df_famous_climbs
    
            ascent_info = df_model.loc[df_model["climb_name"] == ascent_select]
    
            st.subheader(f"{ascent_select}")
    
            st.write("**Ascent Information**", markdown=True)         
            st.text(f"Distance: {ascent_info['distance'].values[0]} m")
            st.text(f"Average Grade: {ascent_info['average_grade'].values[0]}%")
            st.text(f"Maximum Grade: {ascent_info['maximum_grade'].values[0]}%")
            st.text(f"Elevation High: {ascent_info['elevation_high'].values[0]} m")
            st.text(f"Elevation Low: {ascent_info['elevation_low'].values[0]} m")
            
            
            # Calculate the total elevation gain
            total_elevation_gain = ascent_info['elevation_high'].values[0] - ascent_info['elevation_low'].values[0]

            # Display the total elevation gain
            st.text(f"Total Elevation Gain: {total_elevation_gain:.2f} m")

            # predictions:
            st.write("**Prediction**", markdown=True)         

            st.text(f"Predicted elapsed time for {ascent_select}: {ascent_info['predicted_elapsed_time_minutes'].values[0]} minutes")
            
            st.write("**Model Quality Metrics**", markdown=True)

            st.text(f"MSE: {module.mse:.4f}")
            
            st.text(f"RMSE: {module.rmse:.4f}")
            
            st.text(f"MAE: {module.mae:.4f}")
            
            st.text(f"R2: {module.r2:.4f}")
    
        else:
            st.write("No model yet implemented")