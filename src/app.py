import streamlit as st
import pandas as pd
import google.generativeai as genai
import json
import os

# Configure the Gemini API
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]  # Store your API key in Streamlit secrets
genai.configure(api_key=GOOGLE_API_KEY)

def generate_schedule_prompt(num_days, topics, knowledge_scores, extra_notes):
    """Generate a detailed prompt for the AI scheduler."""
    prompt = f"""Create a detailed study schedule for the following parameters:
    
Number of Days: {num_days}
Topics: {', '.join(topics)}
Knowledge Levels: {json.dumps(knowledge_scores, indent=2)}
Additional Notes: {extra_notes}

Please create a day-by-day study schedule that:
1. Prioritizes topics with lower knowledge scores
2. Includes review sessions for previously covered topics
3. Balances the workload across the {num_days} days
4. Takes into account the additional notes provided

Format the schedule as a clear, day-by-day plan with specific topics and activities for each day."""

    return prompt

def get_ai_schedule(prompt):
    """Get schedule from Gemini API."""
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate the schedule
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        return f"Error generating schedule: {str(e)}"

def main():
    # Set page title and header
    st.title("AI Quiz Scheduler")
    st.header("Input Your Study Parameters")

    # Number of days input
    num_days = st.number_input(
        "Number of Days",
        min_value=1,
        max_value=365,
        value=7,
        help="Enter the number of days for your study schedule"
    )

    # Topics input (comma-separated)
    topics_input = st.text_area(
        "Topics (comma-separated)",
        help="Enter your topics separated by commas"
    )

    # Initialize knowledge_scores so it always exists
    knowledge_scores = {}

    # Convert topics to list and create knowledge score inputs
    if topics_input:
        topics = [topic.strip() for topic in topics_input.split(",")]
        
        # Create input fields for each topic
        st.subheader("Knowledge Scores")
        for topic in topics:
            if topic:  # Only create input if topic is not empty
                knowledge_scores[topic] = st.slider(
                    f"Knowledge Score for {topic}",
                    min_value=1,
                    max_value=5,
                    value=3,
                    help=f"Rate your current knowledge of {topic} from 1-5"
                )

    # Extra notes input
    extra_notes = st.text_area(
        "Extra Notes",
        help="Add any additional notes or requirements"
    )

    # Submit button
    if st.button("Generate Schedule"):
        if not topics_input:
            st.error("Please enter at least one topic.")
            return

        # Show a spinner while generating the schedule
        with st.spinner("Generating your personalized study schedule..."):
            # Generate the prompt
            prompt = generate_schedule_prompt(
                num_days=num_days,
                topics=topics,
                knowledge_scores=knowledge_scores,
                extra_notes=extra_notes
            )
            
            # Get the schedule from the AI
            schedule = get_ai_schedule(prompt)
            
            # Display the schedule
            st.success("Schedule Generated!")
            st.markdown("### Your Personalized Study Schedule")
            st.markdown(schedule)
            
            # Display the collected data
            with st.expander("View Collected Data"):
                data = {
                    "Number of Days": num_days,
                    "Topics": topics_input,
                    "Knowledge Scores": knowledge_scores,
                    "Extra Notes": extra_notes
                }
                st.json(data)

if __name__ == "__main__":
    main() 