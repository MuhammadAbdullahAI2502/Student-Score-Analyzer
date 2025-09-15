import statistics
import matplotlib.pyplot as plt
import streamlit as st

def main():
    st.title("📊 Student Scores Analyzer")

    # Input scores
    scores_input = st.text_area(
        "Enter the scores separated by spaces:",
        placeholder="e.g. 45 67 89 92"
    )

    if st.button("Analyze Scores"):
        if not scores_input.strip():
            st.warning("⚠️ Please enter some scores first.")
            return

        try:
            # Convert input string to list of scores
            scores_list = list(map(float, scores_input.split()))
            scores_list.sort()

            # Calculate statistics
            mean_val = statistics.mean(scores_list)
            median_val = statistics.median(scores_list)
            stdev_val = statistics.stdev(scores_list) if len(scores_list) > 1 else 0
            min_val = min(scores_list)
            max_val = max(scores_list)
            score_range = max_val - min_val
            above_avg = [s for s in scores_list if s > mean_val]

            # Display results
            st.subheader("📈 Results")
            st.write("- **Scores in ascending order:**", scores_list)
            st.write(f"- **Average (Mean):** {mean_val:.2f}")
            st.write(f"- **Median:** {median_val:.2f}")
            st.write(f"- **Standard Deviation:** {stdev_val:.2f}")
            st.write(f"- **Minimum:** {min_val}")
            st.write(f"- **Maximum:** {max_val}")
            st.write(f"- **Range:** {score_range}")
            st.write(f"- **Scores above average:** {above_avg if above_avg else 'None'}")

            # Plot scores
            plt.figure(figsize=(6, 4))
            plt.plot(range(1, len(scores_list) + 1), scores_list, marker="o", label="Scores", color="blue")

            plt.axhline(mean_val, linestyle="--", color="red", label="Mean")
            plt.axhline(median_val, linestyle="--", color="green", label="Median")
            if stdev_val > 0:
                plt.axhline(stdev_val, linestyle="--", color="orange", label="Std Dev")
            plt.axhline(min_val, linestyle="--", color="purple", label="Min")
            plt.axhline(max_val, linestyle="--", color="pink", label="Max")

            plt.xlabel("Students")
            plt.ylabel("Scores")
            plt.title("Students Scores")
            plt.legend()
            plt.grid(True)

            st.pyplot(plt)

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
