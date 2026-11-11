import streamlit as st

st.set_page_config(
page_title=&quot;AI Virtual Lab&quot;,
page_icon=&quot;��&quot;,
layout=&quot;wide&quot;
)

st.title(&quot;�� AI VIRTUAL LAB&quot;)
st.subheader(&quot;Artificial Intelligence – Problem Solving Laboratory&quot;)

st.write(
&quot;Welcome to the AI Virtual Lab! &quot;
&quot;Explore classical Artificial Intelligence problems &quot;
&quot;through interactive experiments.&quot;
)

experiments = {
&quot;Tic-Tac-Toe&quot;: &quot;Game playing and Minimax algorithm&quot;,
&quot;8-Queen Problem&quot;: &quot;Constraint satisfaction and backtracking&quot;,
&quot;Chess Problem&quot;: &quot;Game trees and search algorithms&quot;,
&quot;Tower of Hanoi&quot;: &quot;Recursion and state-space representation&quot;,
&quot;Travelling Salesperson&quot;: &quot;Combinatorial optimisation&quot;,
&quot;Monkey and Banana&quot;: &quot;State-space search and planning&quot;,
&quot;Cryptarithmetic&quot;: &quot;Constraint satisfaction&quot;,
&quot;Block World&quot;: &quot;AI planning and goal-based problem solving&quot;
}

choice = st.sidebar.selectbox(
&quot;Select an AI Experiment&quot;,
list(experiments.keys())

)

st.header(choice)
st.info(experiments[choice])

st.markdown(&quot;---&quot;)
st.subheader(&quot;Experiment Instructions&quot;)

st.write(&quot;1. Understand the problem.&quot;)
st.write(&quot;2. Identify the initial state and goal state.&quot;)
st.write(&quot;3. Study the algorithm.&quot;)
st.write(&quot;4. Run the experiment.&quot;)
st.write(&quot;5. Observe and record the result.&quot;)

if choice == &quot;Tic-Tac-Toe&quot;:
st.write(&quot;Tic-Tac-Toe experiment will be developed here.&quot;)
elif choice == &quot;8-Queen Problem&quot;:
st.write(&quot;8-Queen visualisation will be developed here.&quot;)
elif choice == &quot;Chess Problem&quot;:
st.write(&quot;Chess experiment will be developed here.&quot;)
elif choice == &quot;Tower of Hanoi&quot;:
st.write(&quot;Tower of Hanoi simulation will be developed here.&quot;)
elif choice == &quot;Travelling Salesperson&quot;:
st.write(&quot;Travelling Salesperson simulation will be developed here.&quot;)
elif choice == &quot;Monkey and Banana&quot;:
st.write(&quot;Monkey and Banana problem will be developed here.&quot;)
elif choice == &quot;Cryptarithmetic&quot;:
st.write(&quot;Cryptarithmetic solver will be developed here.&quot;)
elif choice == &quot;Block World&quot;:
st.write(&quot;Block World simulation will be developed here.&quot;)

st.markdown(&quot;---&quot;)

st.caption(&quot;EEE Department | AI Virtual Laboratory&quot;)
